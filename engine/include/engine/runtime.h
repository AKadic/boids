#pragma once

#ifndef ENGINE_RUNTIME_H
#define ENGINE_RUNTIME_H

#include <memory>
#include <string>

namespace engine {
class Renderer;
class Window;

class Runtime {
 public:
  Runtime();

  std::unique_ptr<Renderer> CreateRenderer(const Window &) const;
  std::unique_ptr<Window> CreateWindow(std::string title, int width,
                                       int height) const;

  void Poll();
};
}  // namespace engine

#endif  // !ENGINE_RUNTIME_H