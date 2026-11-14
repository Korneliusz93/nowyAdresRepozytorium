# commented out


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Miesiac w ktorym sie ucze to {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('pazdziernik 2026')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Witamy ma zajeciach z PY DEV w pazdzierniku 2026")
print("Moj program sprawdza czy jestes pelnoletni")

# v 1.0 aplikacji
age = input("Podaj wiek:")
if age.isdigit() != False:
    age = int(age)
    if age >= 18:
        print("Prosze bardzo")
        if 50 < age <= 60:
            print("Warning! Badz ostrozny z kofeina!")
        if 60 < age < 120:
            print("Warning! Odradzamy energetyki!")
        if age >= 120:
            exit("nieprawidlowy wiek")
    else:
        print("Odmowa")
else:
    exit("Nieprawidlowy wiek")






