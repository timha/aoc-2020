### Day 5


""" Part 1 """

def find_highest_seat_id(boarding_passes):
    highest_id = 0
    for boarding_pass_code in boarding_passes:
        highest_id = max(highest_id, calc_seat_id(boarding_pass_code))
    return highest_id

def calc_seat_id(code):
    return calc_position(code[0:7]) * 8 + calc_position(code[7:])

def calc_position(code):
    if code == "": 
        return 0

    adder = 0
    if code[0] in ("B", "R"):
        adder += pow(2, len(code) - 1)
    return adder + calc_position(code[1:])
    # return (code[0] in ("B", "R")) * (pow(2, len(code) - 1)) + calc_position(code[1:])

boarding_passes = open("Day_5_input.txt", "r").read().splitlines()
print(find_highest_seat_id(boarding_passes))


""" Part 2 """

def find_yo_seat(boarding_passes):
    seats = calc_seat_ids(boarding_passes)
    return find_missing_seat(sorted(seats))

def calc_seat_ids(boarding_passes):
    seats = []
    for code in boarding_passes:
        seat_id = calc_position(code[0:7]) * 8 + calc_position(code[7:])
        seats.append(seat_id)
    return seats

def calc_position(code):
    if code == "": 
        return 0
    adder = 0
    if code[0] in ("B", "R"):
        adder += pow(2, len(code) - 1)
    return adder + calc_position(code[1:])
    
def find_missing_seat(seats):
    for i in range(1, len(seats)):
        if seats[i] - seats[i - 1] == 2:
            return seats[i] - 1
    return -1

boarding_passes = open("Day_5_input.txt", "r").read().splitlines()
print(find_yo_seat(boarding_passes))
