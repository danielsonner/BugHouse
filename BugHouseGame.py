class BugHouseGame(object):
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