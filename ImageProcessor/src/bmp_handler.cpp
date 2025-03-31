#include "bmp_handler.h"
#include <cstdint>
#include <fstream>

namespace {
constexpr int BitsPerPixel24 = 24;
constexpr float ColorMax = 255.0f;
constexpr int ColorMaxInt = 255;
}  // namespace

#pragma pack(push, 1)
struct BitmapFileHeader {
    char signature[2];
    uint32_t file_size;
    uint16_t reserved1;
    uint16_t reserved2;
    uint32_t data_offset;
};

struct BitmapInfoHeader {
    uint32_t header_size;
    int32_t width;
    int32_t height;
    uint16_t planes;
    uint16_t bits_per_pixel;
    uint32_t compression;
    uint32_t image_size;
    int32_t x_pixels_per_meter;
    int32_t y_pixels_per_meter;
    uint32_t colors_used;
    uint32_t colors_important;
};
#pragma pack(pop)

Image BMPReader::Read(const std::string& path) {
    std::ifstream file(path, std::ios::binary);
    if (!file) {
        throw std::runtime_error("Cannot open file: " + path);
    }

    BitmapFileHeader file_header;
    BitmapInfoHeader info_header;
    file.read(reinterpret_cast<char*>(&file_header), sizeof(file_header));
    file.read(reinterpret_cast<char*>(&info_header), sizeof(info_header));

    if (file_header.signature[0] != 'B' || file_header.signature[1] != 'M') {
        throw std::runtime_error("Invalid BMP file: " + path);
    }
    if (info_header.bits_per_pixel != BitsPerPixel24) {
        throw std::runtime_error("Only 24-bit BMP files are supported: " + path);
    }

    Image image(info_header.width, std::abs(info_header.height));
    file.seekg(file_header.data_offset, std::ios::beg);

    size_t padding = (4 - (info_header.width * 3) % 4) % 4;
    for (int y = info_header.height - 1; y >= 0; --y) {
        for (int x = 0; x < info_header.width; ++x) {
            uint8_t b = 0;
            uint8_t g = 0;
            uint8_t r = 0;
            file.read(reinterpret_cast<char*>(&b), 1);
            file.read(reinterpret_cast<char*>(&g), 1);
            file.read(reinterpret_cast<char*>(&r), 1);
            image.At(x, y) = {static_cast<float>(r) / ColorMax,
                              static_cast<float>(g) / ColorMax,
                              static_cast<float>(b) / ColorMax};
        }
        file.seekg(static_cast<std::streamoff>(padding), std::ios::cur);
    }
    return image;
}

void BMPWriter::Write(const Image& image, const std::string& path) {
    std::ofstream file(path, std::ios::binary);
    if (!file) {
        throw std::runtime_error("Cannot open file: " + path);
    }

    size_t width = image.GetWidth();
    size_t height = image.GetHeight();
    size_t padding = (4 - (width * 3) % 4) % 4;
    uint32_t row_size = width * 3 + padding;
    uint32_t data_size = row_size * height;
    uint32_t file_size = sizeof(BitmapFileHeader) + sizeof(BitmapInfoHeader) + data_size;

    BitmapFileHeader file_header = {
            {'B', 'M'}, file_size, 0, 0, sizeof(BitmapFileHeader) + sizeof(BitmapInfoHeader)};
    BitmapInfoHeader info_header = {sizeof(BitmapInfoHeader),
                                    static_cast<int32_t>(width),
                                    static_cast<int32_t>(height),
                                    1,
                                    BitsPerPixel24,
                                    0,
                                    data_size,
                                    0,
                                    0,
                                    0,
                                    0};

    file.write(reinterpret_cast<const char*>(&file_header), sizeof(file_header));
    file.write(reinterpret_cast<const char*>(&info_header), sizeof(info_header));

    for (size_t y = height; y > 0; --y) {
        for (size_t x = 0; x < width; ++x) {
            const Color& color = image.At(x, y - 1);
            uint8_t r = static_cast<uint8_t>(color.r * ColorMaxInt);
            uint8_t g = static_cast<uint8_t>(color.g * ColorMaxInt);
            uint8_t b = static_cast<uint8_t>(color.b * ColorMaxInt);
            file.write(reinterpret_cast<const char*>(&b), 1);
            file.write(reinterpret_cast<const char*>(&g), 1);
            file.write(reinterpret_cast<const char*>(&r), 1);
        }
        for (size_t i = 0; i < padding; ++i) {
            file.put(0);
        }
    }
}
