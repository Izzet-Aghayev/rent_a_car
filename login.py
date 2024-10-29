import time


flag = True
def login1(*, username: str=None, password: str=None, flag: bool=False):
    while flag:
        if username == 'a' and password == 'a':
            print('-'*50)
            flag = False

        elif username == 'a' and password != 'a':
            print('-'*50)
            print("İstifadəçi şifrəsi yanlışdır, təkrar daxil edə və ya '0' yazaraq çıxa bilərsiniz.")
            print('-'*50)
            time.sleep(1)
            password = input("İstifadəçi şifrəsini daxil edin: ")

        elif username != 'a' and password == 'a':
            print('-'*50)
            print("İstifadəçi adı yanlışdır, təkrar daxil edə və ya '0' yazaraq çıxa bilərsiniz.")
            print('-'*50)
            time.sleep(1)
            username = input("İstifadəçi adını daxil edin: ")

        else:
            print('-'*50)
            print("İstifadəçi adı və şifrəsi yanlışdır, təkrar daxil edə və ya '0' yazaraq çıxa bilərsiniz.")
            print('-'*50)
            time.sleep(1)
            username = input("İstifadəçi adını daxil edin: ")
            password = input("İstifadəçi şifrəsini daxil edin: ")

