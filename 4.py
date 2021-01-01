
def parse_input():
  with open('4.txt') as f:
    text = f.read()
  passport_dicts = []
  next_passport_dict = {}
  for line in text.splitlines():
    if not line:
      passport_dicts.append(next_passport_dict)
      next_passport_dict = {}
    else:
      key_vals = [x.split(':') for x in line.split()]
      for k, v in key_vals:
        next_passport_dict[k] = v
  if next_passport_dict:
    passport_dicts.append(next_passport_dict)
  return passport_dicts

def main():
  valid_count = 0
  passport_dicts = parse_input()
  for passport_dict in passport_dicts:
    if len(passport_dict.keys() - {'cid'}) == 7:
      valid_count += 1
  print('valid_count:', valid_count)

main()