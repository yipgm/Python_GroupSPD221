"""
Напишите программу, которая принимает на вход строку текста и подстроку,
а затем выводит индексы первого вхождения подстроки с начала и с конца строки (без учета регистра).

Шесть шустрых мышат в камышах шуршат

ша

"""

stroka = "Шесть шустрых мышат в камышах шуршат"
podstr = "ша"

print(stroka.find(podstr))
print(stroka.rfind(podstr))