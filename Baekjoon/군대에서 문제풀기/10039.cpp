#include <iostream>

using namespace std;

int main() {
    int totalScore = 0;
    int score;
    for(int i = 0; i < 5; i++) {
        cin >> score;
        if(score < 40) totalScore += 40;
        else totalScore += score;
    }
    cout << (totalScore / 5) << endl;
    return 0;
}
