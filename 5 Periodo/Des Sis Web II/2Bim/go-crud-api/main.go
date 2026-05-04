package main

import (
	"go-crud-api/config"
	"go-crud-api/routers"
	"log"
	"net/http"
)

func main() {
	_, err := config.Connect()
	if err != nil {
		log.Fatalf("Erro ao conectar ao banco de dados: %v", err)
	}

	log.Println("Conectado ao banco de dados com sucesso!")

	router := routers.SetupRouter()
	log.Println("Starting server on :8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
