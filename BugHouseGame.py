from MovedPiece import MovedPiece
from Pawn import Pawn

class BugHouseGame(object):
  """ A Bug House Game is the highest level object we have. 
  It contains 2 single game objects and should be called to
  make a move on a board since if a piece is captured it will
  update the other player's offboard pieces.  """
  def __init__ (self, singleGame1, singleGame2):
    self.game1 = singleGame1
    self.game2 = singleGame2
    
  def initializeNewGame(self):
    
    
  def move(self, startLoc, endLoc, game1=True):
    """Attempts to make move. 
       inputs: startLoc and endLoc are tuples with coordinates x,y
               A startLoc can be a piece if a piece is being dropped
       outputs: True if move made, else False"""
    try:
      if game1:
        gamePlaying = self.game1
        gameNotPlaying = self.game2
      else:
        gamePlaying = self.game2
        gameNotPlaying = self.game1
      capturedPiece = gamePlaying.makeAndValidateMove(startLoc,endLoc)
      if capturedPiece:
        # if it was a promoted pawn, make it back into a pawn
        if capturedPiece.promotedPawn:
          capturedPiece = Pawn()
        # captured pieces are counted as having moved already
        if isinstance(capturedPiece, MovedPiece):
          capturedPiece.move()
          capturedPiece.move()
        # give the captured piece to the the partner of the capturer
        gameNotPlaying.addPiece(capturedPiece)   
      # since no errors were thrown, we were able to make a move
      return True
    except AssertionError:
      return False