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
        self.global_phi = 0
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta_time = .10



    def set_global_x(self, v_left, v_right):
        self.global_x += -np.multiply(np.divide(v_right + v_left, 2), np.sin(self.theta)) * self.delta_time

    def set_global_y(self, v_left, v_right):
        self.global_y += np.multiply(np.divide(v_right + v_left, 2), np.cos(self.theta)) * self.delta_time

    def update_phi(self, v_left, v_right):
        self.theta += np.divide(v_right - v_left, self.width) * self.delta_time

    def set_theta(self, v_left, v_right):
        self.theta = np.divide(v_right - v_left, self.width)

    def get_global_pos(self):
        return (self.global_x, self.global_y)

    def reset_to_start(self):
        # PHYSICS INITS
        self.global_x = 0
        self.global_y = 0
        self.global_phi = 0
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta_time = .10

    def path_1(self):
        x_path = [0]
        y_path = [0]
        for i in range(5):
            for j in range(10):
                self.update_phi(1,1.5)
                self.set_global_x(1, 1.5)
                self.set_global_y(1, 1.5)
                x_path.append(self.global_x)
                y_path.append(self.global_y)


        for i_1 in range(3):
            for j_2 in range(10):
                self.update_phi(-1,-1.5)
                self.set_global_x(-1, -1.5)
                self.set_global_y(-1, -1.5)
                x_path.append(self.global_x)
                y_path.append(self.global_y)



        for i_1 in range(8):
            for j_2 in range(10):
                self.update_phi(.8,-2)
                self.set_global_x(.8, -2)
                self.set_global_y(.8, -2)
                x_path.append(self.global_x)
                y_path.append(self.global_y)



        for i_1 in range(10):
            for j_2 in range(10):
                self.update_phi(2,2)
                self.set_global_x(2, 2)
                self.set_global_y(2, 2)
                x_path.append(self.global_x)
                y_path.append(self.global_y)

        plt.plot(x_path, y_path)
        plt.show()


    def path_2(self):
        '''
        Draws a 5x5 m square
        '''

        #assume our initial heading is facing right
        self.theta = 0
        # motion paths
        x_path = [0]
        y_path = [0]

        for i in range(1):
            for j in range(10):
                self.update_phi(-1,1)
                self.set_global_x(-1,1)
                self.set_global_y(-1, 1)
                x_path.append(self.global_x)
                y_path.append(self.global_y)

        for i in range(1):
            for j in range(10):
                self.update_phi(1,1)
                self.set_global_x(1,1)
                self.set_global_y(1, 1)
                x_path.append(self.global_x)
                y_path.append(self.global_y)
        print(f"THETA: {self.theta}")
        plt.plot(x_path, y_path)
        plt.show()
