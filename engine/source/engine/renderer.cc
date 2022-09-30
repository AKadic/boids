#include "include/engine/renderer.h"

#include <glad/glad.h>

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "include/engine/window.h"

engine::Renderer::Renderer(const Window &window) {
  if (!gladLoadGLLoader((GLADloadproc)window.ProcAddress())) {
    // Failed to initialize OpenGL context
    throw;
  }
}

void engine::Renderer::Clear(float r, float g, float b, float a) {
  glClearColor(r, g, b, a);
  glClear(GL_COLOR_BUFFER_BIT);
}

unsigned int engine::Renderer::CompileShaders(std::string vertex,
                                              std::string fragment) {
  int success;
  char infoLog[512];

  auto vertexSource = vertex.c_str();
  auto vertexShader = glCreateShader(GL_VERTEX_SHADER);
  glShaderSource(vertexShader, 1, &vertexSource, nullptr);
  glCompileShader(vertexShader);

  glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(vertexShader, 512, nullptr, infoLog);
    throw;
  }

  auto fragmentSource = fragment.c_str();
  auto fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
  glShaderSource(fragmentShader, 1, &fragmentSource, nullptr);
  glCompileShader(fragmentShader);

  glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(fragmentShader, 512, nullptr, infoLog);
    throw;
  }

  auto program = glCreateProgram();
  glAttachShader(program, vertexShader);
  glAttachShader(program, fragmentShader);
  glLinkProgram(program);

  glGetProgramiv(program, GL_LINK_STATUS, &success);
  if (!success) {
    glGetProgramInfoLog(program, 512, nullptr, infoLog);
    throw;
  }

  glDeleteShader(vertexShader);
  glDeleteShader(fragmentShader);

  return program;
}

void engine::Renderer::DrawTriangles(unsigned int vao, int n) {
  glBindVertexArray(vao);
  glDrawArrays(GL_TRIANGLES, 0, n);
}

void engine::Renderer::UseProgram(unsigned int program) {
  glUseProgram(program);
}

void engine::Renderer::SetMat4(unsigned int program, const std::string &name,
                               const std::vector<float> &matPtr) {
  glm::mat4 mat = glm::make_mat4(matPtr.data());
  mat = glm::transpose(mat);
  glUniformMatrix4fv(glGetUniformLocation(program, name.c_str()), 1, GL_FALSE,
                     &mat[0][0]);
}

unsigned int engine::Renderer::CreateVertexObject(std::vector<float> vertices) {
  unsigned int vbo, vao;

  glGenBuffers(1, &vbo);
  glBindBuffer(GL_ARRAY_BUFFER, vbo);
  glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(float), &vertices[0],
               GL_STATIC_DRAW);

  glGenVertexArrays(1, &vao);
  glBindVertexArray(vao);
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void *)0);
  glEnableVertexAttribArray(0);

  return vao;
}