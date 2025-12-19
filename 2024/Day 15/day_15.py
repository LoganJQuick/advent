moves = {
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
        return True
      else:
        return False

def part_1(lines):
  starting_pos = [(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == '@']
  grid = get_grid(lines)
  print(get_moves(lines))


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines, 7, 11)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  # print(f"Part 1 with full data: {part_1(full_lines, 103, 101)}")
  # print(f"Part 2 with full data: {part_2(full_lines)}")

