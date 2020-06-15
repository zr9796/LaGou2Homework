import yaml

class Animal:
    name = ''
    color = ''
    age = 0
    sex = ''

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print("{} is running".format(self.name))
    
    def yell(self):
        print("{} is yelling".format(self.name))

class Cat(Animal):
    hair = 'short'
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def CatchMouse(self):
        print("The cat {} is catching mouse".format(self.name))
    
    def yell(self):
        print("{} is miaomiaomiao".format(self.name))

class Dog(Animal):
    hair = 'long'
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        
    def HouseKeeping(self):
        print("The Dog {} is keeping house".format(self.name))
    
    def yell(self):
        print("{} is wangwangwang".format(self.name))
    


if __name__ == "__main__":

    with open('./test.yml', 'r') as f:
        data = yaml.safe_load(f)
        a = Cat(data[0]['name'], data[0]['color'], data[0]['age'], data[0]['sex'])
        a.CatchMouse()
        print(a.name, a.color, a.age, a.sex, a.hair, "捉到了老鼠")

        print()

        b = Dog(data[1]['name'], data[1]['color'], data[1]['age'], data[1]['sex'])
        b.HouseKeeping()
        print(b.name, b.color, b.age, b.sex, b.hair)