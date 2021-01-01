import re


def is_valid(passport_dict):
  '''
  byr (Birth Year) - four digits; at least 1920 and at most 2002.
  iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  hgt (Height) - a number followed by either cm or in:
  If cm, the number must be at least 150 and at most 193.
  If in, the number must be at least 59 and at most 76.
  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  pid (Passport ID) - a nine-digit number, including leading zeroes.
  cid (Country ID) - ignored, missing or not.
  '''

  valid_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
  if len((passport_dict.keys() & valid_keys) - {'cid'}) != 7:
    return False

  byr = int(passport_dict['byr'])
  if byr < 1920 or byr > 2002:
    return False
  iyr = int(passport_dict['iyr'])
  if iyr < 2010 or iyr > 2020:
    return False
  eyr = int(passport_dict['eyr'])
  if eyr < 2020 or eyr > 2030:
    return False
  match = re.match('([0-9]+)(cm|in)$', passport_dict['hgt'])
  if not match:
    return False
  val = int(match.group(1))
  unit = match.group(2)
  if unit == 'cm':
    if val < 150 or val > 193:
      return False
  else:
    if val < 59 or val > 76:
      return False
  if not re.match('#[0-9a-f]{6}$', passport_dict['hcl']):
    return False
  if passport_dict['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
    return False
  if not re.match('[0-9]{9}$', passport_dict['pid']):
    return False
  return True

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
    if is_valid(passport_dict):
      print('valid:', passport_dict)
      valid_count += 1
  print('valid_count:', valid_count)

main()
