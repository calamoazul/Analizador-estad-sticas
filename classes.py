class Quest:
    def __init__(self, case):
        self.case = case
        self.provinces = {}
    def get_provinces(self):
        return self.provinces
    def set_provinces(self, province):
        self.provinces[province] = Province(province)
    
class Province:
    def __init__(self, name):
        self.name = name
        self.cases = 0
        self.accumulated = 0
    def get_name(self):
        return self.name
    def get_cases(self):
        return self.cases
    def set_cases(self, num):
        self.cases += num
    def get_accumulated(self):
        return self.accumulated
    def set_accumulated(self, stadistic):
        self.accumulated += stadistic
    def get_total_cases(self):
        return self.cases + self.accumulated
    
class DataFileError(Exception):

    def __init__(self, file):
        self.file = file
    def __str__(self):
        return 'El archivo {} no se encuentra accesible'.format(self.file)
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    
    
          