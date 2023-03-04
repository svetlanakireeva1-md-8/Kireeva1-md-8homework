#1
# n = int(input("Введите количество слов"))
# word = ""
# for i in range(n):
#     word += input("Введите слово")
#     word += " "
# print(word)

#2
# a = ""
# word = str(input("Введите слово"))
# while word != "stop":
#     a = a + word + " "
#     word = str(input("Введите слово"))
# print(a)

#3
# word = input("Введите слово")
# for i in word:
#     if "ф" in word:
#         print("Ого! Это редкое слово!")
#         break
#     else:
#         print("Эх, это не очень редкое слово...")

#4
# from random import randint
# error = 0
# while error < 3:
#     x = int(randint(0,9))
#     y = int(randint(0,9))
#     print(x,"+",y,"=")
#     z=int(input("Введите ответ"))
#     if x+y!=z:
#         error+=1
# if error == 3:
#     print("Игра окончена")
