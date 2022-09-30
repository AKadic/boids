#!/usr/bin/env python3
import config
import engine
import numpy as np


def flatten(l):
    return [item for sublist in l for item in sublist]


def draw_boid(renderer, boid):
    model_matrix = np.identity(4)
    translation_matrix = np.identity(4)
    translation_matrix[0][3] = boid.position[0]
    translation_matrix[1][3] = boid.position[1]
    model_matrix = np.matmul(translation_matrix, model_matrix)

    renderer.set_mat4(config.program, "model", flatten(model_matrix.tolist()))
    renderer.draw_triangles(config.triangle, 3)


def draw_boids(renderer):
    for boid in config.boids:
        draw_boid(renderer, boid)


def update_boid(boid):
    boid.position = np.add(boid.position, boid.velocity)


def update_boids():
    for boid in config.boids:
        update_boid(boid)


if __name__ == "__main__":
    runtime = engine.create_runtime()
    window = runtime.create_window("Boids", 640, 480)
    renderer = runtime.create_renderer(window)

    config.program = renderer.compile_shaders(
        config.vertexShaderSource,
        config.fragmentShaderSource)
    config.triangle = renderer.create_vertex_object(config.vertices)

    renderer.use_program(config.program)

    config.boids.append(config.Boid(
        position=np.array([0, 0]),
        velocity=np.array([0.01, 0])))

    while not window.closed:
        # Poll
        runtime.poll()
        # Update
        update_boids()
        # Draw
        renderer.clear(0, 0, 0, 1)
        draw_boids(renderer)
        window.present()
