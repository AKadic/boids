#!/usr/bin/env python3
vertices = [
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0,  0.5, 0.0
]

vertexShaderSource = """
#version 330 core
layout (location = 0) in vec3 aPos;

uniform mat4 model;

void main()
{
    gl_Position = model * vec4(aPos, 1.0);
}
"""

fragmentShaderSource = """
#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.0f, 1.0f, 1.0f);
} 
"""

program = None
vertexObject = None
boids = []


class Boid:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
