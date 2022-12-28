# In this video we will talk about

# Encapsulation

# Abstraction

# Some special naming convention

# Name Mangling , __name (not a convention)

class Phone:
    def init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")

 

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def send_mesaage(self):
        pass # twilio

phone1 = Phone( 'nokia', '1100',1000)
# print(phonel.__price)
print(phone1._phone_price)
phone1._phone__price=-1000
print(phone1._phone__price)
# print(phone1.__dict__)
# phonel._price = -1000 
# print(phone._price)