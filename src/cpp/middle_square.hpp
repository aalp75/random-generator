#pragma once

#include <array>
#include <cstdint>
#include <vector>
#include <cstddef>
#include <string>

/** 
 * Middle Square random generator from John von Neumann
 * 
 * just implemented for educational purpose and comparisons
*/

class MiddleSquare {

public:
    MiddleSquare();
    MiddleSquare(int seed);

    void nextState();
    double uniform();

private:
    long long m_state; // 4-digits number
    long long m_space; // set to 10'000 to stay in a 4-digits number space
};

