with open('input.txt', 'r') as file:
    lines = file.read().split("\n")


def get_neighbours(input_cube):
    x,y,z = input_cube
    return [(x-1, y, z), (x+1, y, z), (x,y-1,z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
cubes = set()

for line in lines:
    cube = tuple([int(coordinate) for coordinate in line.split(",")])
    cubes.add(cube)

print(cubes)

open_sides = 0

for cube in cubes:
    open_sides += sum([neighbour not in cubes for neighbour in get_neighbours(cube)])

print(open_sides)