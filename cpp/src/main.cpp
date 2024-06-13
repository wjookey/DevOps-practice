#include <iostream>
#include "Counter.hpp"

int main() {
    Counter cnt(10);
    std::cout << cnt.get() << std::endl;
    cnt.increment();
    std::cout << cnt.get() << std::endl;
    cnt.decrement();
    std::cout << cnt.get() << std::endl;
    return 0;
}