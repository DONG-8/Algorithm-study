// getline �ѹ��� �ޱ� ����
 #include <bits/stdc++.h>
 
 using namespace std;
 
 
 string s;
 // ������ ��
 int T; 
 
 int main(){
// 	getline(cin, s);
// 	cout << s << "\n";
// 	return 0;
 	
 	// ������, cin���� T���� getline�� �������� �����ϰ� T�� ��ŭ getline�� �Է��� ������ ��Ȳ�� �ֽ��ϴ�.
	// Ʋ�� ���ڿ��� ������� ���� �����ø� �ϰ� �޾ƾ� �մϴ�.
	
	// �̶����� �߰��� ��ġ�� ���ۿ� \n �� �����ְ� ��.
	
	cin >> T;
//	string bufferflush;
//	getline(cin, bufferflush);
	for ( int i = 0; i < T; i++) {
		getline(cin,s);
		cout << s << "\n";
	}
	return 0;
 } 
