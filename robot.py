import turtle
import numpy as np
import matplotlib.pyplot as plt

class SkidBot():


    def __init__(self):
        self.width = .30
        self.height = .50
        self.scale = .100
        self.units = "METERS"

        # PHYSICS INITS
        self.global_x = 0
        self.global_y = 0
        self.global_phi = 0
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta_time = .01
        self.x_path = [0]
        self.y_path = [0]
        self.phi_records = [0]

        # STATS
        self.x_velocities = []
        self.y_velocities = []
        self.delta_phi_records = []
        self.time_axis = list(range(0,13331))



    def set_global_x(self, v_left, v_right):
        delta_x = -np.multiply(np.divide(v_right + v_left, 2), np.sin(self.theta)) * self.delta_time
        self.x_velocities.append(delta_x)
        self.global_x += delta_x

    def set_global_y(self, v_left, v_right):
        delta_y = np.multiply(np.divide(v_right + v_left, 2), np.cos(self.theta)) * self.delta_time
        self.y_velocities.append(delta_y)
        self.global_y += delta_y

    def update_phi(self, v_left, v_right):
        delta_phi = np.divide(v_right - v_left, self.width) * self.delta_time
        self.delta_phi_records.append(delta_phi)
        self.theta += delta_phi
        self.phi_records.append(self.theta)

    def plot_stats(self):
        plt.plot(self.x_velocities, label="x velocity")
        plt.plot(self.y_velocities, label="y velocity")
        plt.plot(self.delta_phi_records, label="angular change")
        plt.legend()
        plt.show()



    def set_theta(self, v_left, v_right):
        self.theta = np.divide(v_right - v_left, self.width)

    def get_global_pos(self):
        return (self.global_x, self.global_y)

    def calculate_turn(self, radius, phi):
        return phi*(radius - self.width/2), phi*(radius + self.width/2)

    def move_forward(self, meters, velocity):
        for i_1 in range(meters):
            for j_2 in range(100):
                self.update_phi(velocity,velocity)
                self.set_global_x(velocity, velocity)
                self.set_global_y(velocity, velocity)
                print(f"x: {self.global_x}, y: {self.global_y}")
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)

    def turn_right(self, radius, final_heading):
        v_left, v_right = self.calculate_turn(radius, final_heading)
        print(f"v_left: {v_left}, v_right: {v_right}")
        for i_1 in range(1):
            for j_2 in range(100):
                self.update_phi(v_right, v_left)
                self.set_global_x(v_right, v_left)
                self.set_global_y(v_right, v_left)
                print(f"x: {self.global_x}, y: {self.global_y}")
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)


    def turn_left(self, radius, final_heading):
        v_left, v_right = self.calculate_turn(radius, final_heading)
        print(f"v_left: {v_left}, v_right: {v_right}")
        for i_1 in range(1):
            for j_2 in range(100):
                self.update_phi(v_left, v_right)
                self.set_global_x(v_left, v_right)
                self.set_global_y(v_left, v_right)
                print(f"x: {self.global_x}, y: {self.global_y}")
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)


    def turn_left_in_place(self):
        v_left, v_right = self.calculate_turn(0, np.pi / 2)
        for i in range(100):

            self.update_phi(v_left, v_right)
            self.set_global_x(v_left, v_right)
            self.set_global_y(v_left, v_right)
            print(f"x: {self.global_x}, y: {self.global_y}")
            self.x_path.append(self.global_x)
            self.y_path.append(self.global_y)
        print(f"PHI: {self.theta}")


    def turn_right_in_place(self):
        v_left, v_right = self.calculate_turn(0, np.pi / 2)
        for i in range(100):

            self.update_phi(v_right, v_left)
            self.set_global_x(v_right, v_left)
            self.set_global_y(v_right, v_left)
            print(f"x: {self.global_x}, y: {self.global_y}")
            self.x_path.append(self.global_x)
            self.y_path.append(self.global_y)
        print(f"PHI: {self.theta}")


    def reset_to_start(self):
        # PHYSICS INITS
        self.global_x = 0
        self.global_y = 0
        self.global_phi = 0
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta_time = .01

    def path_1(self):
        self.x_path = [0]
        self.y_path = [0]
        for i in range(5):
            for j in range(100):
                self.update_phi(1,1.5)
                self.set_global_x(1, 1.5)
                self.set_global_y(1, 1.5)
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)


        for i_1 in range(3):
            for j_2 in range(100):
                self.update_phi(-1,-1.5)
                self.set_global_x(-1, -1.5)
                self.set_global_y(-1, -1.5)
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)



        for i_1 in range(8):
            for j_2 in range(100):
                self.update_phi(.8,-2)
                self.set_global_x(.8, -2)
                self.set_global_y(.8, -2)
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)



        for i_1 in range(10):
            for j_2 in range(100):
                self.update_phi(2,2)
                self.set_global_x(2, 2)
                self.set_global_y(2, 2)
                self.x_path.append(self.global_x)
                self.y_path.append(self.global_y)

        self.pyplot_plot()


    def path_2(self):
        '''
        Covers a 5x5 m square
        '''

        self.theta = 0
        # motion paths

        for i in range(8):
            self.move_forward(5,1)
            self.turn_left_in_place()
            self.move_forward(1,.3)
            self.turn_left_in_place()

            self.move_forward(5,1)
            self.turn_right_in_place()
            self.move_forward(1,.3)
            self.turn_right_in_place()


        self.move_forward(5,1)

    def path_3(self):
        '''
        Assumes holonomic ability with swedish wheels. This means the bot can move anywhere without
        change in angle. Each wheel would need an independant motor.
        '''

        '''
        Covers a 5x5 m square
        '''

        self.theta = 0
        # motion paths

        for i in range(8):
            self.move_forward(5,1)
            self.turn_left_in_place()
            self.move_forward(1,.3)
            self.turn_left_in_place()

            self.move_forward(5,1)
            self.turn_right_in_place()
            self.move_forward(1,.3)
            self.turn_right_in_place()


        self.move_forward(5,1)
        self.delta_phi_records = np.zeros(len(self.x_velocities))

    def pyplot_plot(self):
        plt.plot(self.x_path, self.y_path)
        plt.show()


    def turtlefy(self):

        turtle.tracer(1,1)
        turtle.mode("logo")
        i = 0
        scale = 70
        y_offset = 0
        turtle.speed(0)

        for x in self.x_path:
            turtle.goto(x * scale, (self.y_path[i] * scale) - y_offset)
            turtle.setheading(-self.phi_records[i] * (180/np.pi))
            i += 1

        turtle.done()
