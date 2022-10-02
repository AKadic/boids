#!/usr/bin/env python3
import config
import numpy as np
import math


def flatten(l):
    return [item for sublist in l for item in sublist]


class Boid:
    def __init__(self, position):
        self.position = position

        self.velocity = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.maxSpeed = config.maxSpeed
        self.maxForce = config.maxForce

    def update(self, delta):
        force = self.seek(config.target)
        self.acceleration = self.acceleration + force

        # Update velocity
        self.velocity = self.velocity + self.acceleration
        # Limit speed
        self.velocity = np.clip(self.velocity, -self.maxSpeed, self.maxSpeed)
        self.velocity = self.velocity * delta
        # Update position
        self.position = self.position + self.velocity
        # Reset accelertion to 0 each cycle
        self.acceleration *= 0

    def draw(self, renderer):
        scale = 30

        model_matrix = np.identity(4)

        S = np.diag([1/scale, 1/scale, 1, 1])
        model_matrix = np.matmul(S, model_matrix)

        theta = math.atan2(-self.velocity[0], self.velocity[1])
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        model_matrix = np.matmul(R, model_matrix)

        T = np.identity(4)
        T[0][3] = self.position[0]
        T[1][3] = self.position[1]
        model_matrix = np.matmul(T, model_matrix)

        renderer.set_mat4(config.program, "model",
                          flatten(model_matrix.tolist()))
        renderer.draw_triangles(config.triangle, 3)

    def seek(self, target):
        desired = np.subtract(target, self.position)

        if np.linalg.norm(desired) == 0:
            return np.array([0, 0])

        # Scale to maximum speed
        normalized = desired / np.sqrt(np.sum(desired**2))
        desired = normalized * self.maxSpeed
        # Steering = Desired minus Velocity
        steering = desired - self.velocity
        steering = np.clip(steering, -self.maxForce, self.maxForce)

        return steering

    def wrap(self):
        if (self.position[0] > 1):
            self.position[0] = -1
        if (self.position[0] < -1):
            self.position[0] = 1
        if (self.position[1] > 1):
            self.position[1] = -1
        if (self.position[1] < -1):
            self.position[1] = 1
