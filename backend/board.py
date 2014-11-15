class Board(object):
    """This class represents a chess board"""
    board = [[None]*8]*8

    def __init__(self):
      self.setup()

    def  setup(self):
        """Sets up a board for the beginning of a game"""
        whitePawnOne = Pawn(True) #initialize pieces
        whitePawnTwo = Pawn(True)
        whitePawnThree = Pawn(True)
        whitePawnFour = Pawn(True)
        whitePawnFive = Pawn(True)
        whitePawnSix = Pawn(True)
        whitePawnSeven = Pawn(True)
        whitePawnEight = Pawn(True)
        whiteQueenRook = Rook(True)
        whiteQueenKnight = Knight(True)
        whiteQueenBishop = Bishop(True)
        whiteQueen = Queen(True)
        whiteKing = King(True)
        whiteKingBishop = Bishop(True)
        whiteKingKnight = Knight(True)
        whiteKingRook = Rook(True)
        blackPawnOne = Pawn(False)
        blackPawnTwo = Pawn(False)
        blackPawnThree = Pawn(False)
        blackPawnFour = Pawn(False)
        blackPawnFive = Pawn(False)
        blackPawnSix = Pawn(False)
        blackPawnSeven = Pawn(False)
        blackPawnEight = Pawn(False)
        blackQueenRook = Rook(False)
        blackQueenKnight = Knight(False)
        blackQueenBishop = Bishop(False)
        blackQueen = Queen(False)
        blackKing = King(False)
        blackKingBishop = Bishop(False)
        blackKingKnight = Knight(False)
        blackKingRook = Rook(False)

        #set up pieces on board
        self.board[0][0] = blackQueenRook
        self.board[1][0] = blackQueenKnight
        self.board[2][0] = blackQueenBishop
        self.board[3][0] = blackQueen
        self.board[4][0] = blackKing
        self.board[5][0] = blackKingBishop
        self.board[6][0] = blackKingKnight
        self.board[7][0] = blackKingRook
        self.board[0][1] = blackPawnOne
        self.board[1][1] = blackPawnTwo
        self.board[2][1] = blackPawnThree
        self.board[3][1] = blackPawnFour
        self.board[4][1] = blackPawnFive
        self.board[5][1] = blackPawnSix
        self.board[6][1] = blackPawnSeven
        self.board[7][1] = blackPawnEight
        self.board[0][6] = whitePawnOne
        self.board[1][6] = whitePawnTwo
        self.board[2][6] = whitePawnThree
        self.board[3][6] = whitePawnFour
        self.board[4][6] = whitePawnFive
        self.board[5][6] = whitePawnSix
        self.board[6][6] = whitePawnSeven
        self.board[7][6] = whitePawnEight
        self.board[0][7] = whiteQueenRook
        self.board[1][7] = whiteQueenKnight
        self.board[2][7] = whiteQueenBishop
        self.board[3][7] = whiteQueen
        self.board[4][7] = whiteKing
        self.board[5][7] = whiteKingBishop
        self.board[6][7] = whiteKingKnight
        self.board[7][7] = whiteKingRook
    

    def isValidMove(self, start, end):
        """Checks if the piece at "start" can move to "end" legally, or checks whether off-board piece "start"
        can be dropped on end"""
        valid = True
        if isinstance(start, Piece): #handles drops
            if not self.isSquareEmpty(end):
                valid = False
            if start.getColor() == False and end[1] == 7:
                valid = False
            if start.getColor() == True and end[1] == 0:
                valid = False
        
        else: #handles standard moves
            if not (self.isSquareEmpty(end) or not (not self.isSquareEmpty(end) and (self.occupantColor(end) == self.occupantColor(start)))):
                valid = False
            piece = self.board[start[0]][start[1]]
            if not piece.validMove(start, end):
                valid = False
            #check if piece tried to move through another piece
            if isinstance(piece, Rook):
                if not self.rookPathClear(start, end):
                    valid = False
            
            if isinstance(piece, Bishop):
                if not self.bishopPathClear(start, end):
                    valid = False

            if isinstance(piece, Queen):
                if piece.moveLikeRook(start, end):
                    if not self.rookPathClear(start, end):
                        valid = False
                else:
                    if not self.bishopPathClear(start, end):
                        valid = False
            if isinstance(piece, Pawn): #checks special pawn cases
                if start[0] == end[0]:
                    if not self.isSquareEmpty(start, end):
                        valid = False
                elif piece.movedTwice():
                    if not (not self.isSquareEmpty((end[0], end[1]-1))) and self.occupantType(end[0], end[1]-1) == Pawn:
                        valid = False
                else:
                    if not (not self.isSquareEmpty(end)) and (self.occupantColor(end) == self.occupantColor(start)):
                        valid = False
            if isinstance(piece, King): #checks if King is moving into check
                if piece.getColor() == Piece.WHITE:
                    if end[0]-start[0] == 2: 
                        if not whiteKingRook.movedOnce() and self.isValidMove(start, (end[0]-1, end[1])):
                            valid = False
                    elif start[0] - end[0] == 2:
                        if not whiteQueenRook.movedOnce() and self.isValidMove(start (end[0]+1, end[1])):
                            valid = False
                if piece.getColor() == Piece.BLACK:
                     if end[0]-start[0] == 2: 
                        if not blackKingRook.movedOnce() and self.isValidMove(start, (end[0]-1, end[1])):
                            valid = False
                     elif start[0] - end[0] == 2:
                        if not blackQueenRook.movedOnce() and self.isValidMove(start (end[0]+1, end[1])):
                            valid = False
                if self.threatened(end):
                        valid = False

        return valid

    def move(self, start, end):
        """Moves a piece to a new location on the board. Throws an assertion error if move is invalid.
        Returns captured piece, or None if no piece is captured"""
        assert self.isValidMove(start, end)
        if isinstance(start, Piece): #handles drops
            self.board[end[0]][end[1]] = start
            returnValue = None
        else:                       #handles standard moves
            returnValue = self.board[end[0]][end[1]]
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = None
            if isinstance(self.board[end[0]][end[1]], Pawn):
                if self.occupantColor(end) == True and end[1] == 0:
                    self.board[end[0]][end[1]] = Queen(True, promotedPawn = True)
                if self.occupantColor(end) == False and end[1] == 7:
                    self.board[end[0]][end[1]] = Queen(False, promotedPawn = True)
        assert not self.threatened(self.findKing())
        return returnValue

    
              
    

    def rookPathClear(self, start, end):
        """Checks if a rook-style move has a clear passage from start to end"""
        legal = True
        if not (start[0]-end[0] == 0):
            for i in range(start[0]+1, end[0]):
                if not self.isSquareEmpty(i, start[1]):
                    legal = False
        else:
            for i in range(start[1]+1, end[1]):
                if not self.isSquareEmpty(start[0], i):
                    legal = False
        return legal

    def bishopPathClear(self, start, end):
        """Checks if a bishop-style move has a clear passage from start to end"""
        legal = True
        if Bishop.getSlopeOfMove(start, end) == 1:
            for i in range(min(start[0], end[0])+1, max(start[0], end[0])):
                if not self.isSquareEmpty(i, i):
                    legal = False
        else:
            for i in range(min(start[0], end[0])+1, max(start[0], end[0])):
                if not self.isSquareEmpty(i, max(start[1], end[1])-(i-min(start[0], end[0]))): #(x, y0-(x-x0))
                    legal = False
        return legal

    def threatened(self, coord):
        """Determines whether a piece at coord is threatened by an enemy piece"""
        threatened = False
        storage = self.occupant(coord)
        self.board[coord[0]][coord[1]] = None #removes any potential piece at coord, so it does not erroneously affect whether the square is threatened
        allPieceLocations = self.pieceLocations()
        enemyLocations = filter (lambda x: not self.occupantColor(x) == piece.getColor(), allPieces)
        for loc in enemyLocations:
            if self.validMove(loc, coord):
                threatened = True
        self.board[coord[0]][coord[1]] = storage #restores coord its value
        return threatened

    def findThreats(self, coord):
        """Returns the location of the piece threatening a coord"""
        threatLocations = []
        storage = self.occupant(coord)
        self.board[coord[0]][coord[1]] = None #removes any potential piece at coord, so it does not erroneously affect whether the square is threatened
        allPieceLocations = self.pieceLocations()
        enemyLocations = filter (lambda x: not self.occupantColor(x) == piece.getColor(), allPieces)
        for loc in enemyLocations:
            if self.validMove(loc, coord):
                threatLocations.append(loc)
        self.board[coord[0]][coord[1]] = storage #restores coord its value
        return threatLocations

    def findKing(self, color):
        locations = self.pieceLocations()
        throne = None
        for loc in locations:
            if isinstance(self.occupant(loc), King) and self.occupantColor(loc) == color:
                throne = loc
        return throne

    def isSquareEmpty(self, coord):
        """checks if a square is empty"""
        empty = False
        if self.board[coord[0]][coord[1]] == None:
            empty = True
        return empty

    def pieceLocations(self):
        """Returns a list of all pieces in board"""
        locList = []
        for i in range(len(board)):
            for j in range (len(board[i])):
                if not self.isSquareEmpty((i, j)):
                    locList.append((i, j))
        return locList

    def occupant(self, coord):
        """Returns the value stored at coord"""
        return self.board[coord[0]][coord[1]]

    def occupantType(self, coo1rd):
        """Returns the the type of the piece at coord"""
        return type(self.board[coord[0]][coord[1]])

    def occupantColor(self, coord):
        """returns the color of a square's occupant"""
        return self.board[coord[0]][coord[1]].getColor()
    
    def __str__(self):
        """toString"""
        printStr = str(board)
            
