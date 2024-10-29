import json


def ranking(*, sort: str=None, change: str=None) -> list:

    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1 = data.get('cars_data1')

    list_details = []
    if sort == '1':
        for data2 in cars_data1.values():
            list_details.append(data2['İstehsal tarixi'])
    elif sort == '2':
        for data2 in cars_data1.values():
            list_details.append(data2['Yürüşü'])
    elif sort == '3':
        for data2 in cars_data1.values():
            list_details.append(data2['Mühərrik həcmi'])
    elif sort == '4':
        for data2 in cars_data1.values():
            list_details.append(data2['Qiymət'])
    
    if change == '1':
        list_details.sort()
    elif change == '2':
        list_details.sort(reverse=True)
    return list_details