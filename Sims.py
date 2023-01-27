import random
class Human:
    def __init__(self, name="Human", job=None,home = None, car = None):
        self.name = name
        self.job= job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.pet = pet
    def get_home(self):
        self.home=House()
    def get_car(self):
        self.car=Auto(brand_list)

    def get_pet(self):
        self.pet=pet

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=job(get_job)
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
            self.satiety+=5
            self.home.food+=5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.shopping("fuel"):
                return
            else:
                self.to_repair()
                return
        self.money+=self.job.salary
        self.gladness-=self.job.gladness_less
        self.satiety-=4

        def shopping(self,manage):
            if self.car.drive():
                pass
            else:
                if self.car.fuel<20:
                    manage="fuel"
                else:
                    self.to.repair()
                    return
            if manage=="fuel":
                print("купити пальне")
                self.money-=100
                self.car.fuel+=100
            elif manage=="food":
                print("купити їжу")
                self.money-=50
                self.home.food+=50
            elif manage=="feed":
                print("купити корм домашній тварині")
                self.money-=70
                self.pet+=70
            elif manage=="deliciuos":
                print("Ура! Смаколики!")
                self.money-=15
                self.gladness+=10
                self.satiety+=2

    def chill(self):
        self.gladness+=15
        self.home.mess+=5

    def clean_home(self):
        self.gladness-=10
        self.home.mess=0

    def to_repair(self):
        self.car.strenght+=100
        self.money-=50

    def days_indexes(self,day):
        day=f"Today the {day} of {self.name}'a life"
        print(f"{day:=^50}","\n")
        human_indexes=self.name + " 's indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money-{self.money}")
        print(f"Satiety-{self.satiety}")
        print(f"Gladness-{self.gladness}")
        home_indexes="Home indexes"
        print(f"{home_indexes:^50}","\n")
        print(f"Food-{self.home.food}")
        print(f"Mess-{self.home.mess}")
        car_indexes=f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}","\n")
        print(f"Fuel-{self.car.fuel}")
        print(f"Strength-{self.car.strenght}")

    def is_alive(self):
        if self.gladness<=0:
            print("Дипресія")
            return False
        if self.satiety<0:
            print("Голод")
            return False
        if self.money<-500:
            print("Банкрот")
            return  False

    def live(self, day):
        if self.is_alive()==False:
            return False
        if self.gome is None:
            print("Переселився в будинок")
            self.get_home()
        if self.cer is None:
            self.get_car()
            print(f"я купив машину{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"я не маю роботи,я йду отримати роботу{self.job.job}з зарплатою {self.job.salary}")
        self.days_indexes()
        dece=random.randint(1,4)
        if self.satiety<20:
            print("я йду їсти")
            self.eat()
        elif self.gladness<20:
            if self.home.mess>15:
                print("я хочу відпочити, але в будинку брудно \n тож я піду прибирати будинок")
                self.clean_home()
            else:
                print("я відпочиваю")
                self.chill()
        elif self.money<0:
            print("я іду працювати")
            self.work()
        elif self.car.strenght<15:
             print("мені потрібно відремонтувати машину")
             self.to_repair()
        elif dece==1:
             print("давайте відпочинемо")
             self.chill()
        elif dece==2:
             print("початок роботи")
             self.work()
        elif dece==3:
             print("час прибирання")
             self.clean_home()
        elif dece==4:
            print("час погратись з домашньою твариною")
            self.pet
        elif dece==5:
             print("час смачненького")
             self.shopping(manage="delicacies")


class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        brand_of_car = {
    "BMW":{"F-fuel":100,"strength":100,"consumption":6},
    "Lada":{"F-fuel":50,"strength":40,"consumption":10},
    "Volvo":{"F-fuel":70,"strength":150,"consumption":8},
    "Ferrari":{"F-fuel":70,"strength":120,"consumption":14}}
    def drave(self):
     if self.strenght>0 and self.consumption:
         self.fuel-=self.consumption
         self.strenght-=1
         return True
     else:
         print("Машина не може рухатися")
         return False
class House:
    def __init__(self):
        self.mess=0
        self.food=0
class pet:
    def __init__(self,pet_feed):
        self.mess=0
        self.food=0
class Jod:
    def __init__(self,job_list):
        self.job=random.choice((list)(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]
    job_list = {
        "Java developer":{"salary":50,"gladness_less":10},
        "Python developer":{"salary":40,"gladness_less":3},
        "C++ developer":{"salary":45,"gladness_less":25},
        "Rust developer":{"salary":70,"gladness_less":1}}
nick=Human(name="Nick")
for day in range(1,8):
    if nick.live(day)==False:
        break