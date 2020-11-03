class Car(object):

    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating")

    def change_gear(self,gear_type):
        print("gear_changed")

lamborghini=Car("aventador v.2020","black","lamborghini",250)
print(lamborghini.start())
print(lamborghini.stop())
print(lamborghini.accelarate())
print(lamborghini.change_gear)
