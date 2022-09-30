#pragma once

#ifndef ENGINE_RENDERER_H
#define ENGINE_RENDERER_H

#include <string>
#include <vector>

namespace engine {
class Window;

class Renderer {
 public:
  Renderer(const Window &);

  void Clear(float r, float g, float b, float a);
  unsigned int CreateVertexObject(std::vector<float> vertices);
  unsigned int CompileShaders(std::string vertex, std::string fragment);
  void DrawTriangles(unsigned int vao, int n);
  void SetMat4(unsigned int program, const std::string &name,
               const std::vector<float> &matPtr);
  void UseProgram(unsigned int program);
};
}  // namespace engine

#endif  // !ENGINE_RENDERER_H