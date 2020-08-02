#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

vector <pair<int, int> > xy;

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
