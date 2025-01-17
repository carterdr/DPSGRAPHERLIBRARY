import numpy
from Libraries import Excel, Database
from Libraries.config import print_when_adding

class DamageResult():
    def __init__(self, name = "", dot = None, last_time = 0, category = None):
        self.name = name
        self.dot = dot if dot is not None else numpy.zeros(1001, dtype=int)
        self.last_time = last_time
        self.category = category
    def add(self, second):
        if second.name != "":
            if self.name == "":
                self.name = second.name
            else:
                self.name += " + " + second.name
        self.dot += second.dot
        if second.last_time > self.last_time:
            self.last_time = second.last_time
        if self.category != None:
            self.category = "mw"
        if print_when_adding:
            Excel.print_to_sheet(self)
        return self
    def __str__(self):
        return f"name: {self.name}\nlast time:{self.last_time}\ndot:{self.dot}\ncategory:{self.category}"
    def __add__(self, second):
        if second.name != "":
            if self.name == "":
                name = second.name
            else:
                name = self.name + " + " + second.name
        else:
            name = self.name
        if second.last_time > self.last_time:
            last_time = second.last_time
        if self.category != None:
            category = "mw"
        output = DamageResult(dot = self.dot + second.dot, last_time = last_time, name = name, category= category)
        if print_when_adding:
            Excel.print_to_sheet(output)
        return output
    def save(self):
       Database.save_to_database(self, self.category)
    def save_custom(self, custom_name, custom_category):
        self.name = custom_name
        Database.save_to_database(self, custom_category)