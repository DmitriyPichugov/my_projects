#pragma once

#include "filter.h"

class SharpeningFilter : public Filter {
public:
    void Apply(Image& image) const override;
};
