#pragma once

#include <cstdint>

#include "congruence.hpp"

/**
 * Well-known suitable values for congruence generator:
 * 
 * RANDU
 *  a = 65539, b = 0, m = 2 ^ 31 - 1
 * 
 * Standard Minimal
 *  a = 16807, b = 0, m = 2 ^ 31 - 1
 */

CongruenceGenerator::CongruenceGenerator()
    : a(65539)
    , c(0)
    , m((1ll << 31) - 1)
    , m_state(57)
    {}

CongruenceGenerator::CongruenceGenerator(uint64_t seed) 
    : a(65539)
    , c(0)
    , m((1ll << 31) - 1)
    , m_state(seed)
    {}

CongruenceGenerator::CongruenceGenerator(uint64_t a, uint64_t c, uint64_t m)
    : a(a)
    , c(c)
    , m(m)
    , m_state(57)
    {}

CongruenceGenerator::CongruenceGenerator(uint64_t a, uint64_t c, uint64_t m, uint64_t seed)
    : a(a)
    , c(c)
    , m(m)
    , m_state(seed)
    {}

void CongruenceGenerator::nextState() {
    m_state = (a * m_state + c) % m;
}

double CongruenceGenerator::uniform() {
    nextState();
    return static_cast<double>(m_state) / static_cast<double>(m);
}