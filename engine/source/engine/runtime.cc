#include "include/engine/runtime.h"

#include <GLFW/glfw3.h>

#include <utility>

#include "include/engine/renderer.h"
#include "include/engine/window.h"

engine::Runtime::Runtime() {
  if (!glfwInit()) {
    // Initialization failed
    throw;
  }
}

std::unique_ptr<engine::Renderer> engine::Runtime::CreateRenderer(
    const Window &window) const {
  return std::make_unique<Renderer>(window);
}

std::unique_ptr<engine::Window> engine::Runtime::CreateWindow(
    std::string title, int width, int height) const {
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
  glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, true);
#endif

  auto windowHandle =
      glfwCreateWindow(width, height, title.c_str(), NULL, NULL);
  if (!windowHandle) {
    // Window or OpenGL context creation failed
    throw;
  }

  return std::make_unique<Window>(windowHandle);
}

void engine::Runtime::Poll() { glfwPollEvents(); }