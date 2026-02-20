#pragma once

#include <cstdint>

/** 
 * Linear congruence random generator
 * 
 * Generated a sequence of the form:
 *  Xn = (a * Xn + c) % m
 * 
 * a, c and m are critical in the process and needs to be well chosen
 * 
 * Well-known suitable values for congruence generator:
 * 
 * RANDU
 *  a = 65539, b = 0, m = 2 ^ 31 - 1
 * 
 * Standard Minimal
 *  a = 16807, b = 0, m = 2 ^ 31 - 1
 */

class CongruenceGenerator {

public:

    CongruenceGenerator();
    CongruenceGenerator(uint64_t seed);
    CongruenceGenerator(uint64_t a, uint64_t c, uint64_t m);
    CongruenceGenerator(uint64_t a, uint64_t c, uint64_t m, uint64_t seed);

    void nextState();
    double uniform();

private:
    uint64_t a, c, m;
    uint64_t m_state;
};