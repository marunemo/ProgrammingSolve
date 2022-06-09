#include <iostream>

using namespace std;

void sparseTable(int currentVideo[], int nextVideo[], int due, int n, int k, int &m) {
	if(m < due)
		return;
	
	if(due == 1) {
		sparseTable(currentVideo, nextVideo, due * 2, n, k, m);
		if(m >= due) {
			for(int i = 0; i < n; i++) {
				currentVideo[i] = nextVideo[currentVideo[i]];
			}
		}
	}
	else {
		int jumpVideo[100000];
		for(int i = 0; i < k; i++) {
			jumpVideo[i] = nextVideo[nextVideo[i]];
		}
		
		sparseTable(currentVideo, jumpVideo, due * 2, n, k, m);
		if(m >= due) {
			for(int i = 0; i < n; i++) {
				currentVideo[i] = jumpVideo[currentVideo[i]];
			}
			m -= due;
		}
	}
}

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
	m--;
	sparseTable(currentVideo, nextVideo, 1, n, k, m);
	
	for(int i = 0; i < n; i++) {
		// 인덱스를 서수대로 출력
		cout << (currentVideo[i] + 1) << " ";
	}
	endl(cout);
	
	return 0;
}
