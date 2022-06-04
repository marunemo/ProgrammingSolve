#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
	// fast IO 코드
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
	
	const char* ALPHALIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	const int ALPHACOUNT = 52;
	
	int n;
	cin >> n;
	
	vector<vector<bool>> adjMatrix;
	unordered_map<char, int> alphaIndex;
	for(int i = 0; i < ALPHACOUNT; i++) {
		alphaIndex[ALPHALIST[i]] = i;
		adjMatrix.push_back(vector<bool>(ALPHACOUNT, false));
	}
	
	for(int i = 0; i < n; i++) {
		char p, q;
		cin >> p;
		cin.ignore(3);
		cin >> q;
		
		adjMatrix[alphaIndex[p]][alphaIndex[q]] = true;
	}
	
	// https://namu.wiki/w/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
	for(int m = 0; m < ALPHACOUNT; m++) {
		for(int s = 0; s < ALPHACOUNT; s++) {
			for(int e = 0; e < ALPHACOUNT; e++) {
				if(adjMatrix[s][m] && adjMatrix[m][e])
					adjMatrix[s][e] = true;
			}
		}
	}
	
	for(int i = 0; i < ALPHACOUNT; i++) {
		for(int j = 0; j < ALPHACOUNT; j++) {
			if(i != j && adjMatrix[i][j])
				cout << ALPHALIST[i] << " => " << ALPHALIST[j] << "\n";
		}
	}
	
	return 0;
}
