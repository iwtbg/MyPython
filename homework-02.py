Dishes = int(input("Введите количество тарелок: "))
Cleanser = float(input("Введите количество моющего средства: "))

while Dishes >= 1 and Cleanser >=0.5:
    Dishes -= 1
    Cleanser -= 0.5
    print("Осталось вымыть ", Dishes, " тарелок")
    print("Осталось моющего средства: ", Cleanser, "мл")

print("На момент окончания мытья посуды осталось ", Dishes, "тарелок и", Cleanser, "мл моющего средства.")