package main

import (
	"fmt"
	"os"
)

type testFunc func(int) bool //声明一个函数类型

func main() {
	condition()
	function()
}

func condition() {
	x := 1
	if y := x; y == 1 {
		println("this is true, and y is ", y)
	} else if y == 0 {
		println("this is else false")
	} else {
		println("this is false")
	}

	//println(y) cannot use y

	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	println(sum)

	for sum < 1000 {
		sum += sum
	}
	println(sum)

	a := [4]int{1, 2, 3, 4}
	for i := range a {
		println(i)
	}

	m := map[string]string{"a": "aaa", "b": "bbb", "c": "ccc"}
	for k, v := range m {
		println(k, " is ", v)
	}

	n := 5
	switch n {
	case 1:
		println("this is 1")
	case 2:
		println("this is 2")
	case 3, 4, 5:
		println("this is 3, 4, 5")
	default:
		println("this is default")
	}

	switch n {
	case 1, 2, 3, 4, 5:
		println("this is less 5")
		fallthrough
	default:
		println("this is default")
	}
}

func function() {
	no_return(1)
	println(one_return(1, 2))
	a, b := many_return()
	println("this is many return, a, b is ", a, b)
	sum, len := have_return_name(1, 2)
	println("this is many return, sum, len is ", sum, len)
	muliti_param(1, 2, 3, 4, 5)

	y := 1
	pointer(&y)
	fmt.Println("y in func out is ", y)

	openFile()
	slice := []int{1, 2, 3, 4}
	odds := testFuncFilter(slice, isOdd)
	fmt.Println(odds)
	evens := testFuncFilter(slice, isEven)
	fmt.Println(evens)

	//testPanic()
	throwPanic(testPanic)
}

func no_return(a int) {
	println("this is no return a is ", a)
}

func one_return(a int, b int) int {
	return a + b
}

func many_return() (int, int) {
	return 1, 2
}

func have_return_name(a, b int) (sum, len int) {
	sum = a + b
	len = 2
	return
}

//arg is a slice
func muliti_param(arg ...int) {
	for i := range arg {
		println(i)
	}
}

//传指针
//slice, map, channel都是传引用
//若函数需改变slice的长度，则仍需要取地址传递指针
func pointer(x *int) {
	*x += 1
	fmt.Println("x in func is ", *x)
}

//defer 延迟语句, 调用顺序如栈, 先进后出, 由下往上
func openFile() bool {
	f, err := os.Open("readme.md")
	if err != nil {
		panic(err)
	} else {
		println("open file ok")
	}

	defer f.Close()
	defer println("this is first defer")
	defer println("this is second defer")

	return true
}

//函数参数　testFunc
func isOdd(i int) bool {
	if i%2 == 0 {
		return false
	}

	return true
}

func isEven(i int) bool {
	if i%2 == 0 {
		return true
	}

	return false
}

func testFuncFilter(s []int, f testFunc) []int {
	var result []int
	for _, value := range s {
		if f(value) {
			result = append(result, value)
		}
	}

	return result
}

//panic and recover
func testPanic() {
	f, err := os.Open("test.txt")
	defer f.Close() //会执行defer
	if err != nil {
		panic(err)
	}

	println("this is after panic") //cannot get this line
}

func throwPanic(f func()) (b bool) {
	defer func() {
		if x := recover(); x != nil {
			b = true
			println("this is recover") //can get this line
		}
	}()
	f() //如果f函数中有panic 就会恢复过来
	return
}

//main and init init先于main执行
//执行流程:
/**
 * 从main文件中开始
 * import ->(
 *           package1->import1->(
 *                               package2->const2->var2->init2
 *                              )
 *           ->const1->var1->init1
 *          )
 * ->const->var->init->main
 */
func init() {
	println("this is init")
}

//import
/**
 * import (
 *       . "fmt" // . 代表不需要再加前缀, 类似py from os import *
 *       f "fmt" // py import os as f
 *       _ "fmt" // 代表不使用该包，只调用该包的init函数
 *)
 */
