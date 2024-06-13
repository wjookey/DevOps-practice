#ifndef COUNTER_HPP
#define COUNTER_HPP

class Counter {
public:
    long long value;
    Counter(long long value);
    void increment();
    void decrement();
    long long get() const;
    ~Counter();
};

#endif