class Building:
    def __init__(self, cost, polution, upgrade, income):
        self.__cost = cost
        self.__polution = polution
        self.__upgrade = upgrade
        self.__income = income

    def get_income(self):
        return self.__income

    def get_polution(self):
        return self.__polution

    def get_cost(self):
        return self.__cost

    def get_upgrade(self):
        return self.__upgrade

    polution = property(get_polution)
    cost = property(get_cost)
    upgrade = property(get_upgrade)
    income = property(get_income)


class Factory(Building):
    def __init__(self, cost, polution, upgrade, income):
        super().__init__(cost, polution, upgrade, income)

    def upgrade(self):
        if self.__upgrade == 2:
            self.__income = 1.5 * self.__income
            self.__polution = 2 * self.__polution

        elif self.__upgrade == 1:
            self.__income = 1.25 * self.__income
            self.__polution = 1.75 * self.__polution


class Windturbine(Building):
    def __init__(self, cost, polution, upgrade, income):
        super().__init__(cost, polution, upgrade, income)

    def upgrade(self):
        if self.__upgrade == 2:
            self.__income = 1.5 * self.__income

        elif self.__upgrade == 1:
            self.__income = 1.25 * self.__income


class Cleaning_station(Building):
    def __init__(self, cost, polution, upgrade, income):
        super().__init__(cost, polution, upgrade, income)

    def upgrade(self):
        if self.__upgrade == 2:
            self.__polution = 0.25 * self.__polution

        elif self.__upgrade == 1:
            self.__polution = 0.5 * self.__polution

