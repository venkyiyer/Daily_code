class Main:

    country = 'Indian'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        return cls.country
    
    @staticmethod
    def just_checking():
        return 'I am Venkatesh Iyer' 

    class Sub_class: 

        def __init__(self, ram, processor, cost):
            self.ram = ram
            self.processor = processor
            self.cost = cost    

        def give_information(self):
            return self.ram, self.processor, self.cost
    
s1 = Main('VeMkatesh', 29, 'Male')
s2 = Main('Radha', 26, 'Female')


s3 = Main.Sub_class(16, 'i5', 1)
print(s3.give_information())


#print(Main.change_country('Germany'))
#print(Main.just_checking())
