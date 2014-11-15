from tkinter import *
from tkinter import ttk
from functools import partial
import copy,random
    
root = Tk()
root.title("Chessboard")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


class GUI:
    def __init__(self,host,port):
        import socket,sys
        self.transmitnumbers = [] # the numbers that go to the server
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))
        
        self.pieces = {}
        self.pieces["BlackRook"] = PhotoImage(file="pieces/BlackRook.svg.png").subsample(2,2)
        self.pieces["BlackKnight"] = PhotoImage(file="pieces/BlackKnight.svg.png").subsample(2,2)
        self.pieces["BlackBishop"] = PhotoImage(file="pieces/BlackBishop.svg.png").subsample(2,2)
        self.pieces["BlackQueen"] = PhotoImage(file="pieces/BlackQueen.svg.png").subsample(2,2)
        self.pieces["BlackKing"] = PhotoImage(file="pieces/BlackKing.svg.png").subsample(2,2)
        self.pieces["BlackPawn"] = PhotoImage(file="pieces/BlackPawn.svg.png").subsample(2,2)
        self.pieces["WhiteRook"] = PhotoImage(file="pieces/WhiteRook.svg.png").subsample(2,2)
        self.pieces["WhiteKnight"] = PhotoImage(file="pieces/WhiteKnight.svg.png").subsample(2,2)
        self.pieces["WhiteBishop"] = PhotoImage(file="pieces/WhiteBishop.svg.png").subsample(2,2)
        self.pieces["WhiteQueen"] = PhotoImage(file="pieces/WhiteQueen.svg.png").subsample(2,2)
        self.pieces["WhiteKing"] = PhotoImage(file="pieces/WhiteKing.svg.png").subsample(2,2)
        self.pieces["WhitePawn"] = PhotoImage(file="pieces/WhitePawn.svg.png").subsample(2,2)

        self.black=PhotoImage(file="black.png")
        self.white=PhotoImage(file="white.png")
        self.startgui()

    def startgui(self):
        self.boards = []

        for iii in range(2):
            self.boards.append({}) # dictionary that stores the top queue, bottom queue, and board
        
            self.boards[iii]["buttons"] = []
            self.boards[iii]["topQueue"] = []
            self.boards[iii]["bottomQueue"] = []
            for col in range(8): # initialized board
                self.boards[iii]["buttons"].append([])
                for row in range(8):
                    button = Button()
                    button.config(command=partial(self.report, col, row))
                    self.boards[iii]["buttons"][col].append(button)
                    self.boards[iii]["buttons"][col][row].grid(column=col+(8*iii+iii), row=row+4, sticky=W)
                    self.boards[iii]["buttons"][col][row].grid_configure(padx=0, pady=0)


            for element in range(16):
                button = Button()
                button.config(command=partial(self.reportQueue, element))
                button.config(image=self.white)
                self.boards[iii]["topQueue"].append(button)
                if element<8:
                    self.boards[iii]["topQueue"][element].grid(column=element+(8*iii+iii), row=0, sticky=W)
                else:
                    self.boards[iii]["topQueue"][element].grid(column=(element-8)+(8*iii+iii), row=1, sticky=W)
                self.boards[iii]["topQueue"][element].grid_configure(padx=0, pady=10)
                
            for element in range(16):
                button = Button()
                button.config(command=partial(self.reportQueue, element))
                button.config(image=self.white)
                self.boards[iii]["bottomQueue"].append(button)
                if element<8:
                    self.boards[iii]["bottomQueue"][element].grid(column=element+(8*iii+iii), row=15, sticky=W)
                else:
                    self.boards[iii]["bottomQueue"][element].grid(column=(element-8)+(8*iii+iii), row=16, sticky=W)
                self.boards[iii]["bottomQueue"][element].grid_configure(padx=0, pady=10)

                   
        self.bufferButtons = []
        for iii in range(17):
            self.bufferButtons.append(Button())
            self.bufferButtons[iii].grid(column=8,row=iii)
            self.bufferButtons[iii].grid_configure(padx=20,pady=10)

        #for child in mainframe.winfo_children(): child.grid_configure(padx=0, pady=0)
        self.updateButtons()
        root.mainloop()

    def updateButtons(self):
        '''changes all the button's images to reflect current state'''
        # receive data
        gameState = [ [ ["WhitePawn"]*16, [ [None,None,None,"BlackKing",None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,"BlackPawn",None,None],
                [None,None,"BlackQueen",None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,"WhitePawn",None],
                [None,None,None,"WhiteKing",None,None,None,None]
                ], ["BlackPawn"]  ], [ ["WhitePawn"], [ [None,None,None,"BlackKing",None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,"BlackPawn",None,None],
                [None,None,"BlackQueen",None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,"WhitePawn",None],
                [None,None,None,"WhiteKing",None,None,None,None]
                ], ["BlackPawn"]  ] ]

        for iii in range(2):
            for col in range(len(self.boards[iii]["buttons"])):
                for row in range(len(self.boards[iii]["buttons"][col])):
                    if gameState[iii][1][col][row] != None:
                        self.boards[iii]["buttons"][col][row].config(image=self.pieces[gameState[iii][1][col][row]])
                    elif (row % 2 == col % 2):
                        self.boards[iii]["buttons"][col][row].config(image=self.white)
                    else:
                        self.boards[iii]["buttons"][col][row].config(image=self.black)
            for elementIndex in range(len(self.boards[iii]["topQueue"])): # first zero out the topQueue
                self.boards[iii]["topQueue"][elementIndex].config(image=self.white)
            for elementIndex in range(len(gameState[iii][0])): # now fill
                self.boards[iii]["topQueue"][elementIndex].config(image=self.pieces[gameState[iii][0][elementIndex]])
            for elementIndex in range(len(self.boards[iii]["bottomQueue"])): # first zero out the bottomQueue
                self.boards[iii]["bottomQueue"][elementIndex].config(image=self.white)
            for elementIndex in range(len(gameState[iii][2])): # now fill
                self.boards[iii]["bottomQueue"][elementIndex].config(image=self.pieces[gameState[iii][2][elementIndex]])

        self.boards[0]["buttons"][2][4].config(image = random.choice(list(self.pieces.values())))
        root.after(1000, self.updateButtons) # "recusion"

    def report(self,col,row):
        print(str(col)+" "+str(row))
        self.transmitnumbers.append(col)
        self.transmitnumbers.append(row)
        if len(self.transmitnumbers) == 4:
            pass #  do the transmission
            self.transmitnumbers = [] # set back to zero.
        elif len(self.transmitnumbers) == 3:
            pass # do the transmission for queues
            self.transmitnumbers = []

    def reportQueue(self,element):
        self.transmitnumbers.append(elements)


def main():
    G = GUI("localhost",9999)
if __name__=="__main__":
    main()
#root.bind('<Return>', calculate)



