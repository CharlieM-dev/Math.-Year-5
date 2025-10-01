# A helicopter can fly 720 km in 4 hours. How many km will it fly in 6 hours if its speed remains the same?

def distance_calculation():
    starting_time = float(input('Please, enter the starting time in hours: '))
    starting_distance = float(
        input('Please, enter the starting distance in km: '))
    new_time = float(input('Please, enter the new time in hours: '))
    if starting_time > 0 and starting_distance > 0:
        speed = round(starting_distance / starting_time, 2)
    else:
        return 'Sorry, but it does not make sense for time or distance to be 0 in this case. Try again!'
    if new_time > 0:
        new_distance = round(speed * new_time, 2)
        return f'So if the helicopter is moving with speed of {speed}km/hr, the distance it can travel in {new_time} hours is {new_distance} kilometer(s)'
    else:
        return 'Sorry but if new time is 0, then you will get 0. And speed being lower than 0 does not make sense so try again, please!'


result = distance_calculation()
print(result)
