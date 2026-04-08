package main

import (
	"fmt"
	"net/http"
)

func index (w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}

func main() {
	http.HandleFunc("/", index)
	fmt.Println("Servidor rodando na porta 8080")
	http.ListenAndServe(":8080", nil)
}