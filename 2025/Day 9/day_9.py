def get_points(lines):
  return [(int(a),int(b)) for a,b in [line.split(',') for line in lines]]

def largest_rectangle(lines):
  points = get_points(lines)
  largest = 0
  for i, point_a in enumerate(points):
    for point_b in points[i+1:]:
      largest = max(largest, area(point_a, point_b))
  return largest

def area(point_a, point_b):
  return (abs(point_a[0] - point_b[0]) + 1) * (abs(point_a[1] - point_b[1]) + 1)

def largest_rectangle_two(lines):
  points = get_points(lines)
  largest = 0
  for i, point_a in enumerate(points):
    for point_b in points[i+1:]:
      curr_area = area(point_a, point_b)
      if curr_area > largest and valid_rect(points, point_a, point_b):
        largest = area(point_a, point_b)
  return largest

def valid_rect(points, point_a, point_b):
  a1, a2 = min(point_a[0], point_b[0]), min(point_a[1], point_b[1])
  b1, b2 = max(point_a[0], point_b[0]), max(point_a[1], point_b[1])
  for i in range(len(points)):
    next_i = (i + 1) % len(points)
    if points[i][0] == points[next_i][0]:
      top, bottom = max(points[i][1], points[next_i][1]), min(points[i][1], points[next_i][1])
      if a1 < points[i][0] < b1 and (top > a2 and bottom < b2):
        return False
    else:
      right, left = max(points[i][0], points[next_i][0]), min(points[i][0], points[next_i][0])
      if a2 < points[i][1] < b2 and (right > a1 and left < b1):
        return False
  return True

        
if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {largest_rectangle(test_lines)}")
  print(f"Part 2 with test data: {largest_rectangle_two(test_lines)}")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {largest_rectangle(full_lines)}")
  print(f"Part 2 with full data: {largest_rectangle_two(full_lines)}")
