#include <iostream>

using namespace std;

int main() {
	char str[1000000];
	cin.getline(str, 1000000, '\n');
	
	long long spaceCount = 0;
	for(long long i = 0; i < 1000000 && str[i] != '\0'; i++) {
		if(str[i] == ' ' && i != 0 && str[i + 1] != '\0')
			spaceCount++;
	}
	
	// 단어의 개수는 공백 + 1
	cout << (spaceCount + 1) << endl;
	return 0;
}
