import random


def generate_ids():
    id_list = []
    check = True
    while check:
        new_id_car = random.randint(100, 1000)
        if new_id_car not in id_list:

            id_list.append(new_id_car)
            car_id = new_id_car
            check = False
    return car_id