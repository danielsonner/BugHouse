class Player(object):
  def __init__(self, name, color, pieces=[]):
    self.name = name
    self.color = color
    self.pieces = pieces
    
  def getColor(self):
    return self.color
    
  def getPieces(self):
    return self.pieces[:]
    
  def addPiece(self, piece):
    self.pieces.append(piece)
    
  def removePiece(self,piece):
    """ Returns true if piece is removed, else false"""
    try:
      self.pieces.remove(piece)
      return True
    except ValueError:
      return False
    
