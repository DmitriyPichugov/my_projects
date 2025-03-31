#pragma once

#include "filter.h"

class NegativeFilter : public Filter {
public:
    void Apply(Image& image) const override;
};
