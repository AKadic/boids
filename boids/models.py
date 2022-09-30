#!/usr/bin/env python3
import config
import numpy as np


def flatten(l):
    return [item for sublist in l for item in sublist]


class Boid:
    def __init__(self, position):
        self.position = position

        self.velocity = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.maxSpeed = 2
        self.maxForce = 0.5

    def update(self, delta):
        force = self.seek(np.array([-0.8, 0.8]))
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

        scale_matrix = np.diag([1/scale, 1/scale, 1, 1])
        model_matrix = np.matmul(scale_matrix, model_matrix)

        translation_matrix = np.identity(4)
        translation_matrix[0][3] = self.position[0]
        translation_matrix[1][3] = self.position[1]
        model_matrix = np.matmul(translation_matrix, model_matrix)

        renderer.set_mat4(config.program, "model",
                          flatten(model_matrix.tolist()))
        renderer.draw_triangles(config.triangle, 3)

    def seek(self, target):
        desired = np.subtract(target, self.position)
        # Scale to maximum speed
        normalized = desired / np.sqrt(np.sum(desired**2))
        desired = np.multiply(normalized, self.maxSpeed)
        # Steering = Desired minus Velocity
        steering = np.subtract(desired, self.velocity)
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
