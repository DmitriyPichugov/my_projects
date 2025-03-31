#include "filters/blur.h"
#include <cmath>
#include <vector>

namespace {
constexpr float MinSigma = 0.1f;
constexpr int KernelSizeFactor = 6;
}  // namespace

GaussianBlurFilter::GaussianBlurFilter(float sigma) : sigma_(sigma) {
    if (sigma_ <= 0.0f) {
        sigma_ = MinSigma;
    }
}

std::vector<float> GaussianBlurFilter::GenerateKernel(int size) const {
    std::vector<float> kernel(size * size);
    float sum = 0.0f;
    int half_size = size / 2;
    for (int y = -half_size; y <= half_size; ++y) {
        for (int x = -half_size; x <= half_size; ++x) {
            float value = static_cast<float>(
                std::exp(-static_cast<float>(x * x + y * y) / (2 * sigma_ * sigma_)) /
                (2 * M_PI * sigma_ * sigma_));
            kernel[(y + half_size) * size + (x + half_size)] = value;
            sum += value;
        }
    }
    for (float& value : kernel) {
        value /= sum;
    }
    return kernel;
}

void GaussianBlurFilter::Apply(Image& image) const {
    int kernel_size = static_cast<int>(std::ceil(KernelSizeFactor * sigma_)) | 1;
    std::vector<float> kernel = GenerateKernel(kernel_size);
    int half_size = kernel_size / 2;

    Image temp = image;

    for (size_t y = 0; y < image.GetHeight(); ++y) {
        for (size_t x = 0; x < image.GetWidth(); ++x) {
            float r = 0.0f;
            float g = 0.0f;
            float b = 0.0f;
            for (int ky = -half_size; ky <= half_size; ++ky) {
                for (int kx = -half_size; kx <= half_size; ++kx) {
                    int px = static_cast<int>(x) + kx;
                    int py = static_cast<int>(y) + ky;
                    px = std::max(0, std::min(px, static_cast<int>(image.GetWidth()) - 1));
                    py = std::max(0, std::min(py, static_cast<int>(image.GetHeight()) - 1));
                    float weight = kernel[(ky + half_size) * kernel_size + (kx + half_size)];
                    const Color& c = temp.At(px, py);
                    r += c.r * weight;
                    g += c.g * weight;
                    b += c.b * weight;
                }
            }
            image.At(x, y) = {r, g, b};
        }
    }
}
