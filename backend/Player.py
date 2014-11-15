class Player(object):
  """ A bughouse game player who has a color and pieces and screenname"""
  def __init__(self, name, color, playerNum,pieces=[]):
    self.name = name
    self.color = color
    self.playerNum = playerNum
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
    
  def __str__ (self):
    """ encoding player objecst as their list of pieces
     so it's easy to send to server"""
    return str(self.pieces)