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

int main() {
    int num = 1234567;

    cout << countDigits(num) << endl;
}