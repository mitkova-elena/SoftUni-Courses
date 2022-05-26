# free window - the light in so more green, but the car is safe to move on and to not be hit
from collections import deque

start_green_light_duration = int(input())
green_light_duration = start_green_light_duration
free_window_duration = int(input())
cars_queue = deque()
passed_cars = 0

command = input()

safe_road = True

while safe_road and command != 'END':
    if command == 'green':
        while green_light_duration > 0 and cars_queue:
            current_car = cars_queue.popleft()
            if len(current_car) <= (green_light_duration + free_window_duration):
                passed_cars += 1
                green_light_duration -= len(current_car)
                if green_light_duration < 0:
                    free_window_duration += green_light_duration
            else:
                x = current_car[green_light_duration + free_window_duration]
                print("A crash happened!")
                print(f"{current_car} was hit at {x}.")
                safe_road = False
                break

        green_light_duration = start_green_light_duration
        command = input()
    else:
        cars_queue.append(command)
        command = input()

if safe_road:
    print('Everyone is safe.')
    print(f"{passed_cars} total cars passed the crossroads.")
