#pragma once

#include "filter.h"
#include <memory>
#include <string>
#include <vector>

struct FilterConfig {
    std::string name;
    std::vector<std::string> params;
};

std::vector<FilterConfig> ParseArgs(int argc, char** argv);

class FilterFactory {
public:
    static std::unique_ptr<Filter> Create(const std::string& name, const std::vector<std::string>& params);
};
