import json


def filter_model():

    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_model = dict()
    filter_detail = input("Avtomobilin modelini daxil edin: ")
    for data in cars_data1.values():
        for key in data:
            if key == 'Model':
                if filter_detail == data[key]:
                    counter += 1
                    db_model[counter] = data

    for counter1, data1 in db_model.items():
        print(f"{counter1}) {data1}")
    if db_model == {}:
        print(f"{filter_detail} modelli avtomobil tapılmadı.")


def filter_date():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_date = dict()
    filter_detail = int(input("Avtomobilin istehsal tarixini daxil edin: "))
    for data in cars_data1.values():
        for key in data:
            if key == 'İstehsal tarixi':
                if filter_detail <= data[key]:
                    counter += 1
                    db_date[counter] = data

    for counter1, data1 in db_date.items():
        print(f"{counter1}) {data1}")
    if db_date == {}:
        print(f"{filter_detail} istehsal tarixli avtomobil tapılmadı.")


def filter_distance():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_distance = dict()
    filter_detail = int(input("Avtomobilin yürüşünü daxil edin: "))
    for data in cars_data1.values():
        for key in data:
            if key == 'Yürüşü':
                if filter_detail <= data[key]:
                    counter += 1
                    db_distance[counter] = data

    for counter1, data1 in db_distance.items():
        print(f"{counter1}) {data1}")
    if db_distance == {}:
        print(f"{filter_detail} yürüşlü avtomobil tapılmadı.")


def filter_engine_v():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_engine = dict()
    filter_detail = float(input("Avtomobilin mühərrik həcmini daxil edin: "))
    for data in cars_data1.values():
        for key in data:
            if key == 'Mühərrik həcmi':
                if filter_detail <= data[key]:
                    counter += 1
                    db_engine[counter] = data

    for counter1, data1 in db_engine.items():
        print(f"{counter1}) {data1}")
    if db_engine == {}:
        print(f"{filter_detail} mühərrik həcimli avtomobil tapılmadı.")


def filter_firstname():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_firstname = dict()
    filter_detail = input("Avtomobilin sahibinin kimliyini daxil edin: ")
    for data in cars_data1.values():
        for key in data:
            if key == 'Sahibin kimliyi':
                if filter_detail == data[key]:
                    counter += 1
                    db_firstname[counter] = data

    for counter1, data1 in db_firstname.items():
        print(f"{counter1}) {data1}")
    if db_firstname == {}:
        print(f"{filter_detail} kimlikli sahibi olan avtomobil tapılmadı.")


def filter_finn():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_finn = dict()
    filter_detail = input("Avtomobilin sahibinin finini daxil edin: ")
    for data in cars_data1.values():
        for key in data:
            if key == 'Fin':
                if filter_detail == data[key]:
                    counter += 1
                    db_finn[counter] = data

    for counter1, data1 in db_finn.items():
        print(f"{counter1}) {data1}")
    if db_finn == {}:
        print(f"{filter_detail} finli  avtomobil tapılmadı.")


def filter_marka():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')
        cars_data2 = data.get('cars_data2')

    counter = 0
    db_marka = dict()
    filter_detail = input("Avtomobilin markasını daxil edin: ")
    for data in cars_data2.values():
        for key in data:
            if key == 'Marka':
                if filter_detail == data[key]:
                    for data3 in cars_data1:
                        if data['Fin'] == data3['Fin']:
                            counter += 1
                            db_marka[counter] = data3

    for counter1, data1 in db_marka.items():
        print(f"{counter1}) {data1}")
    if db_marka == {}:
        print(f"{filter_detail} markalı  avtomobil tapılmadı.")


def filter_car_num():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_car_num = dict()
    filter_detail = input("Avtomobilin seriyasını daxil edin: ")
    for data in cars_data1.values():
        for key in data:
            if key == 'Nömrə':
                if filter_detail == data[key][:2]:
                    counter += 1
                    db_car_num[counter] = data

    for counter1, data1 in db_car_num.items():
        print(f"{counter1}) {data1}")
    if db_car_num == {}:
        print(f"{filter_detail} seriyali  avtomobil tapılmadı.")


def filter_color():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_color = dict()
    filter_detail = input("Avtomobilin rəngini daxil edin: ")
    for data in cars_data1.values():
        for key in data:
            if key == 'Rəng':
                if filter_detail == data[key]:
                    counter += 1
                    db_color[counter] = data

    for counter1, data1 in db_color.items():
        print(f"{counter1}) {data1}")
    if db_color == {}:
        print(f"{filter_detail} rəngdə avtomobil tapılmadı.")


def filter_price():
    
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    counter = 0
    db_price = dict()
    filter_detail = int(input("Avtomobilin qiymətini daxil edin: "))
    for data in cars_data1.values():
        for key in data:
            if key == 'Qiymət':
                if filter_detail <= data[key]:
                    counter += 1
                    db_price[counter] = data

    for counter1, data1 in db_price.items():
        print(f"{counter1}) {data1}")
    if db_price == {}:
        print(f"{filter_detail} qiymətdə olan avtomobil tapılmadı.")
