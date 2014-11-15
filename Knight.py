from Piece import Piece

class Knight(Piece):
  
  def validMove(self,startLoc,endLoc):
    if (abs(startLoc[0] - endLoc[0]) == 1 and abs(startLoc[1] - endLoc[1]) == 2 or
        abs(startLoc[0] - endLoc[0]) == 2 and abs(startLoc[1] - endLoc[1]) == 1):
      return True
    return False
    
  def __str__(self):
    return Piece.__str__(self).'knight'