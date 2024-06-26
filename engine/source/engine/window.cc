#include "include/engine/window.h"

#include <GLFW/glfw3.h>

#include "include/engine/input.h"

engine::Window::Window(GLFWwindow *handle) : m_handle{handle} {}

bool engine::Window::Closed() const { return glfwWindowShouldClose(m_handle); }

void *engine::Window::ProcAddress() const {
  glfwMakeContextCurrent(m_handle);

  return (void *)glfwGetProcAddress;
}

void engine::Window::Present() { glfwSwapBuffers(m_handle); }

void engine::Window::OnClick(OnClickHandler handler) {
  m_onClickHandlers.push_back(handler);
}