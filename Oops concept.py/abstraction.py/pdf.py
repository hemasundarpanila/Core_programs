'''12. Design an abstract class PaymentGateway with: 
• authenticate() 
• pay(amount) 
• refund(amount) 
Implement subclasses: 
• UPIPayment 
• CardPayment 
• NetBankingPayment 
Show how abstraction helps your main program call payment methods without caring about 
the payment type.

'''
# from abc import ABC,abstractmethod
# class paymentgateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         print("hii")
#     @abstractmethod
#     def pay(self,amount):
#         print("hii")
#     @abstractmethod
#     def refund(self,amount):
#         print("hii")
# # s=paymentgateway()
# # s.pay(100)        
# class upipayment(paymentgateway):
#     def authenticate(self):
#         print("upipayment authentication")
#     def pay(self,amount):
#         print("upipayment:",amount)
#     def refund(self,amount):
#         print("refund amount:",amount)
# class cardpayment(paymentgateway):
#     def authenticate(self):
#         print("cardpayment authentication")
#     def pay(self,amount):
#         print("cardpayment:",amount)
#     def refund(self,amount):
#         print("refund amount:",amount)
# class netbanking(paymentgateway):
#     def authenticate(self):
#         print("netbanking payment authentication")
#     def pay(self,amount):
#         print("net banking payment:",amount)
#     def refund(self,amount):
#         print("refund amount:",amount)
# u=upipayment()
# c=cardpayment()
# n=netbanking()
# c.authenticate()
# c.pay(1000)
# c.refund(200)


'''13. Create: 
• Abstract class VehicleControl with methods accelerate(), brake(), steer() 
• Implement CarControl, BikeControl, TruckControl 
Demonstrate calling each through a single interface. 

'''

# from abc import ABC,abstractmethod
# class vehiclecontrol:
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class car_control(vehiclecontrol):
#     def accelerate(self):
#         print("car accelerate")
#     def br(self):
#         print("car brake")
#     def steer(self):
#         print("car steer")
# class bike_control(vehiclecontrol):
#     def accelerate(self):
#         print("bike accelerate")
#     def brake(self):
#         print("bike brake")
#     def steer(self):
#         print("bike steer")
# c=car_control()
# c.accelerate()
# c.br()
# c.steer()

'''17. Create an abstract class MLModel with: 
• train(data) 
• predict(x) 
• evaluate(test_set) 
Implement models: 
• LinearRegressionModel- some different logic 
• DecisionTreeModel – some logic 
Show how a generic training loop works for any model without caring about details. '''

# from abc import ABC,abstractmethod
# class mlmodel(ABC):
#     @abstractmethod
#     def train(self):
#         pass
#     @abstractmethod
#     def predict(self,data):
#         pass
#     @abstractmethod
#     def evaluate(self,test_set):
#         pass
# class linearmodel(mlmodel):
#     def train(self):
#         print("linearmodel train")
#     def predict(self,data):
#         print("linear predict")
#         return data*2
#     def evaluate(self,data):
#         print("leanear evaluate")
# class decision(mlmodel):
#     def train(self):
#         print("decisionmodel train")
#     def predict(self,data):
#         print("decision predict")
#         return "class A"
#     def evaluate(self,data):
#         print("decision evaluate")
# def models(model,data,set):
#     model.train()
#     predict=model.predict(data)
#     model.evaluate(set)
#     print("prediction:",predict)
# s1=linearmodel()
# s2=decision()

# models(s1,[1,2,3],[4,5])
# print("-"*12)
# models(s2,[1,2,3],[4,5])


# 18. Design a system without abstraction first: 
# • Write separate functions for EmailSender, SMSSender, PushSender 
# Show how the main program becomes a mess with constant if/else. 
# Then: 
# • Redesign using an abstract base class Notifier.


# def emailsender(messege):
#     print("email messege:",messege)
# def smssender(messege):
#     print("sms messege:",messege)
# def pushsender(messege):
#     print("push messege:",messege)
# nf_type=input("enter:")
# messege=input("enter:")
# if nf_type=="emailsender":
#     emailsender(messege)
# elif nf_type=="smssender":
#     smssender(messege)
# elif nf_type=="pushsender":
#     pushsender(messege)
# else:
#     print("invalid type")


# from abc import ABC,abstractmethod
# class notification(ABC):
#     @abstractmethod
#     def send(self,messege):
#         pass
# class email_messege(notification):
#     def send(self,messege):
#         print("email messege:",messege)
# class sms_messege(notification):
#     def send(self,messege):
#         print("sms messege:",messege)
# class push_messege(notification):
#     def send(self,messege):
#         print("push messege:",messege)
# def notify(method,messege):
#     method.send(messege)
# s1=email_messege()
# s2=sms_messege()
# s3=push_messege()
# notify(s1,"happy dasara")
# notify(s2,"happy birthday")
# notify(s3,"happy new year")


'''19. Create an abstract MediaPlayer with: 
• load() 
• play() 
• stop() 
Implement: 
• MP3Player 
• WAVPlayer 
• AACPlayer 
Demonstrate calling each via a unified interface. 
'''

# from abc import ABC,abstractmethod
# class mediaplayer(ABC):
#     @abstractmethod
#     def load(self):
#         pass
#     @abstractmethod
#     def play(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass


'''20. Design: 
• Abstract base class Sensor with functions read_value() and calibrate() 
• Subclasses: TemperatureSensor, PressureSensor, HumiditySensor 
Encapsulate: 
• internal raw sensor readings 
• calibration factor 
Hide all raw operations and allow only a public, clean get_reading() method.'''

from abc import ABC,abstractmethod
class sensor(ABC):
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
class temperature(sensor):
    def __init__(self,raw):
        self.raw=raw
        self.calibration=1.5
    def read_value(self):
        print("read value:",self.raw)
    def calibrate(self):
        print("calibrate value:",self.calibration)
    def get_reading(self):
        self.raw=self.raw*self.calibration
        print("get reading:",self.raw)
s1=temperature(22)
s1.read_value()
s1.calibrate()
s1.get_reading()

    
