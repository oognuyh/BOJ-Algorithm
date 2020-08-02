/*
문제
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

작성해야 하는 함수는 다음과 같다. (함수만 구현하는 문제였음)
 */
#include <iostream>
#include <vector>
using namespace std;

long long sum(vector<int> &v){
    long long sum = 0;
    
    for(int i = 0; i < v.size(); i++){
        sum += v[i];
    }

    return sum;
}

int main(){
    vector<int> v;
    int n, x;
    long long result;

    cin >> n;
    while(n--){
        cin >> x;
        v.push_back(x);
    }

    result = sum(v);
    cout << result << '\n';

}