#pragma once

#include "filter.h"
#include <vector>

class GaussianBlurFilter : public Filter {
public:
    explicit GaussianBlurFilter(float sigma);
    void Apply(Image& image) const override;

private:
    float sigma_;
    std::vector<float> GenerateKernel(int size) const;
};
