from Piece import Piece

class King(Piece):
  def whereCanIMove(self,startLoc,endLoc):
    if abs(startLoc[0] - endLoc[0]) <= 1 or abs(startLoc[1] - endLoc[1]) <= 1:
      return True
    return False