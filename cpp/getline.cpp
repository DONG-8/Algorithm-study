// getline 한번에 받기 위함
 #include <bits/stdc++.h>
 
 using namespace std;
 
 
 string s;
 // 여러개 행
 int T; 
 
 int main(){
// 	getline(cin, s);
// 	cout << s << "\n";
// 	return 0;
 	
 	// 하지만, cin으로 T개의 getline을 받을지를 설정하고 T개 만큼 getline의 입력이 들어오는 상황이 있습니다.
	// 틀정 문자열을 기반으로 버퍼 를래시를 하고 받아야 합니다.
	
	// 이때문에 중간에 위치한 버퍼에 \n 이 남아있게 됨.
	
	cin >> T;
//	string bufferflush;
//	getline(cin, bufferflush);
	for ( int i = 0; i < T; i++) {
		getline(cin,s);
		cout << s << "\n";
	}
	return 0;
 } 
