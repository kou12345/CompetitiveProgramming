#include <iostream>

using namespace std;

int main()
{
    int A = 0; // 500yen
    int B = 0; // 100yen
    int C = 0; // 50yen
    int X = 0; // 合計金額
    int ans = 0;

    cin >> A >> B >> C >> X;

    for (int i = 0; i < A + 1; i++)
    {
        for (int j = 0; j < B + 1; j++)
        {
            for (int k = 0; k < C + 1; k++)
            {
                if (500 * i + 100 * j + 50 * k == X)
                {
                    ans++;
                }
            }
        }
    }
    

    cout << ans << endl;

    return 0;
}