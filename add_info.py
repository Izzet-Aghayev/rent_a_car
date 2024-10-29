import json
from generate_id import generate_ids


def add_info(*,
        car_model=None,
        car_date=0,
        car_distance=0,
        car_engine_v=0.0,
        name_firstname=None,
        finnish_code=None,
        car_brand=None,
        car_num=None,
        car_color=None,
        car_price=0):
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')
        cars_data2 = data.get('cars_data2')
        
    car_id = generate_ids()
    car_data1 = dict()
    car_data1.update({'Model': car_model})
    car_data1.update({'İstehsal tarixi': car_date})
    car_data1.update({'Yürüşü': car_distance})
    car_data1.update({'Mühərrik həcmi': car_engine_v})
    car_data1.update({'Sahibin kimliyi': name_firstname})
    car_data1.update({'Fin': finnish_code})
    car_data1.update({'Nömrə': car_num})
    car_data1.update({'Rəng': car_color})
    car_data1.update({'Qiymət': car_price})

    car_data2 = dict()
    car_data2.update({'Marka': car_brand})
    car_data2.update({'Model': car_model})
    car_data2.update({'Yürüşü': car_distance})
    car_data2.update({'Mühərrik həcmi': car_engine_v})
    car_data2.update({'Nömrə': car_num})
    car_data2.update({'Rəng': car_color})
    car_data2.update({'Qiymət': car_price})
    car_data2.update({'Müştəridədir': 'Xeyir'})

    cars_data1.update({car_id: car_data1})
    cars_data2.update({car_id: car_data2}) 
    data.update({"cars_data1": cars_data1})
    data.update({"cars_data2": cars_data2})

    with open('izzet_task11/data_base.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)