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
    'Ford ',
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

    def __init__(self, number_of_wheels=0, number_of_transmission=1):
        if not self._check_nember_of_wheels():
            number_of_wheels = 0

    def _check_nember_of_wheels(self):
        return self.number_of_wheels >= 0

    def __set_name(self, name):
        self.manufacturer_name = name

    def set_name(self, name):
        if name in MANUFACTURERS:
            self.__set_name(name)

    def get_name(self):
        print(self.manufacturer_name)


class Truck(Transport):
    max_load_ton = 0
    has_trailer = False

    def __init__(self, number_of_wheels=8, number_of_transmission=2, max_load_ton=7):
        super().__init__(self, number_of_wheels, number_of_transmission)


class TruckLessThan7Ton(Truck):
    def __init__(self, number_of_wheels=8, number_of_transmission=2, max_load_ton=7):
        super().__init__(self, number_of_wheels, number_of_transmission, max_load_ton)

# class TruckBiggerThan7Ton(Truck):


