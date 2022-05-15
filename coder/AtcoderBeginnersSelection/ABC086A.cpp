#include <iostream>

using namespace std;

int main() {
	int a = 0;
	int b = 0;
	int ans = 0;

	cin >> a >> b;

	ans = a * b;

	if (ans % 2 == 0)
	{
		cout << "Even" << endl;
	}
	else
	{
		cout << "Odd" << endl;
	}

	return 0;
}