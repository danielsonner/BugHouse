from Piece import Piece

class Bishop(Piece):
  
  def validMove(self,startLoc,endLoc):
    if abs(self.getSlopeOfMove(startLoc,endLoc)) == 1:
      return True
    return False
    
  def getSlopeOfMove(self,startLoc,endLoc):
    return (endLoc[1]-startLoc[1])/(endLoc[0] - startLoc[0])
    
  def __str__(self):
    return 'B'