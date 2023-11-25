import random

class Person:
    def __init__(self, name, age=18, health=100, happiness=50, money=1000):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.money = money

    def get_older(self, years=1):
        self.age += years
        self.health -= random.randint(0, 5)
        self.happiness -= random.randint(0, 5)

    def work(self):
        earnings = random.randint(100, 1000)
        self.money += earnings
        self.happiness -= random.randint(0, 5)
        return earnings

    def socialize(self):
        self.happiness += random.randint(10, 20)

    def see_doctor(self):
        cost = random.randint(50, 200)
        self.health += random.randint(10, 20)
        self.money -= cost
        self.happiness += random.randint(5, 10)

    def display_status(self):
        print(f"\n{name}'s Status:")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print(f"Money: {self.money}")

# Игровой цикл
name = input("Введите имя персонажа: ")
player = Person(name)

while player.health > 0 and player.happiness > 0 and player.money > 0:
    action = input("\nВыберите действие: 1 - Прожить год, 2 - Работать, 3 - Общение, 4 - Посетить врача, 5 - Посмотреть статус: ")

    if action == '1':
        player.get_older()
    elif action == '2':
        earnings = player.work()
        print(f"Вы поработали и заработали {earnings} денег.")
    elif action == '3':
        player.socialize()
        print("Вы провели время с друзьями.")
    elif action == '4':
        player.see_doctor()
        print("Вы посетили врача.")
    elif action == '5':
        player.display_status()
    else:
        print("Неверный выбор. Попробуйте снова.")

# Игра завершена
print("Игра окончена. Ваш персонаж ушел в мир иной.")
