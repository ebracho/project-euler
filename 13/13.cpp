#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Add two integer strings 
string add(string s1, string s2) {
	string res = "";
	int d1, d2;
	bool carry = 0;
	while (s1.length() < s2.length()) {
		s1.insert(s1.begin(),'0');
	}
	while (s2.length() < s1.length()) {
		s2.insert(s2.begin(),'0');
	}
	for(int i = 0; i < s1.length(); i++) {
		d1 = s1[s1.length()-i-1]-48;
		d2 = s2[s2.length()-i-1]-48;
		carry = (d1+d2+carry)>9;
		res.insert(res.begin(), 48+((d1+d2+carry)%10)); 
	}
	if (carry) {
		res.insert(0,"1");
	}
	return res;
}

int main() {
	string num, sum="0";
	while (getline(cin,num)) {
		sum = add(sum,num);
	}
	cout << sum.substr(0,10) << endl;
	return 0;
}
