import random
class Student:
    print('hello teacher')
    self.money = 200

    def __init__(self):
        self.height = 168
        self.age = 22


student_vika = Student()
print(student_vika.height)
print(student_vika.age)


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 40
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.20
        self.gladness -= 8
        self.money += 4

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 4

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.25
        self.money -= 15

    def is_alive(self):
        if self.progress < -0.8:
            print("Cast out…")
            self.alive = False
            self.to_study()
            self.gladness = 0
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 6: \
                print("Passed externally…")
        self.alive = False
        self.to_chill


def end_of_day(self):
    print("Gladness = {self.gladness}")
    print(f"Progress ={round(self.progress, 9)}")


def live(self, day):
    day = "Day" + str(day) + "of" + \
          self.name + "life"
    print(f"{day:=^50}")
    live_cube = random.randint(2, 4)


if live_cube == 3:
    self.to_sleep
elif live_cube == 6: \
        self.to_sleep()
elif live_cube == 5:
    self.to_chill()
    self.end_of_day()
    self.is_alive()
    vika = Student(name="vika")
for day in range(375):
    if vika.alive == False:
        break
    vika.live(day)