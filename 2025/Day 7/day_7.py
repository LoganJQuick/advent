def num_splits(lines):
  curr_rays = set([n for n in range(len(lines[0])) if lines[0][n] == 'S'])
  splits = 0
  for line in lines[1:]:
    new_rays = set()
    for ray in curr_rays:
      if line[ray] == '^':
        splits += 1
        new_rays = new_rays.union([ray+1, ray-1])
      else:
        new_rays.add(ray)
    curr_rays = new_rays
  return splits

def num_rays(lines):
  curr_rays = [n for n in range(len(lines[0])) if lines[0][n] == 'S']
  curr_rays = {curr_rays[0]: 1}
  for line in lines[1:]:
    new_rays = {}
    for ray in curr_rays:
      ways = curr_rays[ray]
      if line[ray] == '^':
        new_rays[ray-1] = new_rays.get(ray-1, 0) + ways
        new_rays[ray+1] = new_rays.get(ray+1, 0) + ways
      else:
        new_rays[ray] = new_rays.get(ray, 0) + ways
    curr_rays = new_rays
  return sum([curr_rays[n] for n in curr_rays])




if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {num_splits(test_lines)}")
  print(f"Part 2 with test data: {num_rays(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {num_splits(full_lines)}")
  print(f"Part 2 with full data: {num_rays(full_lines)}")