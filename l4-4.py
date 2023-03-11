def happy(n):
    return sum(map(int,str(n)[:len(str(n))//2]))==sum(map(int,str(n)[len(str(n))//2:]))
nom=int(input("Введите номер билета"))
if len(str(nom))%2==0:
    print(happy(nom))
else:
    print("Нечетное кол-во цифр в билете")