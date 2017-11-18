#include <iostream>
using namespace std;

#define SIZE 22

int main() {
	long grid[SIZE][SIZE];
	for (long i = 0; i < SIZE; i++) {
		grid[0][i] = 1;
		grid[i][0] = 1;
	}
	for (long i = 1; i < SIZE; i++) 
		for (long j = 1; j < SIZE; j++) 
			grid[i][j] = grid[i-1][j] + grid[i][j-1];
	for (long i = 0; i < SIZE; i++)
		cout << grid[i][i] << endl;
	return 0;
}
