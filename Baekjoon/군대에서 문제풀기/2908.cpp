#include <iostream>

int reverseInt(int i) {
    int temp = 0;
    while(i > 0) {
        temp *= 10;
        temp += i % 10;
        i /= 10;
    }
    return temp;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    a = reverseInt(a);
    b = reverseInt(b);
    
    std::cout << ((a > b) ? a : b) << std::endl;
    return 0;
}
