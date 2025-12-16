def get_rules(lines):
  i = 0
  rules = {}
  while lines[i] != "":
    first, second = [int(n) for n in lines[i].split('|')]
    rules[second] = rules.get(second, set()).union({first})
    i += 1
  return rules

def get_books(lines):
  i = 0
  while lines[i] != "":
    i += 1
  i += 1
  pages = []
  while i < len(lines):
    pages.append([int(n) for n in lines[i].split(',')])
    i += 1
  return pages

def valid_book(book, rules):
  so_far = set()
  valid = True
  for page in book[::-1]:
    if len(rules.get(page, set()).intersection(so_far)) > 0:
      valid = False
      break
    so_far.add(page)
  return valid
  
def part_1(lines):
  rules = get_rules(lines)
  books = get_books(lines)
  total = 0
  for book in books:
    valid = valid_book(book, rules)
    if valid:
      total += book[len(book) // 2]
  return total

def swap(list, pos_1, pos_2):
  first = list[pos_1]
  list[pos_1] = list[pos_2]
  list[pos_2] = first
  return list

def reorder_book(book, rules):
  while not valid_book(book, rules):
    so_far = set()
    for i, page in enumerate(book[::-1]):
      if len(rules.get(page, set()).intersection(so_far)) > 0:
        switch_idx = max([book.index(page) for page in rules.get(page, set()).intersection(so_far)])
        curr_idx = len(book)-i-1
        book = swap(book, switch_idx, curr_idx)
      so_far.add(page)
  return book
      

def part_2(lines):
  rules = get_rules(lines)
  books = get_books(lines)
  total = 0
  for book in books:
    valid = valid_book(book, rules)
    if not valid:
      total += reorder_book(book, rules)[len(book) // 2]
  return total

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")