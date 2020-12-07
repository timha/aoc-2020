### Day 4

""" Part 1 """
def validate_passports(passports):
    num_valid = 0
    for passport in passports:
        num_fields = passport.count(":")
        if (num_fields == 8) or (num_fields == 7 and "cid" not in passport):
            num_valid += 1
        # num_valid += num_fields == 8 or (num_fields == 7 and "cid" not in passport)
    return num_valid

passports = open("Day_4_input.txt", "r").read().split("\n\n")
print(validate_passports(passports))



""" Part 2 """
import re

def validate_passports(passports):
    num_valid = 0
    for passport in passports:
        num_fields = passport.count(":")
        if (num_fields == 8) or (num_fields == 7 and "cid" not in passport):
            num_valid += validate_fields(passport.split())
        # num_valid += num_fields == 8 or (num_fields == 7 and "cid" not in passport)
    return num_valid


def validate_fields(passport):
    # why no swith/case
    print(passport)
    for field in passport:
        field_name = field[:3]
        field_value = field[4:]
        
        # could do: for field .. in [list of fields]?
        # short-circuited
        if field_name == "byr" and (int(field_value) < 1920 or int(field_value) > 2002):
            return 0
        elif field_name == "iyr" and (int(field_value) < 2010 or int(field_value) > 2020):
            return 0
        elif field_name == "eyr" and (int(field_value) < 2020 or int(field_value) > 2030):
            return 0
        elif field_name == "hgt" and not re.search("^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$", field_value):
            return 0
        elif field_name == "hcl" and not re.search("^#[\da-f]{6}$", field_value):
            return 0
        elif field_name == "ecl" and not re.search("^(amb|blu|brn|gry|grn|hzl|oth){1}$", field_value):
            return 0
        elif field_name == "pid" and not re.search("^\d{9}$", field_value):
            return 0
    return 1
    
file_of_passports = open("Day_4_input.txt", "r").read().split("\n\n")
print(validate_passports(file_of_passports))