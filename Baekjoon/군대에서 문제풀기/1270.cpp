#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    // fast IO 코드
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    
    int n;
    cin >> n;
    
    vector<string> answer;
    
    int ti;
    for(int i = 0; i < n; i++) {
        cin >> ti;
        
        unordered_map<long long, int> milCount;
        long long mil;
		bool isOccupied = false;
        for(int j = 0; j < ti; j++) {
            cin >> mil;
			
			if(!isOccupied) {
				if(milCount.find(mil) == milCount.end())
					milCount[mil] = 1;
				else
					milCount[mil]++;

				if(milCount[mil] > ti / 2) {
					answer.push_back(to_string(mil));
					isOccupied = true;
				}
			}
        }

		if(!isOccupied)
			answer.push_back("SYJKGW");
    }
    
    for(int i = 0; i < n; i++)
		cout << answer[i] << "\n";
    
    return 0;
}
