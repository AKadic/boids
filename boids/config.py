#!/usr/bin/env python3
import numpy as np

vertices = [
    -1, -1, 0,
    1, -1, 0,
    0,  1, 0
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
target = np.array([0, 0])

maxSpeed = 3.5
maxForce = 0.5
