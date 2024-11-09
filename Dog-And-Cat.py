class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def eat(self):
        if self.hunger < 100:
            self.hunger += 10
            self.happiness += 5
            print(f"{self.name} з'їв і виглядає щасливішим!")
        else:
            print(f"{self.name} не голодний.")

    def sleep(self):
        if self.energy < 100:
            self.energy += 20
            self.happiness += 10
            print(f"{self.name} поспав і виглядає відпочилим!")
        else:
            print(f"{self.name} не хоче спати зараз.")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 20
            print(f"{self.name} грається і виглядає радісним!")
        else:
            print(f"{self.name} занадто втомлений, щоб гратися.")

    def status(self):
        print(f"Ім'я: {self.name}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print(f"Щастя: {self.happiness}")



my_cat = Cat("Сніжок")
my_cat.status()
my_cat.eat()
my_cat.play()
my_cat.sleep()
my_cat.status()
