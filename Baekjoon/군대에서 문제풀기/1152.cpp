#include <iostream>

using namespace std;

int main() {
	char str[1000000];
	cin.getline(str, 1000000, '\n');
	
	// 문자가 없는 경우 0을 출력
	if(str[0] == '\0' || (str[0] == ' ' && str[1] == '\0')) {
		cout << 0 << endl;
		return 0;
	}
	
	long long spaceCount = 0;
	for(long long i = 0; i < 1000000 && str[i] != '\0'; i++) {
		if(str[i] == ' ' && i != 0 && str[i + 1] != '\0')
			spaceCount++;
	}
	
	// 단어의 개수는 공백 + 1
	cout << (spaceCount + 1) << endl;
	return 0;
}
