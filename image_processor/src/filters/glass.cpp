#include "filters/glass.h"
#include <random>

namespace {
constexpr int GlassOffsetMin = -5;
constexpr int GlassOffsetMax = 5;
}  // namespace

void GlassFilter::Apply(Image& image) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(GlassOffsetMin, GlassOffsetMax);

    Image temp = image;
    for (size_t y = 0; y < image.GetHeight(); ++y) {
        for (size_t x = 0; x < image.GetWidth(); ++x) {
            int offset_x = dist(gen);
            int offset_y = dist(gen);
            size_t dx = static_cast<size_t>(
                std::max(0, std::min(static_cast<int>(x) + offset_x, static_cast<int>(image.GetWidth()) - 1)));
            size_t dy = static_cast<size_t>(
                std::max(0, std::min(static_cast<int>(y) + offset_y, static_cast<int>(image.GetHeight()) - 1)));
            image.At(x, y) = temp.At(dx, dy);
        }
    }
}
