n = int(input("Введите количество слов: "))
s = ("")
for i in range(n):
    a = input("Введите слово: ")
    s = s + " " + a
print(s)

def z2():
    slova = []
    while (a := str(input("Введите слово: "))) != "stop":
        slova.append(a)

    print(" ".join(slova))

def z3():
    slova = [ ]
    while (a := str(input("Введите слово для проверки редкости: "))) != "stop":
        if "ф" in a or "Ф" in a:
            print("Легендарочка!")
        else:
            print("Коммонка...")

def z4():
    import random
    lives = 3
    while lives != 0:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        s = a + b
        ans = int(input(f"Сколько будет {a} + {b}? "))
        if s == ans:
            print("Хорош!")
        else:
            lives -= 1
            print("Чел ты...")
        continue

z2()
z3()
z4()