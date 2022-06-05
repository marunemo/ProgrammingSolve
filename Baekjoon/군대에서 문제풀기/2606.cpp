#include <iostream>
#include <vector>

using namespace std;

int main() {
	// FAST IO
	cout.tie(0);
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	
	int comCount, netCount;
	cin >> comCount >> netCount;
	
	vector<vector<bool>> linkedNetwork(comCount, vector<bool>(comCount, false));
	
	for(int i = 0; i < netCount; i++) {
		int com1, com2;
		cin >> com1 >> com2;
		
		// 서수를 인덱스에 맞게 수정
		com1--;
		com2--;
		
		linkedNetwork[com1][com2] = true;
		linkedNetwork[com2][com1] = true;
	}
	
	// Floyd-Warshall algorithm
	for(int m = 0; m < comCount; m++) {
		for(int s = 0; s < comCount; s++) {
			for(int e = 0; e < comCount; e++) {
				if(linkedNetwork[s][m] && linkedNetwork[m][e]) {
					linkedNetwork[s][e] = true;
				}
			}
		}
	}
	
	int answer = 0;
	linkedNetwork[0][0] = false;
	for(int i = 0; i < comCount; i++) {
		if(linkedNetwork[0][i]) answer++;
	}
	
	cout << answer << endl;
	
	return 0;
}
