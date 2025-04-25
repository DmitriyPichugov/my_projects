#pragma once

#include "filter.h"

class EdgeDetectionFilter : public Filter {
public:
    explicit EdgeDetectionFilter(float threshold) : threshold_(threshold) {
    }
    void Apply(Image& image) const override;

private:
    float threshold_;
};
