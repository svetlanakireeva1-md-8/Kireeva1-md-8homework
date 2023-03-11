def magik(day,month,year):
    return day * month == year % 100
d=int(input("Введите день"))
m=int(input("Введите месяц"))
y=int(input("Введите год"))
if 0<d<31 and 0<m<13 and 999<y:
    print(magik(d,m,y))
