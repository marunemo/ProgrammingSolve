// 파이썬에 대한 Time Complexity 관련 이슈를 반영하여 C++로도 풀어봄
#include <iostream>

using namespace std;

bool isPrime(int n) {
    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0)
            return false;
    }
    return true;
}

void awesomePrime(int num, int digit, int n) {
    if(digit == n) {
        cout << num << endl;
        return;
    }

    num *= 10;
    int primeDigit[4] = {1, 3, 7, 9};
    for(int i : primeDigit) {
        if(isPrime(num + i))
            awesomePrime(num + i, digit + 1, n);
    }
}

int main() {
    int n;
    cin >> n;

    int firstPrime[4] = {2, 3, 5, 7};
    for(int num : firstPrime)
        awesomePrime(num, 1, n);
}