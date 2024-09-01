class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(House(self.number_of_floors)):
            if self.number_of_floors > new_floor:
                self.number_of_floors += 1
                print(new_floor)
            elif new_floor > self.number_of_floors:
                print('Такого этажа не существует')
            continue

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


#class House:
#    def __init__(self, name, number_of_floors):
#        self.name = name
#        self.number_of_floors = number_of_floors
#
#    def go_to(self, new_floor):
#
#        if self.number_of_floors > new_floor:
#            self.number_of_floors += 1
#            print(new_floor)
#        elif new_floor > self.number_of_floors:
#            print('Такого этажа не существует')
#
#
#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)
#h1.go_to(5)
#h2.go_to(10)
