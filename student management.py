class student:
    def __init__(self,rollnum, name, english, math, chemistry , phone_number):
        self.rollnum = rollnum
        self.name = name
        self.english = english
        self.math = math
        self.chemistry = chemistry
        self.phone_number = phone_number



    def get_rollnum(self):
        return self.rollnum
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def set_english(self,english):
        self.english = english
    def set_math(self,math):
        self.math = math
    def set_chemistry(self,chemistry):
        self.chemistry = chemistry
    def set_phone_number(self,phone_number):
        self.phone_number = phone_number

    def Eget_mark(self):
        return self.english
    def Mget_mark(self):
        return self.math
    def cget_mark(self):
        return self.chemistry



    def getphone(self):
        return self.phone_number


    def show(self):
        print("-------STUDENT MANAGEMENT------")
        print("Roll num: ",self.rollnum)
        print("Name: ", self.name)
        print("English: ", self.english)
        print("Math: ", self.math)
        print("Chemistry: ", self.chemistry)
        print("Phone number: ",self.phone_number)
        print("--------------")
