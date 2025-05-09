#include "filters/crop.h"

CropFilter::CropFilter(size_t width, size_t height) : width_(width), height_(height) {
}

void CropFilter::Apply(Image& image) const {
    size_t new_width = std::min(width_, image.GetWidth());
    size_t new_height = std::min(height_, image.GetHeight());
    Image temp(new_width, new_height);
    for (size_t y = 0; y < new_height; ++y) {
        for (size_t x = 0; x < new_width; ++x) {
            temp.At(x, y) = image.At(x, y);
        }
    }
    image = std::move(temp);
}
