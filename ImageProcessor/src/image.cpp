#include "image.h"

Image::Image(size_t width, size_t height) : width_(width), height_(height) {
    data_.resize(height_, std::vector<Color>(width_));
}

size_t Image::GetWidth() const {
    return width_;
}

size_t Image::GetHeight() const {
    return height_;
}

Color& Image::At(size_t x, size_t y) {
    if (x >= width_ || y >= height_) {
        throw std::out_of_range("Image coordinates out of bounds");
    }
    return data_[y][x];
}

const Color& Image::At(size_t x, size_t y) const {
    if (x >= width_ || y >= height_) {
        throw std::out_of_range("Image coordinates out of bounds");
    }
    return data_[y][x];
}
