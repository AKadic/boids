#!/usr/bin/env python3
import engine
import time
import numpy as np
import config
from models import Boid


def on_click(input):
    config.target = input.mouse_position


def draw_boids(renderer):
    for boid in config.boids:
        boid.draw(renderer)


def update_boids(delta):
    for boid in config.boids:
        boid.update(delta)
        boid.wrap()


if __name__ == "__main__":
    runtime = engine.create_runtime()
    window = runtime.create_window("Boids", 640, 480)
    renderer = runtime.create_renderer(window)

    config.program = renderer.compile_shaders(
        config.vertexShaderSource,
        config.fragmentShaderSource)
    config.triangle = renderer.create_vertex_object(config.vertices)

    renderer.use_program(config.program)

    config.boids.append(Boid(
        position=np.array([0, 0])))

    target_fps = 60
    prev_time = time.time()
    sum = 0
    count = 0

    window.on_click(on_click)

    while not window.closed:
        curr_time = time.time()
        delta = curr_time - prev_time
        sum += delta
        count += 1
        if sum >= 1:
            print("FPS: ", count)
            sum = 0
            count = 0

        # Poll
        runtime.poll()
        # Update
        update_boids(delta)
        # Draw
        renderer.clear(0, 0, 0, 1)
        draw_boids(renderer)
        window.present()

        delay = max(1.0/target_fps - delta, 0)
        time.sleep(delay)
        fps = 1.0/(delay + delta)
        prev_time = curr_time
