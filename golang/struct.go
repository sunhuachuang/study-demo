package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
}

type Who struct {
	person
	say string
}

func main() {
	var p person
	p.name = "aaa"
	p.age = 20
	fmt.Println(p)

	p2 := person{"sun", 22}
	fmt.Println(p2)

	p3 := person{name: "sss", age: 21}
	fmt.Println(p3)

	p4 := new(person)
	p4.name = "s"
	fmt.Println(p4)

	who := Who{person: p, say: "hello"}
	fmt.Println(who)
}
