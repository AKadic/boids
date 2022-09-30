#pragma once

#ifndef ENGINE_WINDOW_H
#define ENGINE_WINDOW_H

class GLFWwindow;

namespace engine {
class Window {
 public:
  Window(GLFWwindow *);

  bool Closed() const;
  void *ProcAddress() const;
  void Present();

 private:
  GLFWwindow *m_handle;
};
}  // namespace engine

#endif  // !ENGINE_WINDOW_H