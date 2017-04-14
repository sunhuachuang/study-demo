package main

import (
	"fmt"
	"reflect"
	"strconv"
)

type Person struct {
	name string
	age  int
}

type Dog struct {
	name string
}

func (p Person) say() {
	fmt.Println("hello, ", p.name)
}

//only a copy d
func (d Dog) say() {
	fmt.Println("wang wang, ", d.name)
}

//pointer
func (d *Dog) change() {
	d.name = "changed"
}

//interface
type Hello interface {
	say()
}

func say(some interface{}) {
	fmt.Println(some)
}

func (this Person) String() string {
	return "name is " + this.name + ", age is " + strconv.Itoa(this.age)
}

//comma-ok panic value, ok = element.(T)
func checkType(element interface{}) {
	if value, ok := element.(Person); ok {
		fmt.Println(value) //this is a copy fmt.Println(element)
		println(&value)
		println(&element)
	} else {
		fmt.Println("this interface is not person type")
	}

	switch value := element.(type) { //type only use in switch
	case int:
		fmt.Println("this is int: ", value)
	case Person:
		fmt.Println("this is person: ", value)
	default:
		fmt.Println("donot know: ", value)
	}
}

// interface support mixin
// reflection
// t := reflect.TypeOf(i)    //得到类型的元数据,通过t我们能获取类型定义里面的所有元素
// v := reflect.ValueOf(i)   //得到实际的值，通过v我们获取存储在里面的值，还可以去改变值
func testReflect() {
	t := reflect.TypeOf(1)
	fmt.Println(t) //int
	vv := reflect.ValueOf(1)
	fmt.Println(vv) //1

	var x float64 = 3.4
	v := reflect.ValueOf(x)
	fmt.Println("type:", v.Type())
	fmt.Println("kind is float64:", v.Kind() == reflect.Float64)
	fmt.Println("value:", v.Float())

	var xx float64 = 3.4
	pp := reflect.ValueOf(&xx)
	v2 := pp.Elem()
	v2.SetFloat(7.1)
	fmt.Println(xx) //7.1
}

func main() {
	p := Person{"sun", 2}
	p.say()

	d := Dog{"hua"}
	d.say()

	d.change()
	d.say()

	var h Hello
	p1 := Person{"a", 1}
	d1 := Dog{"b"}

	h = p1
	h.say()

	h = d1
	h.say()

	hh := make([]Hello, 2)
	hh[0] = p1
	hh[1] = d1

	for _, i := range hh {
		i.say()
	}

	say(p1)
	say(d1)

	checkType(p)
	checkType(1)

	testReflect()
}
