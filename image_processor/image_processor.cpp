#include <iostream>
#include "bmp_handler.h"
#include "filters/filter_factory.h"

void PrintHelp() {
    std::cout << "Usage: image_processor <input_file.bmp> <output_file.bmp> [filters]\n"
              << "Filters:\n"
              << "  -crop <width> <height>    Crop image to specified size\n"
              << "  -gs                      Convert to grayscale\n"
              << "  -neg                     Convert to negative\n"
              << "  -sharp                   Apply sharpening\n"
              << "  -edge <threshold>        Detect edges with threshold (0.0-1.0)\n"
              << "  -blur <sigma>            Apply Gaussian blur with sigma\n"
              << "  -glass                   Apply glass distortion effect\n"
              << "Example: image_processor input.bmp output.bmp -crop 800 600 -gs -blur 0.5\n";
}

int main(int argc, char** argv) {
    try {
        if (argc == 1) {
            PrintHelp();
            return 0;
        }
        if (argc < 3) {
            throw std::invalid_argument("Error: Input and output files must be specified.");
        }

        std::string input_path = argv[1];
        std::string output_path = argv[2];
        Image img = BMPReader::Read(input_path);

        auto filters = ParseArgs(argc, argv);
        for (const auto& filter_config : filters) {
            auto filter = FilterFactory::Create(filter_config.name, filter_config.params);
            filter->Apply(img);
        }

        BMPWriter::Write(img, output_path);
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
