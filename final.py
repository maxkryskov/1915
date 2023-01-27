import random
class Human:
    def __init__(self, name="Human", job=None,home = None, perents=None):
        self.name = name
        self.job= job
        self.home = home
        self.perents = perents
        self.money = 100
        self.gladness = 50
    def get_home(self):
        self.home=House()

    def get_job(self):
        if self.study.school():
            pass
        else:
            self.to_repair()
            return
        self.job=Job()
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
        if self.study.school():
            pass
        else:
                return
        self.money+=0
        self.gladness+=5
        self.satiety-=5

        def shopping(self,manage):
            if self.walk():
                pass
            else:
                if self.walk.happu<+0:

                    if manage=="fuel":
                        self.fuel+=10
                        self.money-=10
                elif manage=="deliciuos":
                    print("Ура! Смаколики!")
                    self.money-=15
                    self.gladness+=10
                    self.satiety+=2

    def chill(self):
        self.gladness+=10
        self.home.mess+=5

    def clean_home(self):
        self.gladness-=10
        self.home.mess=0

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

    def is_alive(self):
        if self.gladness<=0:
            print("Дипресія")
            return False
        if self.satiety<0:
            print("Голод")
            return False
        if self.money<-0:
            print("погана оцінка")
            return  False

    def live(self, day):

        if self.job is None:
            self.get_job()
            print(f"в мене погана оцінка піду вчити матеріал{self.job.work}з зарплатою {self.job.work}")
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
            print("я іду в школу")
            self.work()
        elif self.car.strenght<15:
             print("мені потрібно підтянути оцінки")
             self.work()
        elif dece==1:
             print("давайте відпочинемо")
             self.chill()
        elif dece==2:
             print("початок навчання")
             self.work()
        elif dece==3:
             print("час прибирання")
             self.clean_home()
        elif dece==4:
             print("час смачненького")
             self.shopping(manage="delicacies")


class House:
    def __init__(self):
        self.mess=0
        self.food=30
class Job:
    def __init__(self,job_list):
        self.job=random.choice((list)(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]
    job_list = {
        "study in school":{"salary":50,"gladness_less":10},
        "help perents":{"salary":40,"gladness_less":3},}
nick=Human(name="Nick")
for day in range(1,8):
    if nick.live(day)==False:
        break