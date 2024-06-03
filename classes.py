class RestorationOrder:
    def __init__(self, cost, order_date):
        self.cost = cost
        self.order_date = order_date

class Workshop:
    def __init__(self, load):
        self.load = load

class Material:
    def __init__(self, material_type):
        self.material_type = material_type

class Furniture:
    def __init__(self, condition, material):
        self.condition = condition
        self.material = material

class Category:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, registration_data):
        self.registration_data = registration_data