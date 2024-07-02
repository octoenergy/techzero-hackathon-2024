package router

import (
	"fmt"
	"net/http"
)

func ServeRouter() {
	http.Handle("/energy", enableCORS(http.HandlerFunc(EnergyHandler)))
	http.Handle("/my_response", enableCORS(http.HandlerFunc(myResponse)))
	http.Handle("/health", enableCORS(http.HandlerFunc(healthCheck)))

	fmt.Print("Starting server on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Could not start server: %s\n", err.Error())
	}
}
