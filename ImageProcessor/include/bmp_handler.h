#pragma once

#include "image.h"
#include <string>

class BMPReader {
public:
    static Image Read(const std::string& path);
};

class BMPWriter {
public:
    static void Write(const Image& image, const std::string& path);
};
