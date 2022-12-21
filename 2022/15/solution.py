import re

from tqdm import tqdm


def beacons_available(x, y):
    for sensor_ in sensors:
        new_distance = get_manhattan_distance((x, y), sensor_)
        if new_distance <= sensors[sensor_]['distance'] and (x, y) not in beacons:
            return False
    return True


def get_manhattan_distance(p: tuple, q: tuple):
    """
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of absolute difference between coordinates
    distance = 0
    for p_i, q_i in zip(p, q):
        distance += abs(int(p_i) - int(q_i))

    return distance


with open('input.txt', 'r') as file:
    lines = file.read().split("\n")

sensors = {}
beacons = []
min_columns = 0
max_columns = 0
for line in lines:
    sensor_text, beacon_text = line.split(":")
    sensor_coordinates = tuple(re.findall(r"-?\d+", sensor_text))
    beacon_coordinates = tuple(re.findall(r"-?\d+", beacon_text))
    manhattan_distance = get_manhattan_distance(sensor_coordinates, beacon_coordinates)
    print(f"sensor: {sensor_coordinates} beacon: {beacon_coordinates} distance: {manhattan_distance}")

    current_min_columns = int(sensor_coordinates[0]) - manhattan_distance
    current_max_columns = int(sensor_coordinates[0]) + manhattan_distance
    if current_max_columns > max_columns:
        max_columns = current_max_columns

    if current_min_columns < min_columns:
        min_columns = current_min_columns

    sensors[sensor_coordinates] = {"beacon_coordinates": beacon_coordinates, "distance": manhattan_distance}
    beacons.append(beacon_coordinates)

print(sensors.keys())
print(f"min columns:{min_columns}")
print(f"max columns:{max_columns}")

beacons = [(int(x), int(y)) for x, y in beacons]
sensors_keys = [(int(x), int(y)) for x, y in sensors.keys()]
y = 2000000

# PART 1
counter = 0
for x in tqdm(range(min_columns, max_columns)):
    if (x, y) in beacons:
        continue

    if not beacons_available(x, y) and (x, y) not in beacons:
        counter += 1
print(counter)

# PART 1 finished


# PART 2
part_2_score = 0
for sensor in tqdm(sensors):
    x = int(sensor[0])
    y = int(sensor[1])
    distance = sensors[sensor]['distance']

    for dx in range(distance + 2):
        dy = (distance + 1) - dx
        for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
            new_x, new_y = x + (dx * mx), y + (dy * my)
            if not (0 <= new_x <= 4_000_000 and 0 <= new_y <= 4_000_000):
                continue

            if beacons_available(new_x, new_y):
                part_2_score = new_x * 4_000_000 + new_y
                print(part_2_score)
                break

print(part_2_score)
