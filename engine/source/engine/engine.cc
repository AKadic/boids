#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <memory>
#include <utility>

#include "include/engine/renderer.h"
#include "include/engine/runtime.h"
#include "include/engine/window.h"

namespace py = pybind11;
using namespace py::literals;

std::unique_ptr<engine::Runtime> create_runtime() {
  return std::make_unique<engine::Runtime>();
}

PYBIND11_MODULE(engine, m) {
  py::class_<engine::Renderer>(m, "PyRenderer")
      .def("clear", &engine::Renderer::Clear)
      .def("create_vertex_object", &engine::Renderer::CreateVertexObject)
      .def("compile_shaders", &engine::Renderer::CompileShaders)
      .def("draw_triangles", &engine::Renderer::DrawTriangles)
      .def("set_mat4", &engine::Renderer::SetMat4)
      .def("use_program", &engine::Renderer::UseProgram);

  py::class_<engine::Window>(m, "PyWindow")
      .def_property_readonly("closed", &engine::Window::Closed)
      .def("present", &engine::Window::Present);

  py::class_<engine::Runtime>(m, "PyRuntime")
      .def("create_renderer", &engine::Runtime::CreateRenderer)
      .def("create_window", &engine::Runtime::CreateWindow)
      .def("poll", &engine::Runtime::Poll);

  m.def("create_runtime", &create_runtime);
}