from string import ascii_uppercase
import json


def check_fin(*, finnish_code: str=None) -> bool:
    fin_list = []
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1_values = data.get('cars_data1').values()
        for g in cars_data1_values:
            fin_list.append(g.get('Fin'))


    if len(finnish_code) == 7:
        if finnish_code in fin_list:
            print("Fin kod DB-da mövcuddur.")
            return True
        else:
            return False
    else:
        print("Fin kod 7 simvoldan ibarət olmalıdır.")
        return True

  
def check_car_num(*, car_num: str=None) -> bool:
    car_num_list = []
    with open('izzet_task11/data_base.json', encoding='utf-8') as file:
        data = json.load(file)
        cars_data1_values = data.get('cars_data1').values()
        for g in cars_data1_values:
            car_num_list.append(g.get('Nömrə'))

    NUMBERS_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    EXTRANEOUS_LETTERS = 'WİÜƏÖĞÇŞ'
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag6 = False
    flag7 = False
    flag8 = False
    flag9 = False
    flag10 = False
    num_element_lst = []
    if car_num in car_num_list:
        print("Nömrə DB-da mövcuddur.")
        return True
    else:
        for element in car_num:
            num_element_lst.append(element)
        
        if len(num_element_lst) == 9:
            if num_element_lst[0] in NUMBERS_LIST:
                flag1 = True
            if num_element_lst[1] in NUMBERS_LIST:
                flag2 = True
            if num_element_lst[2] == '-':
                flag3 = True
            if (num_element_lst[3] in ascii_uppercase and num_element_lst[3] not in EXTRANEOUS_LETTERS):
                flag4 = True
            if (num_element_lst[4] in ascii_uppercase and num_element_lst[4] not in EXTRANEOUS_LETTERS):
                flag5 = True
            if num_element_lst[5] == '-':
                flag6 = True
            if num_element_lst[6] in NUMBERS_LIST:
                flag7 = True
            if num_element_lst[7] in NUMBERS_LIST:
                flag8 = True
            if num_element_lst[8] in NUMBERS_LIST:
                flag9 = True
            if (num_element_lst[0] == '0' or num_element_lst[1] == '0'):
                flag10 = False
            else:
                flag10 = True

            if (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9 and flag10):
                pass
            else:
                print("Nömrə formatı düzgün deyil.")
                return True  
        else:
            print("Nömrə formatı düzgün deyil.")
            return True  
        

def check_int_detail(*, car_int_detail) -> bool:
    numbers_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    car_detail_lst = []
    lst2 = []
    k = 0
    for i in car_int_detail:
        car_detail_lst.append(i)
    while k < len(car_detail_lst):
        k += 1
        lst_element = car_detail_lst[k-1]
        if lst_element in numbers_lst:
            lst2.append(lst_element)

    if len(lst2) == len(car_detail_lst):
        return False
    else:
        return True        