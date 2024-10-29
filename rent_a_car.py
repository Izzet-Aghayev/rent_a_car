import json



def rent_a_car(*, client_car=0):
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data2 = data.get('cars_data2')

    cars_data2[client_car]['Müştəridədir'] = 'Bəli'
    
    with open('izzet_task11/data_base.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return f"{client_car} ID-li avtomobil icarəyə verildi."