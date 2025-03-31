#include "filters/grayscale.h"

namespace {
constexpr float GrayscaleRedCoeff = 0.299f;
constexpr float GrayscaleGreenCoeff = 0.587f;
constexpr float GrayscaleBlueCoeff = 0.114f;
}  // namespace

void GrayscaleFilter::Apply(Image& image) const {
    for (size_t y = 0; y < image.GetHeight(); ++y) {
        for (size_t x = 0; x < image.GetWidth(); ++x) {
            Color& color = image.At(x, y);
            float gray = GrayscaleRedCoeff * color.r + GrayscaleGreenCoeff * color.g +
                         GrayscaleBlueCoeff * color.b;
            color.r = gray;
            color.g = gray;
            color.b = gray;
        }
    }
}
