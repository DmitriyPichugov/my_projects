#include <gtest/gtest.h>
#include "bmp_handler.h"
#include "filters/blur.h"
#include "filters/crop.h"
#include "filters/edge.h"
#include "filters/grayscale.h"
#include "filters/negative.h"

namespace {
constexpr size_t TestImageWidth = 10;
constexpr size_t TestImageHeight = 20;
constexpr float TestColorValue05 = 0.5f;
constexpr float TestColorValue02 = 0.2f;
constexpr float TestColorValue04 = 0.4f;
constexpr float TestColorValue06 = 0.6f;
constexpr float GrayscaleRedCoeff = 0.299f;
constexpr float GrayscaleGreenCoeff = 0.587f;
constexpr float GrayscaleBlueCoeff = 0.114f;
constexpr float EdgeThreshold = 0.5f;
constexpr float BlurSigma = 0.5f;
constexpr size_t CropSizeLarge = 400;
constexpr size_t CropSizeSmall = 200;
constexpr float Epsilon = 1e-2f;

bool AreImagesEqual(const Image& img1, const Image& img2) {
    if (img1.GetWidth() != img2.GetWidth() || img1.GetHeight() != img2.GetHeight()) {
        return false;
    }

    for (size_t y = 0; y < img1.GetHeight(); ++y) {
        for (size_t x = 0; x < img1.GetWidth(); ++x) {
            const Color& c1 = img1.At(x, y);
            const Color& c2 = img2.At(x, y);
            if (std::abs(c1.r - c2.r) > Epsilon ||
                std::abs(c1.g - c2.g) > Epsilon ||
                std::abs(c1.b - c2.b) > Epsilon) {
                return false;
            }
        }
    }
    return true;
}
}  // namespace

TEST(ImageTest, Dimensions) {
    Image img(TestImageWidth, TestImageHeight);
    EXPECT_EQ(img.GetWidth(), TestImageWidth);
    EXPECT_EQ(img.GetHeight(), TestImageHeight);
}

TEST(FilterTest, Grayscale) {
    Image img(1, 1);
    img.At(0, 0) = {1.0f, TestColorValue05, 0.0f};
    GrayscaleFilter filter;
    filter.Apply(img);
    float gray = GrayscaleRedCoeff * 1.0f + GrayscaleGreenCoeff * TestColorValue05 + GrayscaleBlueCoeff * 0.0f;
    EXPECT_FLOAT_EQ(img.At(0, 0).r, gray);
    EXPECT_FLOAT_EQ(img.At(0, 0).g, gray);
    EXPECT_FLOAT_EQ(img.At(0, 0).b, gray);
}

TEST(FilterTest, Negative) {
    Image img(1, 1);
    img.At(0, 0) = {TestColorValue02, TestColorValue04, TestColorValue06};
    NegativeFilter filter;
    filter.Apply(img);
    EXPECT_FLOAT_EQ(img.At(0, 0).r, 1.0f - TestColorValue02);
    EXPECT_FLOAT_EQ(img.At(0, 0).g, 1.0f - TestColorValue04);
    EXPECT_FLOAT_EQ(img.At(0, 0).b, 1.0f - TestColorValue06);
}

TEST(FilterTest, EdgeDetection) {
    Image img(3, 3);
    img.At(1, 1) = {TestColorValue05, TestColorValue05, TestColorValue05};
    EdgeDetectionFilter filter(EdgeThreshold);
    filter.Apply(img);
    EXPECT_FLOAT_EQ(img.At(1, 1).r, 1.0f);
    EXPECT_FLOAT_EQ(img.At(0, 0).r, 0.0f);
}

TEST(FilterTest, GaussianBlur) {
    Image img = BMPReader::Read("../test_script/data/lenna.bmp");
    Image expected = BMPReader::Read("../test_script/data/lenna_blur.bmp");
    GaussianBlurFilter filter(BlurSigma);
    filter.Apply(img);
    EXPECT_TRUE(AreImagesEqual(img, expected));
}

TEST(FilterTest, BlurTwice) {
    Image img = BMPReader::Read("../test_script/data/lenna.bmp");
    Image expected = BMPReader::Read("../test_script/data/lenna_blur_blur.bmp");
    GaussianBlurFilter filter(BlurSigma);
    filter.Apply(img);
    filter.Apply(img);
    EXPECT_TRUE(AreImagesEqual(img, expected));
}

TEST(FilterTest, CropTwice) {
    Image img = BMPReader::Read("../test_script/data/lenna.bmp");
    Image expected = BMPReader::Read("../test_script/data/lenna_crop_crop.bmp");
    CropFilter filter1(CropSizeLarge, CropSizeLarge);
    CropFilter filter2(CropSizeSmall, CropSizeSmall);
    filter1.Apply(img);
    filter2.Apply(img);
    EXPECT_TRUE(AreImagesEqual(img, expected));
}
