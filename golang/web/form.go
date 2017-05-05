package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

func login(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Method)
	if r.Method == "GET" {
		t, _ := template.ParseFiles("template/login.gtpl")
		log.Println(t.Execute(w, nil))
	} else {
		r.ParseForm()
		fmt.Println(r.Form)
	}
}

func main() {
	http.HandleFunc("/login", login)
	err := http.ListenAndServe(":9000", nil)

	if err != nil {
		log.Fatal(err)
	}
}
