import json


def delete_car(*, car_del=0):
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')
        cars_data2 = data.get('cars_data2')

    if car_del in cars_data1:
        cars_data1.pop(car_del)
        cars_data2.pop(car_del)

        with open('izzet_task11/data_base.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return f"{car_del} ID-li avromobil proqramdan silindi."
    else:
        return f"{car_del} ID-li avtomobil yoxdur"
    