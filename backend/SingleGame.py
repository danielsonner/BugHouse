class SingleGame(object):
  """ Represents a board on which part of a game of bughouse
  is being played on."""
  def __init__(self, player1, player2, board, whoseTurn = True):
    self.player1 = player1
    self.player2 = player2
    self.board = board
    self.whoseTurn = whoseTurn
    
  def makeAndValidateMove(self, start, end):
    """
    inputs: start is a tuple x coord, y coord and end is tuple with end x, end y
    outputs: Piece captured if one is captured, else None if no piece captrued
    throws: AssertionError if the move is invalid.  Move will not be executed.
    """
    assert(self.board.occupantColor(start) == whoseTurn)
    pieceCaptured = self.board.move(start,end)
    return pieceCaptured
    
  def addPiece(self, piece):
    """ gives a piece to the appropriate player based on color"""
    if self.player1.getColor() == piece.getColor():
      self.player1.addPiece(piece)
    else:
      self.player2.addPiece(piece)    
      
  def newGame(self):
    self.board.setup()