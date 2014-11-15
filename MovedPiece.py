from Piece import Piece

class MovedPiece(Piece):
  """ Abstract class. This is a piece that keeps track of whether it 
  has moved (keeps track up to 2 moves)"""
  
  def __init__(self,color, moved=False, movedTwice=False, promotedPawn=False):
    """ color is 0 for white and 1 black"""
    self.color = color
    self.moved = moved
    self.movedTwice = movedTwice
    self.promotedPawn = promotedPawn
  
  def __eq__(self, other):
    oldEq = Piece.__eq__(self, other)
    if oldEq and self.moved == other.moved:
      return True
    return False
  
  def move(self):
    if (self.moved == False):
      self.moved = True
    else:
      self.movedTwice = True
      
  def movedOnce(self):
    return self.moved
  
  def movedTwice(self):
    return self.movedTwice