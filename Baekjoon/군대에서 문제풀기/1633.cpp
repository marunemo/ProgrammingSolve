#include <iostream>
#include <cstring>

using namespace std;

// 냅색 문제와 상당히 유사
int bestTeamMaker(int teamStat[][16][16], int playerStat[][2], int maxPlayerIndex, int playerIndex, int white, int black) {
	// 흑과 백의 인덱스가 모두 15인 경우, 모두 0으로 나타나므로 미리 계산한다.
	if(white == 15 && black == 15)
		return 0;
	
	// 흑과 백으로 플레이하는 인원이 모두 채워지지 않은 채로 마지막 인덱스에 도달한 경우에는 의미 없는 값으로 간주한다.
	if(playerIndex == maxPlayerIndex)
		return 0;
	
	// 메모이제이션
	if(teamStat[playerIndex][white][black])
		return teamStat[playerIndex][white][black];
	
	int tempStat = 0;
	
	// 백으로 플레이하는 인원이 15명 이하라면 현재 인덱스의 인원이 백으로 플레이하는 경우 계산
	if(white < 15) {
		tempStat = bestTeamMaker(teamStat, playerStat, maxPlayerIndex, playerIndex + 1, white + 1, black) + playerStat[playerIndex][0];
		if(tempStat > teamStat[playerIndex][white][black])
			teamStat[playerIndex][white][black] = tempStat;
	}
	// 흑으로 플레이하는 인원이 15명 이하라면 현재 인덱스의 인원이 흑으로 플레이하는 경우 계산
	if(black < 15) {
		tempStat = bestTeamMaker(teamStat, playerStat, maxPlayerIndex, playerIndex + 1, white, black + 1) + playerStat[playerIndex][1];
		if(tempStat > teamStat[playerIndex][white][black])
			teamStat[playerIndex][white][black] = tempStat;
	}
	// 현재 인덱스의 인원이 대회 참가 대상이 아닌 경우 계산
	tempStat = bestTeamMaker(teamStat, playerStat, maxPlayerIndex, playerIndex + 1, white, black);
	if(tempStat > teamStat[playerIndex][white][black])
		teamStat[playerIndex][white][black] = tempStat;
	
	// 현재 인덱스의 최대 팀능력치 반환
	return teamStat[playerIndex][white][black];
}

int main() {
	// FAST IO
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);
	
	// 입력받을 플레이어 능력치 초기화
	int playerStat[1001][2];
	for(int i = 0; i < 1001; i++)
		memset(playerStat[i], 0, 2 * sizeof(int));
	
	// 입력이 끝날 때까지 플레이어의 능력치를 입력 받음
	int white, black, playerIndex = 0;
	while(cin >> white >> black) {
		playerStat[playerIndex][0] = white;
		playerStat[playerIndex][1] = black;
		playerIndex++;
	}
	
	// 흑과 백 플레이어 수와 현재 플레이어 차례에 따른 최대 능력치를 저장할 메모 배열 생성
	int teamStat[1001][16][16];
	for(int i = 0; i < 1001; i++) {
		for(int j = 0; j < 16; j++)
			memset(teamStat[i], 0, 16 * sizeof(int));
	}
	
	// 나타날 수 있는 모든 경우의 수 중 최대의 능력치 출력
	cout << bestTeamMaker(teamStat, playerStat, playerIndex, 0, 0, 0) << endl;
	
	return 0;
}
