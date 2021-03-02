class Piece:
  def __init__(self, color, row, col):
    self.color = color
    self.row = row
    self.col = col
    
    self.has_moved = False
    
  def getPosition(self):
    return (self.row, self.col)
    
  def sanitizeMoves(self, moves):
    i = 0
    while (i < len(moves)):
      if (moves[i][0] < 0 or moves[i][0] > 7):
        moves.pop(i)
      elif (moves[i][1] < 0 or moves[i][1] > 7):
        moves.pop(i)
      #elif (not isPositionFree(moves[i])):
        #moves.pop(i)
      else:
        i += 1
        
    return moves
    
  #def move(self):
    #self.row = 
  
class Pawn(Piece):
  def __init__(self, color, row, col):
    super().__init__(color, row, col)
    
    # -1 for white, 1 for black
    self.direction = int(color == "black") - int(color == "white")
    
  def getPossibleMoves(self):    
    moves = []
    
    if (self.has_moved):
      moves.append((self.row + self.direction, self.col))
    else:
      moves.append((self.row + (self.direction * 2), self.col))
      moves.append((self.row + self.direction, self.col))
      
    moves = self.sanitizeMoves(moves)
    print(moves)
  
