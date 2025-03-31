#pragma once

#include "filter.h"

class GlassFilter : public Filter {
public:
    GlassFilter() = default;
    void Apply(Image& image) const override;
};
