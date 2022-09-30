# ---- Add dependencies via CPM ----

include(${CMAKE_CURRENT_LIST_DIR}/CPM.cmake)

# ---- Dependencies ----

# glad
CPMAddPackage(
  NAME glad
  GITHUB_REPOSITORY Dav1dde/glad
  VERSION 0.1.36
)

# glfw
CPMAddPackage(
  NAME glfw
  GITHUB_REPOSITORY glfw/glfw
  GIT_TAG 3.3.8
  OPTIONS
	  "GLFW_BUILD_TESTS OFF"
	  "GLFW_BUILD_EXAMPLES OFF"
	  "GLFW_BUILD_DOCS OFF"
)

# glm
CPMAddPackage(
  NAME glm
  GITHUB_REPOSITORY g-truc/glm
  GIT_TAG 0.9.9.8
)

# OpenGL
# find_package(OpenGL REQUIRED)

# PyBind11
CPMAddPackage(
  NAME pybind11
  GITHUB_REPOSITORY pybind/pybind11
  VERSION 2.10.0
  OPTIONS
    "PYBIND11_TEST OFF"
)
