#include <iostream>
#include <string>

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

    cout << countDigits(num) << endl;
}