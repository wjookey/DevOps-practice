CXX = g++
CXXFLAGS = -g -O1
INCLUDE = include

all: main clean
clean:
	del /f main *.o
main: main.o Counter.o
	mkdir bin | $(CXX) $(CXXFLAGS) $^ -o bin/$@.exe

main.o:
	$(CXX) $(CXXFLAGS) -I $(INCLUDE) -c src/main.cpp

Counter.o:
	$(CXX) $(CXXFLAGS) -I $(INCLUDE) -c src/Counter.cpp

.PHONY: all clean