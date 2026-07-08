cmake_minimum_required(VERSION 3.16)

project(embedded_project_template
    VERSION 0.1.0
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(app
    src/app.cpp
)

target_include_directories(app PUBLIC
    include
)

add_executable(embedded_project_template
    src/main.cpp
)

target_link_libraries(embedded_project_template PRIVATE
    app
)

enable_testing()

add_executable(test_app
    tests/test_app.cpp
)

target_link_libraries(test_app PRIVATE
    app
)

add_test(NAME test_app COMMAND test_app)
