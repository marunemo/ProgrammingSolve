#include <iostream>

using namespace std;

int main() {
	int n, k, m;
	cin >> n >> k >> m;
	
	int currentVideo[100000];
	int nextVideo[100000];
	
	for(int i = 0; i < n; i++) {
		int videoChannel;
		cin >> videoChannel;
		
		// 번호를 인덱스에 맞게 수정
		currentVideo[i] = videoChannel - 1;
	}
	
	for(int i = 0; i < k; i++) {
		int nextChannel;
		cin >> nextChannel;
		
		// 번호를 인덱스에 맞게 수정
		nextVideo[i] = nextChannel - 1;
	}
	
	// 처음 보는 비디오 재생 시간 1분 감산
	for(long long t = 0; t < m - 1; t++) {
		for(int i = 0; i < n; i++) {
			currentVideo[i] = nextVideo[currentVideo[i]];
		}
	}
	
	for(int i = 0; i < n; i++) {
		// 인덱스를 서수대로 출력
		cout << (currentVideo[i] + 1) << " ";
	}
	endl(cout);
	
	return 0;
}
