class category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent

    def hd_display_name(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.hd_display_name()} > {self.name}"

    def __str__(self):
        return self.hd_display_name()

    def csort():
        for i in range(0, len(categories)):
            for j in range(i + 1, len(categories)):
                if categories[i].name > categories[j].name:
                    temp = categories[i]
                    categories[i] = categories[j]
                    categories[j] = temp
        for cat in categories:
            print(cat.name, cat.code, cat.hd_display_name())
            for pro in products:
                if cat.name == pro.category.name:
                    print(pro.name, pro.code, pro.price, pro.category.hd_display_name())

            print("\n")

class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price


    def __str__(self):
        return f"Product: {self.name} , Code: {self.code} , Category: {self.category.hd_display_name()} , Price: {self.price}"


vehicle = category("Vehicle", "V001")
car = category("Car", "C001", parent=vehicle)
petrol = category("Petrol", "P001", parent=car)
od = category("Od", "d001", parent=petrol)
hd = category("Hd","doo1",parent=od)

# Assemble the categories into a list
categories = [vehicle, car, petrol, od , hd]

products = [
    product("cycle", 1, vehicle, 1500),
    product("bike", 2, vehicle, 1800),
    product("truck", 2, vehicle, 1800),
    product("shell", 3, petrol, 9000),
    product("reliance", 4, petrol, 6000),
    product("oddd", 2, petrol, 1800),
    product("merci", 5, car, 7500),
    product("volvo", 6, car, 10500),
    product("kia", 6, car, 10500),
    product("fila", 10, od, 800),
    product("nike", 10, od, 800),
    product("pau", 10, od, 800),
    product("fsgfs",11,hd,346),
    product("gkdo",11,hd,346),
    product("lpsd",11,hd,346)
]

category.csort()





