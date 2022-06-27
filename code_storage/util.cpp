#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 数値の桁数を取得する
template<typename T>
size_t countDigits(T n)
{
    string tmp;

    tmp = to_string(n);
    return tmp.size();
}

// 各桁の和を計算する
int findSumOfDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}



int main() {
    int num = 1234567;

    vector<int> numbers = {1, 2, 3, 4, 99, 3};
    // vector の最大値を取得
    int maxNum = *max_element(numbers.begin(), numbers.end());
    cout << maxNum << endl;
    
    // イテレータを取得し、値と位置（何番目）を調べる
    auto it = max_element(numbers.begin(), numbers.end());
    cout << it << endl;

    // cout << countDigits(num) << endl;
}