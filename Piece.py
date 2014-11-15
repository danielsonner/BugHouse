from abc import ABCMeta, abstractmethod

class Piece(object):
  """Abstract class that represents a piece that has a color and the 
     ability to check if its move is valid"""
  WHITE = True
  BLACK = False
  
  __metaclass__ = ABCMeta
  
  def __init__(self,color,promotedPawn=False):
    """ color is True for white and False for black.  
        promotedPawn if the piece was a pawn but has now been promoted"""
    self.color = color
    self.promotedPawn = promotedPawn
    
  def __eq__(self, other):
      if self.color == other.color and type(self) == type(other):
          return True
      else:
          return False

  @abstractmethod
  def validMove(self, startLoc, endLoc):
    """ Returns whether the piece's move is a valid shape.  Does not
    take into account things such as pieces in the way but just looks
    at the general shape of the movement."""
    raise NotImplementedError("implement valid move")
    
  def getColor(self):
    return self.color