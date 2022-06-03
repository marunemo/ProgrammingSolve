#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> answer;
    
    int ti;
    for(int i = 0; i < n; i++) {
        cin >> ti;
        
        unordered_map<int, int> milCount;
        int mil;
        int maxIndex = -1;
        for(int j = 0; j < ti; j++) {
            cin >> mil;
            if(milCount.find(mil) == milCount.end())
                milCount[mil] = 1;
            else
                milCount[mil]++;
            
            if(maxIndex == -1 || milCount[mil] > milCount[maxIndex])
                maxIndex = mil;
        }
        
        if(milCount[maxIndex] > ti / 2)
            answer.push_back(maxIndex);
        else
            answer.push_back(-1);
    }
    
    for(int i = 0; i < n; i++) {
        if(answer[i] == -1)
            cout << "SYJKGW\n";
        else
            cout << answer[i] << "\n";
    }
    
    return 0;
}
