class BugHouseGame(object):
  """ A Bug House Game is the highest level object we have. 
  It contains 2 single game objects and should be called to
  make a move on a board since if a piece is captured it will
  update the other player's offboard pieces.  """
  def __init__ (self, singleGame1, singleGame2):
    self.game1 = singleGame1
    self.game2 = singleGame2
    
  def move(self, startLoc, endLoc, game1=True):
    """Tries to make move. If move is made returns true, else false."""
    try:
      if game1:
        gamePlaying = self.game1
        gameNotPlaying = self.game2
      else:
        gamePlaying = self.game2
        gameNotPlaying = self.game1
      capturedPiece = gamePlaying.makeAndValidateMove(startLoc,endLoc)
      if capturedPiece:
        gameNotPlaying.addPiece(capturedPiece)   
      return True
    except AssertionError:
      return False