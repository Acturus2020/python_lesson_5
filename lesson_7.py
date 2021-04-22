MANUFACTURERS = [
    'Acura',
    'Alfa Romeo',
    'Apollo',
    'Apple',
    'Aston Martin',
    'Audi ',
    'Automobili Pininfarina',
    'Bentley',
    'BMW ',
    'Bollinger',
    'Brilliance',
    'Bugatti',
    'Buick',
    'BYD ',
    'Cadillac',
    'Chana ',
    'Chery ',
    'Chevrolet ',
    'Chrysler ',
    'Citroen ',
    'Continental',
    'Cupra ',
    'Dacia ',
    'Daewoo ',
    'Daihatsu',
    'Datsun ',
    'Detroit Electric',
    'Dodge ',
    'DS Automobiles',
    'FAW ',
    'Ferrari',
    'Fiat ',
    'Fisker',
    'Ford',
    'Geely ',
    'Genesis',
    'GMC ',
    'Great Wall',
    'Haval ',
    'Honda ',
    'Hummer ',
    'Hyundai ',
    'Infiniti ',
    'Iran Khodro',
    'JAC ',
    'Jaguar',
    'Jeep ',
    'JETOUR',
    'KIA ',
    'Lada ',
    'Lamborghini',
    'Lancia ',
    'Land Rover',
    'Lexus ',
    'Lifan ',
    'Lincoln ',
    'Lordstown',
    'LvChi ',
    'Lynk & Co',
    'Maserati',
    'Maybach',
    'Mazda ',
    'MCLaren ',
    'Mercedes-Benz',
    'MG ',
    'MINI ',
    'Mitsubishi',
    'Nikola',
    'NIO ',
    'Nissan',
    'Opel ',
    'Pagani ',
    'Peugeot ',
    'Polestar',
    'Porsche',
    'Qoros ',
    'Range Rover',
    'Ravon ',
    'Renault',
    'Rimac ',
    'Rivian ',
    'Rolls-Royce',
    'Saab ',
    'Saipa ',
    'SEAT ',
    'Skoda ',
    'smart ',
    'SsangYong',
    'SSC North America',
    'Stellantis',
    'Subaru ',
    'Suzuki',
    'Tata ',
    'Tesla ',
    'Toyota',
    'Volkswagen',
    'Volvo ',
    'Zotye',
    'ВАЗ ',
    'ГАЗ ',
    'ЗАЗ ',
    'КрАЗ',
    'УАЗ'
]


class Transport:
    year_born = 0
    manufacturer_name = ''
    model_name = ''
    gasoline = ''
    is_electric = False
    number_of_wheels = 0
    number_of_transmission = 1
    is_cargo = False
    is_passenger = False
    best_transport = False

    def __init__(self, number_of_wheels=0, number_of_transmission=1):
        if not self._check_nember_of_wheels():
            number_of_wheels = 0

    def _check_nember_of_wheels(self):
        return self.number_of_wheels >= 0

    def __set_manufacturer(self, manufacturer):
        self.manufacturer_name = manufacturer

    def set_manufacturer(self, manufacturer):
        if manufacturer in MANUFACTURERS:
            self.__set_manufacturer(manufacturer)

    def get_manufacturer(self):
        print(self.manufacturer_name)


class Truck(Transport):
    max_load_ton = 0
    has_trailer = False

    def __init__(self, number_of_wheels=8, number_of_transmission=2, max_load_ton=7, is_cargo=True):
        super().__init__(number_of_wheels, number_of_transmission)


class Bus(Transport):
    def __init__(self, number_of_wheels=6, is_passenger=True):
        super().__init__(number_of_wheels)


class MotoTransport(Transport):
    def __init__(self, number_of_wheels=2):
        super().__init__(number_of_wheels)


class Car(Transport):
    def __init__(self, number_of_wheels=4, is_passenger=True, is_cargo=False):
        super().__init__(number_of_wheels)


class TruckLessThan7Ton(Truck):
    def __init__(self, number_of_wheels=8, number_of_transmission=2, max_load_ton=7, is_cargo=True):
        super().__init__(number_of_wheels, number_of_transmission, max_load_ton, is_cargo)


class TruckBiggerThan7Ton(Truck):
    def __init__(self, number_of_wheels=8, number_of_transmission=3, max_load_ton=10, is_cargo=True):
        super().__init__(number_of_wheels, number_of_transmission, max_load_ton, is_cargo)


class BusLessThan10People(Bus):
    def __init__(self, number_of_wheels=6, is_passenger=True):
        super().__init__(number_of_wheels, is_passenger)


class BusForMoreThan10People(Bus):
    def __init__(self, number_of_wheels=10, is_passenger=True):
        super().__init__(number_of_wheels, is_passenger)


class Motorcycle(MotoTransport):
    def __init__(self, number_of_wheels=2, best_transport=True, is_passenger=True):
        super().__init__(number_of_wheels)


class Moped(MotoTransport):
    def __init__(self, number_of_wheels=2):
        super().__init__(number_of_wheels)


class Sedan(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


class Miniven(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


class Coupe(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


class MuscleCar(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


class Universal(Car):
    def __init__(self, is_passenger=True, is_cargo=True):
        super().__init__(is_cargo)


class Hatchback(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


class Cabriolet(Car):
    def __init__(self, is_passenger=True):
        super().__init__()


def main():
    Ford_musstang = MuscleCar()
    Ford_musstang.set_manufacturer('Ford')
    print(Ford_musstang.manufacturer_name)

