package main

import (
	"fmt"
	"net/http"
)

type MyMux struct{}

func (m MyMux) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path == "/" {
		helloName(w, r)
		return
	}

	http.NotFound(w, r)
	return
}

func helloName(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "hello, world")
}

func main() {
	m := &MyMux{}
	http.ListenAndServe(":9000", m)
}
