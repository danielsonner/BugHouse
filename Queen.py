from Piece import Piece

class Queen(Piece):
  def validMove(self,startLoc,endLoc):
    if (startLoc[0] == endLoc[0] or startLoc[1] == endLoc[1]
        or abs(((endLoc[1]-startLoc[1])/(endLoc[0] - startLoc[0]))) == 1):
      return True
    return False
    
  def moveLikeRook(self, startLoc, endLoc):
    """ Returns True if the piece can move like a rook from start
        to end location (False is moving like bishop)"""
    if startLoc[0] == endLoc[0] or startLoc[1] == endLoc[1]:
      return True
    return False
    
  def __str__(self):
    return Piece.__str__(self).'Queen'