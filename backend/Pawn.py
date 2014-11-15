from MovedPiece import MovedPiece

class Pawn(MovedPiece):
  
  def validMove(self,startLoc,endLoc):
    if abs(endLoc[0] - startLoc[0]) > 1:
      return False # moved too far to a side
    if self.color == self.WHITE:
      if start[0] - end[0] == 1:
        return True
      elif start[0] - end[0] == 2 and not self.moved:
        return True
    else:
      if start[0] - end[0] == -1:
        return True
      elif start[0] - end[0] == -2 and not self.moved:
        return True
    return False
    
  def __str__(self):
    return Piece.__str__(self).'Pawn'