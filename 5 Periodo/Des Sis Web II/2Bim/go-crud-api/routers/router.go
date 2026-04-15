package routers

import (
	"go-crud-api/controllers"
	"net/http"

	"github.com/gorilla/mux"
)

func SetupRouter () *mux.Router {
	router := mux.NewRouter()
	router.HandleFunc("/users", controllers.GetUsers).Methods("GET")
	router.NotFoundHandler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNotFound)
		w.Write([]byte("404 - Not Found"))
	})

	return router
}