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
        self.global_x += -np.multiply(np.divide(v_right + v_left, 2), np.sin(self.get_phi(v_left, v_right)))

    def set_global_y(self, v_left, v_right):
        self.global_y += np.multiply(np.divide(v_right + v_left, 2), np.cos(self.get_phi(v_left, v_right)))

    def get_phi(self, v_left, v_right):
        return np.multiply(np.divide(v_right - v_left, self.width), np.divide(np.pi, 180))

    def get_global_pos(self):
        return (self.global_x, self.global_y)
