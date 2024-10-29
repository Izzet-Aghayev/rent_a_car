import time
from login import *
from add_info import *
from check_funcs import *
from about_cars import *
from delete_car import delete_car
from detail_update import detail_update, update_info
from about_cars import *
from filters import *
from rent_a_car import rent_a_car
from ranking_func import ranking


username = input("İstifadəçi adını daxil edin: ")           # a
password = input("İstifadəçi şifrəsini daxil edin: ")       # a

stop = ''
counter = 0
while stop != '0':
    login1(username=username, password=password, flag=flag)

    counter += 1
    if counter == 1:
        print("RENT-A-CAR PROQRAMINA XOŞ GƏLMİSİNİZ :)")
        print('-'*50)
    time.sleep(1)

    transaction = input('''
            Avtomobil məlumatlarını əlavə etmək üçün ---> 1
            Bütün avtomobillərə baxmaq üçün ---> 2
            Spesifik bir avtomobilin detallarına baxmaq üçün ---> 3
            Avtomobil silmək üçün ---> 4
            Məlumatları yeniləmək üçün ---> 5
            Avtomobili icarəyə vermək üçün ---> 6
            Avtomobilləri filterləmək üçün ---> 7
            Avtomobilləri sıralamaq üçün ---> 8
            Proqramdan çıxış etmək üçün ---> 0
            yazılarını yazın: ''')
            
    if transaction == '1':
        print('-'*50)  
        car_model = input("Avtomobilin modelini daxil edin: ")
        car_date = input("Avtomobilin istehsal tarixinin daxil edin: ")
        while check_int_detail(car_int_detail=car_date):
            car_date = input("Avtomobilin istehsal tarixinin daxil edin: ")
        car_date = int(car_date)

        car_distance = input("Avtomobilin yürüşünü daxil edin: ")
        while check_int_detail(car_int_detail=car_distance):
            car_distance = input("Avtomobilin yürüşünü daxil edin: ")
        car_distance = int(car_distance)
        
        flag_enginier = True
        while flag_enginier:
            try:    
                car_engine_v = float(input("Avtomobilin mühərrik həcmini daxil edin: "))
                flag_enginier = False
            except Exception:
                print("Ədəd daxil edilməlidir.")

        name_firstname = input("Avtomobilin sahibinin adını və soyadını daxil edin: ").capitalize()
        finnish_code = input("Avtomobilin sahibinin fin kodunu daxil edin: ").upper()
        while check_fin(finnish_code=finnish_code):
            finnish_code = input("Avtomobilin sahibinin fin kodunu daxil edin: ").upper()

        car_brand = input("Avtomobilin markasını daxil edin: ")
        car_num = input("Avtomobilin qeydiyyat nişanını [00-RR-000] formatında daxil edin: ").upper()
        while check_car_num(car_num=car_num):
            car_num = input("Avtomobilin qeydiyyat nişanını [00-RR-000] formatında daxil edin: ").upper()

        car_color = input("Avtomobilin rəngini daxil edin: ")
        car_price = input("Avtomobilin qiymətini daxil edin: ")
        while check_int_detail(car_int_detail=car_price):
            car_price = input("Avtomobilin qiymətini daxil edin: ")
        car_price = int(car_price)

        print('-'*50)

        add_info(car_model=car_model, car_date=car_date,car_distance=car_distance,
                car_engine_v=car_engine_v, name_firstname=name_firstname,
                finnish_code=finnish_code, car_brand=car_brand, car_num=car_num,
                car_color=car_color, car_price=car_price)
        print("Məlumatlar uğurla daxil edildi.")
                

    elif transaction == '2':
        about_cars()

    elif transaction == '3':
        print('-'*50)
        car_choice = input("Avtomobilin ID-sini daxil edin: ")
        print('-'*50)
        print(specific_car(car_choice=car_choice))
                
    elif transaction == '4':
        print('-'*50)
        car_del = input("Siləcəyiniz avtomobilin ID-sini yazın: ")
        print('-'*50)
        print(delete_car(car_del=car_del))

    elif transaction == '5':
        print('-'*50)
        car = input("Məlumatı yenilənəcək avtomobilin ID-sini daxil edin: ")
        choice_update = input("""
            Sipesifik bir məlumatı dəyişdirmək üçün ---> 1
            Avtomobilin ümumi məlumatlarını dəyişdirmək üçün ---> 2
            yazdırın: """)
        if choice_update == '1':
            print(detail_update(car=car))
        elif choice_update == '2':
            car_model = input("Avtomobilin modelini daxil edin: ")
            car_date = input("Avtomobilin istehsal tarixinin daxil edin: ")
            while check_int_detail(car_int_detail=car_date):
                car_date = input("Avtomobilin istehsal tarixinin daxil edin: ")
            car_date = int(car_date)

            car_distance = input("Avtomobilin yürüşünü daxil edin: ")
            while check_int_detail(car_int_detail=car_distance):
                car_distance = input("Avtomobilin yürüşünü daxil edin: ")
            car_distance = int(car_distance)
            
            flag_enginier = True
            while flag_enginier:
                try:    
                    car_engine_v = float(input("Avtomobilin mühərrik həcmini daxil edin: "))
                    flag_enginier = False
                except Exception:
                    print("Ədəd daxil edilməlidir.")

            name_firstname = input("Avtomobilin sahibinin adını və soyadını daxil edin: ").capitalize()
            finnish_code = input("Avtomobilin sahibinin fin kodunu daxil edin: ").upper()
            while check_fin(finnish_code=finnish_code):
                finnish_code = input("Avtomobilin sahibinin fin kodunu daxil edin: ").upper()

            car_brand = input("Avtomobilin markasını daxil edin: ")
            car_num = input("Avtomobilin qeydiyyat nişanını [00-RR-000] formatında daxil edin: ").upper()
            while check_car_num(car_num=car_num):
                car_num = input("Avtomobilin qeydiyyat nişanını [00-RR-000] formatında daxil edin: ").upper()

            car_color = input("Avtomobilin rəngini daxil edin: ")
            car_price = input("Avtomobilin qiymətini daxil edin: ")
            while check_int_detail(car_int_detail=car_price):
                car_price = input("Avtomobilin qiymətini daxil edin: ")
            car_price = int(car_price)

            print('-'*50)

            update_info(car_id1=car, car_model=car_model, car_date=car_date,car_distance=car_distance,
                    car_engine_v=car_engine_v, name_firstname=name_firstname,
                    finnish_code=finnish_code, car_brand=car_brand, car_num=car_num,
                    car_color=car_color, car_price=car_price)
            print("Məlumatlar uğurla yeniləndi.")

    elif transaction == '6':
        print('-'*50)
        about_cars()
        client_car = input("Seçdiyiniz avtomobilin ID-sini daxil edin: ")
        print(rent_a_car(client_car=client_car))

    elif transaction == '7':
        print('-'*50)
        choice = input("""
            Filtir edəcəyiniz hissəni seçin
            Model üçün ---> 1
            İstehsal tarixi üçün ---> 2
            Yürüşü üçün ---> 3
            Mühərriki üçün ---> 4
            Sahibinin adı üçün ---> 5
            Finn kod üçün ---> 6
            Marka üçün ---> 7
            Rəng üçün ---> 8
            Qiyməti üçün ---> 9
            rəqəmlərini yazın: """)
        if choice == '1':
            filter_model()
        elif choice == '2':
            filter_date()
        elif choice == '3':
            filter_distance()
        elif choice == '4':
            filter_engine_v()
        elif choice == '5':
            filter_firstname()
        elif choice == '6':
            filter_finn()
        elif choice == '7':
            filter_marka()
        elif choice == '8':
            filter_color()
        elif choice == '9':
            filter_price()

    elif transaction == '8':
        sort = input("""
            İstehsal tarixi üçün ---> 1
            Yürüşü üçün ---> 2
            Mühərriki üçün ---> 3
            Qiyməti üçün ---> 4
            """)
        change = input("""
            Artıan sıra üçün ---> 1
            Azalan sıra üçün ---> 2
            """)
        print(ranking(sort=sort, change=change))

    elif transaction == '0':
        stop = transaction

    else:
        print('-'*50)
        print(f"{transaction} əməliyyatı mövcud deyil.")