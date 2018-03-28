package main

import (
    "fmt"
    "math"
)

func isPrime(n int, primes []int) bool {
    ub := int(math.Ceil(math.Sqrt(float64(n))))
    for _, p := range primes {
        if p > ub {
            return true
        }
        if n % p == 0 {
            return false
        }
    }
    return true
}

func primesUpTo(n int) []int {
    primes := []int{2}
    for i := 3; i < n; i++ {
        if isPrime(i, primes) {
            primes = append(primes, i)
        }
    }
    return primes
}

func euler69_2(N int) int {
    primes := primesUpTo(200)
    fmt.Println(primes)
    n := 1
    for _, p := range primes {
        n *= p
        if n > N {
            return n/p
        }
    }
    return -1
}

func main() {
    fmt.Println(euler69_2(1000000))
}

