class car:
    def __init__(self, name, model, year, horsepower):
        self.name = name
        self.model = model
        self.year = year
        self.horsepower = horsepower

    def get_info(self):
        return f"{self.name} {self.model} {self.year} {self.horsepower}"


bmw = car("BMW", "e36", 1998, 140)
print(bmw.get_info())

lancia = car("Lancia", "Delta", 1995, 120)
print(lancia.get_info())

audi = car("Audi", "A4", 2005, 180)
print(audi.get_info())
