#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main() {

	int a, b; cin >> a >> b;
	bool flag = 0;

	for (int i = a; i <= b; i++)
	{
		if (i % 3 == 0)
		{
			flag = 1;
		}
		for (int j = i; j; j /= 10)
		{
			if (j % 10 == 3)
			{
				flag = 1;
			}
		}
		if (flag)
		{
			cout << i << endl;
		}
		flag = 0;
	}

	return 0;
}