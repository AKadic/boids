#!/usr/bin/env python3
vertices = [
    -1, -1, 0,
    1, -1, 0,
    0,  1, 0
]

vertexShaderSource = """
#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos, 1.0);
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
