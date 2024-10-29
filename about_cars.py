import json



def about_cars():
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    for keys, vaules in cars_data1.items():
        print(f"{keys} id-li avtomobilin məlumatları: {vaules}")
    if cars_data1 == {}:
        print('Məlumat yoxdur.')


def specific_car(*, car_choice=0):
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data2 = data.get('cars_data2')

    if car_choice in cars_data2:
        return cars_data2.get(car_choice)
    else:
        return f"{car_choice} ID-li avtomobil yoxdur"
    