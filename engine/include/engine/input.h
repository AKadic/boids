#pragma once

#ifndef ENGINE_INPUT_H
#define ENGINE_INPUT_H

#include <glm/glm.hpp>
#include <vector>

namespace engine {
struct Input {
  glm::vec2 mousePosition;

  std::vector<float> GetMousePosition() {
    return {mousePosition.x, mousePosition.y};
  }
};
}  // namespace engine

#endif  // !ENGINE_INPUT_H