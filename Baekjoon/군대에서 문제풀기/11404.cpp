#include <iostream>
#include <vector>

using namespace std;

int main() {
	// FAST IO
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);
	
	int nodeCount, edgeCount;
	cin >> nodeCount >> edgeCount;
	
	vector<vector<unsigned int>> adjMatrix(nodeCount, vector<unsigned int>(nodeCount, 0));
	for(int i = 0; i < edgeCount; i++) {
		unsigned int start, end, weight;
		cin >> start >> end >> weight;
		
		// 서수를 인덱스에 맞게 수정
		start--;
		end--;
		
		if(adjMatrix[start][end] == 0 || adjMatrix[start][end] > weight)
			adjMatrix[start][end] = weight;
	}
	
	for(int m = 0; m < nodeCount; m++) {
		for(int s = 0; s < nodeCount; s++) {
			for(int e = 0; e < nodeCount; e++) {
				if(s != e && adjMatrix[s][m] != 0 && adjMatrix[m][e] != 0) {
					if(adjMatrix[s][e] == 0 || adjMatrix[s][e] > adjMatrix[s][m] + adjMatrix[m][e]) {
						adjMatrix[s][e] = adjMatrix[s][m] + adjMatrix[m][e];
					}
				}
			}
		}
	}
	
	for(int i = 0; i < nodeCount; i++) {
		for(int j = 0; j < nodeCount; j++) {
			cout << adjMatrix[i][j] << " ";
		}
		cout << "\n";
	}
	
	return 0;
}
