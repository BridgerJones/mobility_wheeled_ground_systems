import turtle
import numpy as np
import matplotlib.pyplot as plt

class SkidBot():


    def __init__(self):
        self.width = .30
        self.height = .50
        self.scale = .10
        self.units = "METERS"

        # PHYSICS INITS
        self.global_x = 0
        self.global_y = 0


    def set_global_x(self, v_left, v_right):
        self.global_x += -np.multiply(np.divide(v_right + v_left, 2), np.sin(self.get_phi(v_left, v_right)))

    def set_global_y(self, v_left, v_right):
        self.global_y += np.multiply(np.divide(v_right + v_left, 2), np.cos(self.get_phi(v_left, v_right)))

    def get_phi(self, v_left, v_right):
        return np.multiply(np.divide(v_right - v_left, self.width), np.divide(np.pi, 180))

    def get_global_pos(self):
        return (self.global_x, self.global_y)

    def path_1(self):
        x_path = [0]
        y_path = [0]
        for i in range(5):
            self.set_global_x(1, 1.5)
            self.set_global_y(1, 1.5)
            x_path.append(self.global_x)
            y_path.append(self.global_y)

        for i in range(3):
            self.set_global_x(-1, -1.5)
            self.set_global_y(-1, -1.5)
            x_path.append(self.global_x)
            y_path.append(self.global_y)

        for i in range(8):
            self.set_global_x(.8, -2)
            self.set_global_y(.8, -2)
            x_path.append(self.global_x)
            y_path.append(self.global_y)

        for i in range(10):
            self.set_global_x(2, 2)
            self.set_global_y(2, 2)
            x_path.append(self.global_x)
            y_path.append(self.global_y)

        plt.plot(x_path, y_path)
        plt.show()


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
