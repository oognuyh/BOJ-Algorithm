/*
����
���� n���� �־����� ��, n���� ���� ���ϴ� �Լ��� �ۼ��Ͻÿ�.

�ۼ��ؾ� �ϴ� �Լ��� ������ ����. (�Լ��� �����ϴ� ��������)
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