#include "mt19937.hpp"

MT19937::MT19937() {
    seed(42);
}

MT19937::MT19937(uint32_t s) {
    seed(s);
}

void MT19937::seed(uint32_t s) {
    m_mt[0] = s;
    for (uint32_t i = 1; i < n; ++i) {
        uint32_t x = m_mt[i - 1] ^ (m_mt[i - 1] >> (w - 2));
        m_mt[i] = static_cast<uint32_t>(f * x + i);
    }
    m_index = n;
}

uint32_t MT19937::extract_number() {
    if (m_index >= n) {
        twist();
        m_index = 0;
    }

    uint32_t y = m_mt[m_index];

    y ^= ((y >> u) & d);
    y ^= ((y << t) & c);
    y ^= ((y << s) & b);
    y ^= (y >> l);

    m_index++;
    return y;
}

double MT19937::uniform() {
    return static_cast<double>(extract_number()) * (1.0 / 4294967296.0);
}

std::vector<double> MT19937::uniform(int count) {
    if (count <= 0) return {};
    std::vector<double> res;
    res.reserve(static_cast<size_t>(count));
    for (int i = 0; i < count; ++i) res.push_back(uniform());
    return res;
}

void MT19937::twist() {
    for (uint32_t i = 0; i < n; ++i) {
        uint32_t x = (m_mt[i] & upper_mask) | (m_mt[(i + 1) % n] & lower_mask);
        uint32_t xA = x >> 1;
        if (x & 1u) xA ^= a;
        m_mt[i] = m_mt[(i + m) % n] ^ xA;
    }
}
