#!/usr/bin/env python3
import engine
from example import config


def update():
    pass


def draw(renderer):
    renderer.draw_triangles(config.triangle, 3)


def on_click(input):
    print("Click!")
    pass


def main():
    runtime = engine.create_runtime()
    window = runtime.create_window("Example", 640, 480)
    renderer = runtime.create_renderer(window)

    config.program = renderer.compile_shaders(
        config.vertexShaderSource,
        config.fragmentShaderSource)
    config.triangle = renderer.create_vertex_object(config.vertices)

    renderer.use_program(config.program)

    window.on_click(on_click)

    while not window.closed:
        # Poll
        runtime.poll()
        # Update
        update()
        # Draw
        renderer.clear(0, 0, 0, 1)
        draw(renderer)
        window.present()


if __name__ == "__main__":
    main()
