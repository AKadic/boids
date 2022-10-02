#pragma once

#ifndef ENGINE_WINDOW_H
#define ENGINE_WINDOW_H

#include <functional>
#include <vector>

#include "include/engine/runtime.h"

struct GLFWwindow;

namespace engine {
struct Input;

typedef std::function<void(const Input &)> OnClickHandler;

class Window {
 public:
  Window(GLFWwindow *);

  bool Closed() const;
  void *ProcAddress() const;
  void Present();
  void OnClick(OnClickHandler);

 private:
  GLFWwindow *m_handle;
  std::vector<OnClickHandler> m_onClickHandlers;

  friend void HandleClickEvent(Window &window, Input);
};
}  // namespace engine

#endif  // !ENGINE_WINDOW_H