#include <cstdint>

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