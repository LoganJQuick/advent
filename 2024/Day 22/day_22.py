def next_secret(n):
  n = ((n * 64) ^ n) % 16777216
  n = ((n // 32) ^ n) % 16777216
  return ((n * 2048) ^ n) % 16777216

def secret_n_steps(num, steps):
  for _ in range(steps):
    num = next_secret(num)
  return num

def n_prices(num, n):
  prices = []
  for _ in range(n):
    prices.append(num % 10)
    num = next_secret(num)
  return prices

def part_1(lines):
  return sum([secret_n_steps(int(line), 2000) for line in lines])

def part_2(lines):
  algo_values = {}
  for line in lines:
    algos = {}
    prev = int(line) % 10
    sequence = []
    for price in n_prices(int(line), 2001)[1:]:
      sequence.append(price - prev)
      if len(sequence) == 5:
        sequence.pop(0)
      if len(sequence) == 4:        
        t = tuple(sequence)
        algos[t] = algos.get(t, price)
      prev = price
    for algo in algos:
      algo_values[algo] = algo_values.get(algo, 0) + algos[algo]
  return max([(algo_values[algo], algo) for algo in algo_values])
      
      


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")