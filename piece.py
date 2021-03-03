import pygame
import config

class Piece:
  isWhite = False

  def __init__(self, name, row, col):
    if (Piece.isWhite):
      self.name = name.upper()
    else:
      self.name = name.lower()
      
    self.row = row
    self.col = col
    
    self.hasMoved = False
    self.isWhite = Piece.isWhite
    #print(self.name)
    self.image = pygame.image.load(f"assets/img/{name.lower()}.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    
  def getPosition(self):
    return (self.row, self.col)
    
  def update(self):
    pass
    
  def draw(self):
    pass
    #config.screen.blit(self.image, ())
    
  #def move(self):
    #self.row = 

class King(Piece):
  def __init__(self, row, col):
    super().__init__("K", row, col)

  def getPossibleMoves(self):
    row = self.row
    col = self.col
    
    moves = []
    
    # Vertical
    moves.append((row + 1, col))
    moves.append((row - 1, col))
  
    # Horizontal
    moves.append((row, col + 1))
    moves.append((row, col - 1))
    
    # Diagonal
    moves.append((row + 1, col + 1))
    moves.append((row + 1, col - 1))
    moves.append((row - 1, col + 1))
    moves.append((row - 1, col - 1))
    
    return moves

class Queen(Piece):
  def __init__(self, row, col):
    super().__init__("Q", row, col)
    
class Rook(Piece):
  def __init__(self, row, col):
    super().__init__("R", row, col)

class Bishop(Piece):
  def __init__(self, row, col):
    super().__init__("B", row, col)

class Knight(Piece):
  def __init__(self, row, col):
    super().__init__("N", row, col)
      
  def getPossibleMoves(self):
    row = self.row
    col = self.col
  
    moves = []
  
    # Up
    moves.append((row - 2, col - 1))
    moves.append((row - 2, col + 1))
    
    # Down
    moves.append((row + 2, col - 1))
    moves.append((row + 2, col + 1))
    
    # Left
    moves.append((row - 1, col - 2))
    moves.append((row - 1, col + 2))
    
    # Right
    moves.append((row + 1, col - 2))
    moves.append((row + 1, col + 2))

    return moves
  
class Pawn(Piece):
  def __init__(self, row, col):
    super().__init__("P", row, col)
    
    # -1 for white, 1 for black
    if (self.isWhite):
      self.direction = -1
    else:
      self.direction = 1
    
  def getPossibleMoves(self):    
    moves = []
    
    # Change options depending on it having moved or not
    if (self.hasMoved):
      moves.append((self.row + self.direction, self.col))
    else:
      moves.append((self.row + (self.direction * 2), self.col))
      moves.append((self.row + self.direction, self.col))
    
    return moves
    
