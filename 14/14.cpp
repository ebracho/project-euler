#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;

class Collatz {
	private:
		unordered_map<long,long> mem;
	public:
		Collatz();
		long get(int n);
		long _get(int n);
		size_t size();
};

Collatz::Collatz() {
	mem[1] = 1;
}

long Collatz::get(int n) {
	long t=n, len;
	stack<long> terms;
	unordered_map<long,long>::iterator search;

	// Compute terms
	while ((search = mem.find(t)) == mem.end()) {
		terms.push(t);
		if (t%2 == 0)  
			t /= 2;
		else 
			t = t*3 + 1;
	}

	// Cache terms
	len = search->second;
	while (!terms.empty()) {
		mem[terms.top()] = ++len;
		terms.pop();
	}

	return len;
}

long Collatz::_get(int n) {
	int i;
	long term=n;
	for (i=1; term != 1; i++) 
		term = term%2 == 0 ? term/2 : term*3 + 1;
	return i;
}

size_t Collatz::size() {
	return mem.size();
}

// Using _get takes about as long as get
int find_max_term(int lb, int ub) {
	long len, maxlen=0, termmax=1;
	Collatz c = Collatz();
	for (int i = lb; i < ub; i++) {
		if ((len = c.get(i)) > maxlen) {
			maxlen = len;
			termmax = i;
		}
	}
	return termmax;
}

int main() {
	cout << find_max_term(1, 1000000) << endl;
	return 0;
}

