#include "filters/filter_factory.h"
#include "filters/grayscale.h"
#include "filters/crop.h"
#include "filters/glass.h"
#include "filters/negative.h"
#include "filters/sharpening.h"
#include "filters/edge.h"
#include "filters/blur.h"
#include <stdexcept>

std::vector<FilterConfig> ParseArgs(int argc, char** argv) {
    std::vector<FilterConfig> filters;
    if (argc < 3) {
        throw std::invalid_argument("Usage: image_processor input.bmp output.bmp [-filter ...]");
    }
    for (int i = 3; i < argc;) {
        std::string name = argv[i] + 1;
        FilterConfig cfg{name, {}};
        if (name == "crop") {
            if (i + 2 >= argc) {
                throw std::invalid_argument("Crop filter requires 2 parameters");
            }
            cfg.params.push_back(argv[++i]);
            cfg.params.push_back(argv[++i]);
        } else if (name == "edge") {
            if (i + 1 >= argc) {
                throw std::invalid_argument("Edge filter requires 1 parameter");
            }
            cfg.params.push_back(argv[++i]);
        } else if (name == "blur") {
            if (i + 1 >= argc) {
                throw std::invalid_argument("Blur filter requires 1 parameter");
            }
            cfg.params.push_back(argv[++i]);
        }
        ++i;
        filters.push_back(cfg);
    }
    return filters;
}

std::unique_ptr<Filter> FilterFactory::Create(const std::string& name, const std::vector<std::string>& params) {
    if (name == "gs") {
        if (!params.empty()) {
            throw std::invalid_argument("Grayscale filter takes no parameters");
        }
        return std::make_unique<GrayscaleFilter>();
    }
    if (name == "crop") {
        if (params.size() != 2) {
            throw std::invalid_argument("Crop filter requires 2 parameters");
        }
        return std::make_unique<CropFilter>(std::stoul(params[0]), std::stoul(params[1]));
    }
    if (name == "neg") {
        if (!params.empty()) {
            throw std::invalid_argument("Negative filter takes no parameters");
        }
        return std::make_unique<NegativeFilter>();
    }
    if (name == "sharp") {
        if (!params.empty()) {
            throw std::invalid_argument("Sharpening filter takes no parameters");
        }
        return std::make_unique<SharpeningFilter>();
    }
    if (name == "edge") {
        if (params.size() != 1) {
            throw std::invalid_argument("Edge filter requires 1 parameter");
        }
        return std::make_unique<EdgeDetectionFilter>(std::stof(params[0]));
    }
    if (name == "blur") {
        if (params.size() != 1) {
            throw std::invalid_argument("Blur filter requires 1 parameter");
        }
        return std::make_unique<GaussianBlurFilter>(std::stof(params[0]));
    }
    if (name == "glass") {
        if (!params.empty()) {
            throw std::invalid_argument("Glass filter takes no parameters");
        }
        return std::make_unique<GlassFilter>();
    }
    throw std::invalid_argument("Unknown filter: " + name);
}
