#include "filters/edge.h"
#include "filters/grayscale.h"

void EdgeDetectionFilter::Apply(Image& image) const {
    GrayscaleFilter grayscale;
    grayscale.Apply(image);

    Image temp = image;
    const float matrix[3][3] = {{-1, -1, -1}, {-1, 8, -1}, {-1, -1, -1}};

    for (size_t y = 0; y < image.GetHeight(); ++y) {
        for (size_t x = 0; x < image.GetWidth(); ++x) {
            float sum = 0.0f;
            for (int dy = -1; dy <= 1; ++dy) {
                for (int dx = -1; dx <= 1; ++dx) {
                    int px = static_cast<int>(x) + dx;
                    int py = static_cast<int>(y) + dy;
                    if (px >= 0 && px < static_cast<int>(image.GetWidth()) && py >= 0 &&
                        py < static_cast<int>(image.GetHeight())) {
                        sum += temp.At(px, py).r * matrix[dy + 1][dx + 1];
                    }
                }
            }
            float value = sum > threshold_ ? 1.0f : 0.0f;
            image.At(x, y) = {value, value, value};
        }
    }
}
