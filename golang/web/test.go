package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

func sayHelloName(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	fmt.Println(r.Form)
	fmt.Println("path: ", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])

	for k, v := range r.Form {
		fmt.Println("key: ", k, " , value: ", strings.Join(v, " "))
	}
	s := "hello" + strings.Join(r.Form["name"], "")
	fmt.Fprintf(w, s)
}

func main() {
	http.HandleFunc("/", sayHelloName)

	err := http.ListenAndServe(":9000", nil)

	if err != nil {
		log.Fatal("listenAndServe", err)
	}
}
