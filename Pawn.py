from Piece import Piece

class Pawn(Piece):
  
  def __init__(self,color, moved=False):
    """ color is 0 for white and 1 black"""
    self.color = color
    self.moved = moved
  
  def whereCanIMove(self,startLoc,endLoc):
    if abs(endLoc[0] - startLoc[0]) > 1:
      return False # moved too far to a side
    if self.color:
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