#pragma once

#include <vector>
#include <stdexcept>

struct Color {
    float r = 0.0f;
    float g = 0.0f;
    float b = 0.0f;
};

class Image {
public:
    Image(size_t width, size_t height);
    size_t GetWidth() const;
    size_t GetHeight() const;
    Color& At(size_t x, size_t y);
    const Color& At(size_t x, size_t y) const;

private:
    size_t width_, height_;
    std::vector<std::vector<Color>> data_;
};
