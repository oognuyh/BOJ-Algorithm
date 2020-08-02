#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

vector <pair<int, int> > xy;
/*
C++98에서는 위 코드가 컴파일되지 않습니다. 왜냐하면 “>>”이 연속된 ‘>’으로 인식되는 것이 아니라 
구문 분석 시작 전 어휘 분석 단계(lexical analysis)에서 최대 흡수(Maximal munch) 규칙에 따라  “>>” 토큰으로 인식되고 이는 다시 문법 단계에서 “>>” 연산자로 인식되고,
 ">>" 연산자 좌우로 int, heroChronicles 같은 토큰들이 있는 것으로 인식되기 때문입니다.
따라서 >>를 > >로 해야한다.
출처: https://yesarang.tistory.com/375 [김윤수의 이상계를 꿈꾸며]
 */

void exe(){
    sort(xy.begin(), xy.end());

    for(int i = 0; i < xy.size(); i++)
        cout << xy[i].first << ' ' << xy[i].second << '\n';
    
}

int main(){
    int N;
    int x, y;

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> x >> y;
        xy.push_back(make_pair(x, y));
    }

    exe();
    
}