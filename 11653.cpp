#include <iostream>
using namespace std;

int N;

void exe(){
    int cnt = 2;

    while (N > 1){
        if (N % cnt != 0){
            while (N % cnt != 0){
                cnt++;
            }
        }

        N /= cnt;
        cout << cnt << '\n';
    }
}

int main(){

    cin >> N;

    exe();
    
}
