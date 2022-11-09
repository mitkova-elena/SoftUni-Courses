from collections import deque


def read_robots():
    result = {}
    all_robots_info = input().split(';')
    for robot_info in all_robots_info:
        robot_details = robot_info.split('-')
        robot_name = robot_details[0]
        processing_time = int(robot_details[1])
        result[robot_name] = processing_time
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def read_products():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break
        result.append(line)
    return result


def to_string_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()

available_robots = ([k for k in robots.keys()])
processing_robots = {}

starting_time_parts = [int(x) for x in input().split(':')]

time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()


while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for current_robot in [k for k in processing_robots.keys()]:
        processing_robots[current_robot] -= 1
        if processing_robots[current_robot] <= 0:
            processing_robots.pop(current_robot)

    current_product = products.popleft()
    for robot in available_robots:
        if robot not in processing_robots:
            print(f"{robot} - {current_product} [{to_string_time(time_in_seconds)}]")
            processing_robots[robot] = int(robots[robot])
            break
    else:
        products.append(current_product)
