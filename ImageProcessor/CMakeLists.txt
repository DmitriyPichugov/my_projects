cmake_minimum_required(VERSION 3.10)
project(image_processor)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
cmake_policy(SET CMP0135 NEW)

enable_testing()

include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
FetchContent_MakeAvailable(googletest)

add_executable(
        image_processor
        image_processor.cpp
        src/image.cpp
        src/bmp_handler.cpp
        src/filters/grayscale.cpp
        src/filters/crop.cpp
        src/filters/glass.cpp
        src/filters/negative.cpp
        src/filters/sharpening.cpp
        src/filters/edge.cpp
        src/filters/blur.cpp
        src/filters/filter_factory.cpp
)

target_include_directories(image_processor PRIVATE include)

add_executable(
        image_test
        tests/image_test.cpp
        src/image.cpp
        src/filters/grayscale.cpp
        src/filters/crop.cpp
        src/filters/glass.cpp
        src/filters/negative.cpp
        src/filters/sharpening.cpp
        src/filters/edge.cpp
        src/filters/blur.cpp
        src/bmp_handler.cpp
)

target_include_directories(image_test PRIVATE include)

target_link_libraries(image_test PRIVATE gtest_main)

add_test(NAME ImageProcessorTests COMMAND image_test)
