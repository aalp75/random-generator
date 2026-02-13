#include "middle_square.hpp"

MiddleSquare::MiddleSquare() : m_state(57), m_space(10'000) {}
MiddleSquare::MiddleSquare(int seed) :m_state(seed), m_space(10'000) {
    m_state %= m_space;
}

void MiddleSquare::nextState() {
    m_state = m_state * m_state;
    std::string s = std::to_string(m_state);

    while (s.size() < 8)
        s = "0" + s;

    m_state = std::stoi(s.substr(2, 4));
}

double MiddleSquare::uniform() {
    nextState();
    return static_cast<double>(m_state) / static_cast<double>(m_space);
}