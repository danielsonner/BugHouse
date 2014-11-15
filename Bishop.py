from Piece import Piece

class Bishop(Piece):
  def whereCanIMove(self,startLoc,endLoc):
    if abs(((endLoc[1]-startLoc[1])/(endLoc[0] - startLoc[0]))) == 1:
      return True
    return False