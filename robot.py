import turtle

class SkidBot():


    def __init__(self):
        self.width = 30
        self.height = 50
        self.scale = .10
        self.units = "CENTIMETERS"


    def hellow_world(self):
        print(f"{self.width}, {self.height}, {self.units}")


    def turtle_demo(self):
        turtle.speed(1)
        turtle.shape("square")
        turtle.shapesize(self.width * self.scale, self.height * self.scale)
        turtle.screensize(1000, 1000)

        self.move_pattern_1()

        turtle.done()

    def move_pattern_1(self):
        for i in range(0,5):
            turtle.forward(50)
            turtle.right(45)
            turtle.forward(20)
            turtle.right(45)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(200)
            turtle.right(45)
            turtle.forward(20)
            turtle.right(45)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(200)
