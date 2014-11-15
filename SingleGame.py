class SingleGame(object):
  def __init__(self, player1, player2, board, whoseTurn = True):
    self.player1 = player1
    self.player2 = player2
    self.board = board
    self.whoseTurn = whoseTurn
    
  def makeAndValidateMove(self, start, end):
    """
    inputs: start is a tuple x coord, y coord and end is tuple with end x, end y
    outputs: True if move is valid, else False
    """
    if self.board.occupantColor(start) != whoseTurn:
      return False
    else:
      # in some cases board throws assertion error if move is invalid
      try: 
        return self.board.move(start,end)
      except AssertionError:
        return False