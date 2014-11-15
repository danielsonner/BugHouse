from MovedPiece import MovedPiece

class King(MovedPiece):
  
  def validMove(self,startLoc,endLoc):
    if abs(startLoc[0] - endLoc[0]) <= 1 or abs(startLoc[1] - endLoc[1]) <= 1:
      return True
    return False
    
  def __str__(self):
    return Piece.__str__(self).'King'