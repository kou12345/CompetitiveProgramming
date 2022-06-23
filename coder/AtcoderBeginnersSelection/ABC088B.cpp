#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    int a = 0;
    vector<int> A(N);

    // 配列に入れたい
    for (int i = 0; i < N; i++) {
        cin >> a;
        A.push_back(a);
    }

    int Alice = 0;
    int Bob = 0;

    for (int i = 0; i < N; i++) {
        auto maxNum = max_element(A.begin(), A.end());
    }


    return 0;
}