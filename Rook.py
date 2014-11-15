from MovedPiece import MovedPiece

class Rook(MovedPiece):
  def validMove(self,startLoc,endLoc):
    if startLoc[0] == endLoc[0] or startLoc[1] == endLoc[1]:
      return True
    return False
    
  def __str__(self):
    return Piece.__str__(self).'rook'