### Day 3

""" Part 1 """
# grid = open("Day3Input.txt", "r").read().splitlines()
# slope = (3,1)
# x_pos = 0
# trees_counted = 0
# for line in grid[::slope[1]]:
#     if line[x_pos] == "#":
#         trees_counted += 1
#     x_pos = (x_pos + slope[0]) % len(line.strip())
# print(trees_counted)


""" Part 1 and Part 2 """
def le_solve_it(grid_file, slopes):
    grid = open(grid_file, "r").read().splitlines()
    return calc_product_of_treez_counted(grid, slopes)
    

def count_treez_encountered(grid, delta_x, delta_y):
    x_pos = trees_counted = 0
    for line in grid[::delta_y]:
        if line[x_pos] == "#": trees_counted += 1 
        x_pos = (x_pos + delta_x) % len(line)
    return trees_counted


def calc_product_of_treez_counted(grid, slopes):
    product = 1
    for slope in slopes: product *= count_treez_encountered(grid, slope[0], slope[1])
    return product


grid_file = "day_3_input.txt"
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print(le_solve_it(grid_file, [(3,1)]))
print(le_solve_it(grid_file, slopes))