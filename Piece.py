from abc import ABCMeta, abstractmethod

class Piece(object):
  """Represents a piece"""
  
  __metaclass__ = ABCMeta
  
  def __init__(self,color):
    """ color is True for white and False for black"""
    self.color = color
    
  def __eq__(self, other):
      if self.color == other.color and type(self) == type(other):
          return True
      else:
          return False

  @abstractmethod
  def validMove(self, startLoc, endLoc):
    raise NotImplementedError("implement valid move")
    
  def getColor(self):
    return self.color