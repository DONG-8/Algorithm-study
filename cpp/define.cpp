// define 을 통해 상수, 매크로를 정의할 수 있음
// #define <이름> <값>

# include <bits/stdc++.h>

using namespace std;

# define PI 3.14159
#define loop(x,n) for (int x = 0; x < n; x++)

int main() {
	cout << PI << '\n';
	int sum = 0;
	loop(i,10) {
		sum  += i;
	}
	cout << sum <<'\n';
	return 0;
} 
