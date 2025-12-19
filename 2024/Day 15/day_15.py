move_mapping = {
  '^': (-1, 0),
  '<': (0, -1),
  'v': (1, 0),
  '>': (0, 1),
}

def get_grid(lines):
  grid = []
  i = 0
  while lines[i] != '':
    grid.append(list(lines[i]))
    i += 1
  return grid

def get_moves(lines):
  moves = ""
  i = 0
  while lines[i] != '':
    i += 1
  i += 1
  for j in range(i, len(lines)):
    moves += lines[j]
  return moves

def make_move(lines, pos, dir):
  x, y = pos
  i, j = dir
  match lines[x][y]:
    case '#':
      return False
    case '.':
      return True
    case char:
      if make_move(lines, (x+i,y+j), dir):
        lines[x][y] = '.'
        lines[x+i][y+j] = char
        return (x+i, y+j)
      else:
        return False

def part_1(lines):
  grid = get_grid(lines)
  x, y = [(i, j) for i in range(len(grid)) for j in range(len(lines[0])) if grid[i][j] == '@'][0]
  moves = [move_mapping[move] for move in get_moves(lines)]
  for move in moves:
    new_pos = make_move(grid, (x,y), move)
    if new_pos:
      x, y = new_pos
  return sum([100*i + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'O'])

def get_grid_two(lines):
  original = get_grid(lines)
  new_grid = []
  for i in range(len(original)):
    line = []
    for j in range(len(original[0])):
      match original[i][j]:
        case '#':
          line += ['#', '#']
        case 'O':
          line += ['[', ']']
        case '.':
          line += ['.', '.']
        case '@':
          line += ['@', '.']
    new_grid.append(line)
  return new_grid

def move_possible(grid, pos, dir):
  x, y = pos
  match grid[x][y], dir:
    case '.', _:
      return True
    case '#', _:
      return False
    case '[', (0, j):
      return move_possible(grid, (x, y+j), dir)
    case '[', (i, 0):
      return move_possible(grid, (x+i, y), dir) and move_possible(grid, (x+i, y+1), dir)
    case ']', (0, j):
      return move_possible(grid, (x, y+j), dir)
    case ']', (i, 0):
      return move_possible(grid, (x+i, y), dir) and move_possible(grid, (x+i, y-1), dir)
    case '@', (i, j):
      return move_possible(grid, (x+i, y+j), dir)

def make_move_two(grid, pos, dir):
  x, y = pos
  match grid[x][y], dir:
    case '[', (i, 0):
      make_move_two(grid, (x+i, y), dir)
      make_move_two(grid, (x+i, y+1), dir)
      grid[x][y] = '.'
      grid[x][y+1] = '.'
      grid[x+i][y] = '['
      grid[x+i][y+1] = ']'
    case '[', (0, 1):
      make_move_two(grid, (x, y+2), dir)
      grid[x][y] = '.'
      grid[x][y+1] = '['
      grid[x][y+2] = ']'
    case '[', (0, -1):
      make_move_two(grid, (x, y-1), dir)
      grid[x][y+1] = '.'
      grid[x][y-1] = '['
      grid[x][y] = ']'
    case ']', (i, 0):
      make_move_two(grid, (x+i, y), dir)
      make_move_two(grid, (x+i, y-1), dir)
      grid[x][y] = '.'
      grid[x][y-1] = '.'
      grid[x+i][y] = ']'
      grid[x+i][y-1] = '['
    case ']', (0, 1):
      make_move_two(grid, (x, y+1), dir)
      grid[x][y-1] = '.'
      grid[x][y] = '['
      grid[x][y+1] = ']'
    case ']', (0, -1):
      make_move_two(grid, (x, y-2), dir)
      grid[x][y] = '.'
      grid[x][y-2] = '['
      grid[x][y-1] = ']'
    case '@', (i, j):
      make_move_two(grid, (x+i, y+j), dir)
      grid[x][y] = '.'
      grid[x+i][y+j] = '@'


def part_2(lines):
  grid = get_grid_two(lines)
  x, y = [(i, j) for i in range(len(grid)) for j in range(len(lines[0])) if grid[i][j] == '@'][0]
  moves = [move_mapping[move] for move in get_moves(lines)]
  for move in moves:
    if move_possible(grid, (x, y), move):
      make_move_two(grid, (x,y), move)
      x, y = x + move[0], y + move[1]    
  return sum([100*i + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '['])
    

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")

