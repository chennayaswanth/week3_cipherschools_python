# can we derive more than one class from base class ?
# multilevel inheritance

# method resolution order

# method overriding

# isinstpnce(), issubclass()

class Phone: # base class / parent class
    def _init_(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self ._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}...."

class Smartphone(Phone): # derived / child class
    def _init_(self, brand,model_name, price, ram, internal_memory, rear_camera):
        #two ways
        # Phone.__init__(self, brand, model_name,price) # uncommon way
        super().__init__(brand,model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init_(self, brand,model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand,model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front_camera={self.front_camera}"
   
# phone = Phone( ‘noki
oneplus5 = Smartphone('onePlus','5',30000,'6GB','4G', '20MP')
oneplus5t = FlagshipPhone( 'onePlus','5t',30000,'6GB', '64GB', '20 MP', '16MP')
# print(oneplus.full_name())

# print(help(FlagshipPhone) )

# isinstance

# print(isinstance(oneplusS, FlagshipPhone))

# print(isinstance(oneplusst,Phone))

#print(issubclass(FlagshipPhone, Smartphone)

  