def first_task(file):
    planets = parse_input(file)
    result = 0
    for planet in planets.keys():
        result += len(find_orbits(planets, planet))
    return result


def second_task(file):
    planets = parse_input(file)
    my_orbits = set(find_orbits(planets, 'YOU'))
    santa_orbits = set(find_orbits(planets, 'SAN'))
    same_orbits = my_orbits.intersection(santa_orbits)
    return len(my_orbits) + len(santa_orbits) - (len(same_orbits)*2)


def find_orbits(planets, planet):
    orbits = []
    while planets[planet] is not None:
        orbits.append(planets[planet])
        planet = planets[planet]
    return orbits


def parse_input(file):
    with open(file,'r') as f:
        planets = {}
        for line in f:
            split_line = line.split(')')
            if split_line[0] not in planets:
                planets[split_line[0].strip()] = None
            planets[split_line[1].strip()] = split_line[0].strip()
        return planets


# print(first_task('day06.txt'))
print(second_task('day06.txt'))
