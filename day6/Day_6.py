### Day 6

""" Part 1 """
from functools import reduce

def sum_all_unique_answers(all_answers):
    return reduce(lambda x, y: x + y, map(lambda group_answer: count_unique_answers("".join(group_answer)), all_answers))

def count_unique_answers(group_answers):
    unique_answers = set()
    for answer in group_answers:
        unique_answers.add(answer)
    return len(unique_answers)


# list of list. each element in inner list (group) is an individual's answer
all_answers = [list(group_ans.split()) for group_ans in open("Day_6_input.txt", "r").read().split("\n\n")]
print(sum_all_unique_answers(all_answers))




""" Part 2 """
from functools import reduce

def sum_all_common_answers(all_answers):
    return reduce(lambda x, y: x + y, map(lambda group_answer: count_common_answers(group_answer), all_answers))

def count_common_answers(group_answers):
    common_answers = reduce(lambda x, y: x.intersection(y) , [set(answer) for answer in group_answers])
    return len(common_answers)


all_answers = [list(group_ans.split()) for group_ans in open("Day_6_input.txt", "r").read().split("\n\n")]
print(sum_all_common_answers(all_answers))
