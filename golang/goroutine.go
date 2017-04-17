package main

import (
	"fmt"
	"runtime"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		runtime.Gosched()
		fmt.Println(s)
	}
}

func sum(a []int, c chan int) {
	total := 0
	for _, v := range a {
		total += v
	}
	c <- total
}

func sendChan(c chan string) {
	c <- "hello world"
}

func getChan(c chan string, where string) {
	fmt.Println("aaaa: ", where)
	s := <-c
	fmt.Println(s, where)
	fmt.Println("ssss", where)
}

func fibonacci(n int, c chan int) {
	x, y := 1, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func selectFibonacci(c, quit chan int) {
	x, y := 1, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func timeoutChan(c chan int, q chan bool) {
	for {
		select {
		case v := <-c:
			fmt.Println(v)
		case <-time.After(5 * time.Second):
			fmt.Println("timeout")
			q <- true
			break
		}
	}
}

func main() {
	go say("hello")
	say("world")

	//ci := make(chan int)
	//cs := make(chan string)
	//cf := make(chan interface{})

	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	c := make(chan int)
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)

	x, y := <-c, <-c

	fmt.Println(x, y, x+y)

	cs := make(chan string, 1)

	go sendChan(cs)
	go getChan(cs, "go")
	getChan(cs, "no")

	cc := make(chan int, 10)
	go fibonacci(cap(cc), cc)

	for i := range cc {
		fmt.Println(i)
	}

	if _, ok := <-cc; !ok {
		fmt.Println("cc is empty")
	}

	ccc, quit := make(chan int), make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-ccc)
		}
		quit <- 0
	}()
	selectFibonacci(ccc, quit)

	cccc, q := make(chan int), make(chan bool)
	go timeoutChan(cccc, q)
	fmt.Println(<-q)
}
