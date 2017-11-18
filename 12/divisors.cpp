#include <iostream>
#include <cmath>
using namespace std;

int divisors(int n) {
	int count = 0;
	int ub = sqrt(n);
	for (int i = 1; i <= ub; i++) {
		if (n%i == 0) {
			count += 2;
		}
	}
	return count;
}

int main() {
	int i, tn=0, dvs;
	while (1) {
		tn += ++i;
		dvs = divisors(tn);
		if (dvs > 500) {
			cout << i << '\t' << tn << '\t' << dvs << endl;
			break;
		}
	}
	return 0;
}
