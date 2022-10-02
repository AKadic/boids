#include "include/engine/runtime.h"

#include <GLFW/glfw3.h>

#include <utility>

#include "include/engine/input.h"
#include "include/engine/renderer.h"
#include "include/engine/window.h"

glm::vec2 ndcToScreen(GLFWwindow* window, glm::vec2 ndc) {
  int width, height;
  glfwGetWindowSize(window, &width, &height);

  auto x = (ndc.x + 1.0f) * 0.5f * width;
  auto y = (1.0f - ndc.y) * height * 0.5f;

  return glm::vec2(x, y);
}

glm::vec2 screenToNdc(GLFWwindow* window, glm::vec2 screen) {
  int width, height;
  glfwGetWindowSize(window, &width, &height);

  auto x = (screen.x * 2.0f / width) - 1.0f;
  auto y = ((height - screen.y) / height * 2.0f) - 1.0f;

  return glm::vec2(x, y);
}

void engine::HandleClickEvent(Window& window, Input input) {
  input.mousePosition = screenToNdc(window.m_handle, input.mousePosition);

  for (auto& handler : window.m_onClickHandlers) {
    handler(input);
  }
}

void mouse_button_callback(GLFWwindow* window, int button, int action,
                           int mods) {
  const auto userWindow =
      static_cast<engine::Window*>(glfwGetWindowUserPointer(window));

  engine::Input input;

  double xpos, ypos;
  glfwGetCursorPos(window, &xpos, &ypos);

  input.mousePosition.x = (float)xpos;
  input.mousePosition.y = (float)ypos;

  if (button == GLFW_MOUSE_BUTTON_LEFT && action == GLFW_PRESS) {
    engine::HandleClickEvent(*userWindow, input);
  }
}

engine::Runtime::Runtime() {
  if (!glfwInit()) {
    // Initialization failed
    throw;
  }
}

std::unique_ptr<engine::Renderer> engine::Runtime::CreateRenderer(
    const Window& window) const {
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

  glfwSetMouseButtonCallback(windowHandle, mouse_button_callback);

  auto window = std::make_unique<Window>(windowHandle);

  glfwSetWindowUserPointer(windowHandle, window.get());

  return window;
}

void engine::Runtime::Poll() { glfwPollEvents(); }