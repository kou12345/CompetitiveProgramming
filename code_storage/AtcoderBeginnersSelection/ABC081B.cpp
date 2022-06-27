#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    int even_num_count = 0; // 割り切れた回数を記録する
    int ans = 0;
    bool flag = true;

    // N 回ループする
    while (flag)
    {
        for (int i = 0; i < N; i++)
        {
            // もし A[i] の値が 2 で割り切れるなら even_num_count++ して A[i] に A[i] / 2 を代入する
            if (A[i] % 2 == 0)
            {
                even_num_count++;
                A[i] = A[i] / 2;
                // even_num_count が N と同じなら ans++ して even_num_count = 0 する
                if (even_num_count == N)
                {
                    ans++;
                    even_num_count = 0;
                }

                // cout << "A[" << i << "]:" << A[i] << endl;
            }
            else
            {
                // 割り切れないなら flag に false 代入する
                flag = false;
                // そうでない場合は、ループを抜ける
                break;
            }
        }
    }

    cout << ans << endl;

    return 0;
}