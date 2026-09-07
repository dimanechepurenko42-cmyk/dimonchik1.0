#написать метод который будет определять регион по номеру

# def region_name(num):
#     if num == "1":
#         return "Бишкек"
#     elif num =="2":
#         return "Ош"
#     elif num =="3":
#         return "Баткенская область"
#     elif num == "4":
#         return "Джалал-Абад"
#     elif num == "5":
#         return "Нарынская область"
#     elif num =="6":
#             return "Ошская область"
#     elif num == "7":
#          return "Таласская область"
#     elif num == "8":
#          return "Чуйская область"
#     elif num == "9":
#          return "Иссык-Кульская область"
#     elif num == "10":
#          return "Легализованный транспорт"
#     elif num == "11":
#          return "Транспорт на временном учете"

# print(region_name(input("Введите номер региона")))



#написать метод который проверяет возраст на совершеннолетие

def age_name(age):
     if age > 115:
        return False
     elif age >= 18:
        return True
     elif age < 18:
          return False
     
     

print(age_name(int(input("сколько вам лет?"))))