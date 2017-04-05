package main

import (
	"errors"
	"fmt"
	"reflect"
	"runtime"
)

var i int = 10 //var 一般用与定义全局变量
var (
	HELLO = "hello"
	WORLD = "world"
)

func main() {
	println("hello, world")
	fmt.Printf("%s\n", runtime.Version())
	variable()
	error_handle()
	const_iota()
	array_slice_map()
}

func array_slice_map() {
	var arr [10]int
	arr[0] = 0
	arr[2] = 2
	fmt.Println(arr) //[0 0 2 0 0 0 0 0 0 0]

	arrr := [...]int{1, 2, 3, 4}
	fmt.Println(arrr)

	arrm := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println(arrm)

	//数组的传递是值传递，而不是指针
	change_array(arrr)
	fmt.Println(arrr) //[1 2 3 4]

	var sli []int //slice 声明不用指定长度，实质是引用类型
	sli = arrr[0:2]
	fmt.Println(sli)
	fmt.Println(reflect.TypeOf(sli))

	slis := []byte{'a', 'b', 'c', 'd', 'e'}
	fmt.Println(slis)

	// slice 可以改变数组
	a := [5]byte{'a', 'b', 'c', 'd', 'e'}
	fmt.Println("before change:", a)
	sliss := a[:]
	change_slice(a[:])
	fmt.Println("after change:", a)
	slisss := a[1:3:4]
	fmt.Println("no three cap is ", cap(sliss), sliss)    //5 [65 98 99 100 101]
	fmt.Println("has three cap is ", cap(slisss), slisss) //3 [98 99]

	//map == dict 与slice一样是引用传递，而且二者都需要初始化
	//var numbers map[string]int
	numbers := make(map[string]int) //需要初始化才能赋值 make 作用于 slice map channel
	numbers["one"] = 1
	numbers["two"] = 2
	one := numbers["one"]
	no, ok := numbers["no"]
	if !ok {
		println("not get no")
	}
	delete(numbers, "two")
	fmt.Println(numbers, " one is", one, " no contain ", no)
}

func change_slice(sli []byte) {
	sli[0] = 'A'
}

func change_array(arr [4]int) {
	arr[0] = 10
	fmt.Println(arr) //[10 2 3 4]
}

func const_iota() {
	const (
		h = iota //0
		i = iota //1
		j        //2
		k        //3
	)

	const l = iota          //0
	const m, n = iota, iota //0 0 同一行代表一个值
	println(h, i, j, k, l, m, n)
}

func error_handle() {
	err := errors.New("this is new error")
	if err != nil {
		fmt.Println(err)
	}
}

func variable() {
	println(i)

	a := 10
	println(a)

	b, c := 'b', 'c'
	println(b, c)

	const PI float32 = 3.1415926
	const MAX = 10
	println(PI, MAX)

	var bool_true bool = true
	bool_false := false
	if bool_true && !bool_false {
		println("bool_true, bool_false")
	}

	complex32 := 5 + 10i
	println("complex32 is %v", complex32)

	var s string = "this"
	ss := "thisis"
	println(s, ss)
	ss = "abcde"
	println(ss, ss[1:3]) //切片前闭后开 bc

	//ss[0] = "A" 切片不可变
	cs := []byte(ss)
	cs[0] = 'A'
	sss := string(cs)
	println(sss)

	ssss := sss + "fgh"
	println(ssss)

	sml := `this is first line
	       this is second line`
	println(sml)
}
