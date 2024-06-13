#include "Counter.hpp"

Counter::Counter(long long value) : value(value) {}

void Counter::increment() {
    value++;
}
 
void Counter::decrement() {
    value--;
}

long long Counter::get() const {
    return value;
}

Counter::~Counter() {}