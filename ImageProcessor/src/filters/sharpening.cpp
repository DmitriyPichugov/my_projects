#include "filters/sharpening.h"

void SharpeningFilter::Apply(Image& image) const {
    Image temp = image;
    const float matrix[3][3] = {{0, -1, 0}, {-1, 5, -1}, {0, -1, 0}};

    for (size_t y = 0; y < image.GetHeight(); ++y) {
        for (size_t x = 0; x < image.GetWidth(); ++x) {
            float r = 0.0f;
            float g = 0.0f;
            float b = 0.0f;
            for (int dy = -1; dy <= 1; ++dy) {
                for (int dx = -1; dx <= 1; ++dx) {
                    int px = static_cast<int>(x) + dx;
                    int py = static_cast<int>(y) + dy;
                    px = std::max(0, std::min(px, static_cast<int>(image.GetWidth()) - 1));
                    py = std::max(0, std::min(py, static_cast<int>(image.GetHeight()) - 1));
                    const Color& c = temp.At(px, py);
                    float weight = matrix[dy + 1][dx + 1];
                    r += c.r * weight;
                    g += c.g * weight;
                    b += c.b * weight;
                }
            }
            r = std::min(1.0f, std::max(0.0f, r));
            g = std::min(1.0f, std::max(0.0f, g));
            b = std::min(1.0f, std::max(0.0f, b));
            image.At(x, y) = {r, g, b};
        }
    }
}
