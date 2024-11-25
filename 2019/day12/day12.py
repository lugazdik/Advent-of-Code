import re


def first_task(file, steps):
    positions = parse_input(file)
    velocities = [[0, 0, 0] for planet in range(len(positions))]
    for step in range(steps):
        do_step(positions, velocities)
    return calculate_energy(positions, velocities)


def join_positions(positions):
    res = []
    for position in positions:
        res.append(','.join(str(x) for x in position))
    return ','.join(res)


def parse_input(file):
    result = []
    with open(file,'r') as f:
        for line in f:
            x = re.findall('-?\d+', line)
            result.append(x)
        res = []
        for array in result:
            res.append(list(map(int,array)))
        return res


def do_step(positions, velocities):
    vel_index = 0
    for planet in positions:
        find_planet_velocities(planet, positions, velocities, vel_index)
        vel_index += 1
    update_positions(positions, velocities)


def find_planet_velocities(cur_planet, positions, velocities, vel_index):
    for planet in positions:
        if cur_planet == planet:
            continue
        for index in range(len(planet)):
            if cur_planet[index] < planet[index]:
                velocities[vel_index][index] += 1
            elif cur_planet[index] > planet[index]:
                velocities[vel_index][index] -= 1
    
        
def update_positions(positions, velocities):
    for position, velocity in zip(positions, velocities):
        for i in range(len(position)):
            position[i] += velocity[i]


def calculate_energy(positions, velocities):
    result = 0
    for position, velocity in zip(positions, velocities):
        pos_energy = 0
        kin_energy = 0
        for val in position:
            pos_energy += abs(val)
        for val in velocity:
            kin_energy += abs(val)
        result += pos_energy * kin_energy
    return result

# TASK ONE DONE, TASK TWO HARD, HINT IS TO FIND EACH ORBITS PERIOD AND CALCULATE LCM
# print(first_task('day12.txt', 1000))
