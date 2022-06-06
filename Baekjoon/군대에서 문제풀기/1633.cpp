#include <iostream>
#include <vector>

using namespace std;

// 냅색 문제와 상당히 유사
int bestTeamMaker(vector<vector<vector<int>>> teamStat, vector<pair<int, int>> playerStat, int playerIndex, int white, int black) {
	// 마지막에 도달하기 전에 모든 인원이 채워지더라도 결국 모든 인원을 고려한 것이 아니므로 무시한다.
	if(white == 15 && black == 15) {
		return 0;
	}
	
	// 흑과 백으로 플레이하는 인원이 모두 채워지지 않은 채로 마지막 인덱스에 도달해도 무시한다.
	if(playerIndex == 1000) {
		return 0;
	}
	
	// 메모이제이션
	if(teamStat[playerIndex][white][black]) {
		return teamStat[playerIndex][white][black];
	}
	
	int tempStat = 0;
	
	// 백으로 플레이하는 인원이 15명 이하라면 현재 인덱스의 인원이 백으로 플레이하는 경우 계산
	if(white < 15) {
		tempStat = bestTeamMaker(teamStat, playerStat, playerIndex + 1, white + 1, black) + playerStat[playerIndex].first;
		if(tempStat > teamStat[playerIndex][white][black])
			teamStat[playerIndex][white][black] = tempStat;
	}
	// 흑으로 플레이하는 인원이 15명 이하라면 현재 인덱스의 인원이 흑으로 플레이하는 경우 계산
	if(white < 15) {
		tempStat = bestTeamMaker(teamStat, playerStat, playerIndex + 1, white, black + 1) + playerStat[playerIndex].second;
		if(tempStat > teamStat[playerIndex][white][black])
			teamStat[playerIndex][white][black] = tempStat;
	}
	// 현재 인덱스의 인원이 대회 참가 대상이 아닌 경우 계산
	tempStat = bestTeamMaker(teamStat, playerStat, playerIndex + 1, white, black);
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
	
	vector<pair<int, int>> playerStat;
	
	int white, black;
	while(!cin.eof()) {
		cin >> white >> black;
		if(!cin.eof())
			playerStat.push_back(make_pair(white, black));
	}
	
	vector<vector<vector<int>>> teamStat(1001, vector<vector<int>>(16, vector<int>(16)));
	
	cout << bestTeamMaker(teamStat, playerStat, 0, 0, 0) << endl;
	
	return 0;
}
