#pragma once

#include <array>
#include <cstdint>
#include <vector>
#include <cstddef>

class MT19937 {

public:
    MT19937();
    explicit MT19937(uint32_t s);

    void seed(uint32_t s);
    uint32_t extract_number();

    double uniform();
    std::vector<double> uniform(int count);

private:
    static constexpr uint32_t w = 32;
    static constexpr uint32_t n = 624;
    static constexpr uint32_t m = 397;
    static constexpr uint32_t r = 31;

    static constexpr uint32_t a = 0x9908B0DFu;
    static constexpr uint32_t u = 11;
    static constexpr uint32_t d = 0xFFFFFFFFu;
    static constexpr uint32_t s = 7;
    static constexpr uint32_t b = 0x9D2C5680u;
    static constexpr uint32_t t = 15;
    static constexpr uint32_t c = 0xEFC60000u;
    static constexpr uint32_t l = 18;
    static constexpr uint32_t f = 1812433253u;

    static constexpr uint32_t upper_mask = 0x80000000u;
    static constexpr uint32_t lower_mask = 0x7FFFFFFFu;

    std::array<int, n> m_mt;
    uint32_t m_index = n;

    void twist();
};