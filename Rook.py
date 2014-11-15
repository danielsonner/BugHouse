from Piece import Piece

class Rook(Piece):
  def whereCanIMove(self,startLoc,endLoc):
    if startLoc[0] == endLoc[0] or startLoc[1] == endLoc[1]:
      return True
    return False