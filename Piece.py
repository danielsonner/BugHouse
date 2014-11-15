from abc import ABCMeta, abstractmethod

class Piece(object):
  """Represents a piece"""
  
  __metaclass__ = ABCMeta
  
  def __init__(self,color):
    """ color is True for white and False for black"""
    self.color = color

  @abstractmethod
  def validMove(self, startLoc, endLoc):
    raise NotImplementedError("implement valid move")
    
  def getColor(self):
    return self.color