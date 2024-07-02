package router

import (
	"encoding/json"
	"fmt"
	"net/http"

	"main/external"
	"main/models"

	"github.com/brianvoe/gofakeit/v7"
)

func myResponse(w http.ResponseWriter, r *http.Request) {
	var f models.MyResponse
	err := gofakeit.Struct(&f)

	if err != nil {
		fmt.Printf("Error while generating my response: %s", err)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(f)
}

type Response struct {
	Message string `json:"message"`
}

func ShellyHandler(w http.ResponseWriter, r *http.Request) {
	// Create a new instance of ShellyAPIClient
	client := external.ShellyAPIClient{}
	client.SetAPIKey("MjM4ODIzdWlkAADF348BEBF971B1AD87EAF753A4182CC1202C778454F445D2BEE68DB05A61AFB04661939C704494") // Set your API key

	// Fetch the Shelly data using the client
	deviceID := "d48afc400484" // Replace with actual device ID if needed
	data := client.Fetch(deviceID)

	// Set header and return the ShellyResponse object as JSON
	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(data); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func EnergyHandler(w http.ResponseWriter, r *http.Request) {

	query_params := r.URL.Query()
	from_date, to_date, function_id := query_params.Get("from"), query_params.Get("to"), query_params.Get("functionId")

	data := external.GetCarbonIntensityApi(from_date, to_date, function_id)

	// Calculate carbon intensity per minute
	totalCarbonIntensity, ciPerMinuteArray := external.CalcCarbonIntensity(data.Data)

	// Create an instance of ShellyAPIClient and set the API key
	shellyClient := &external.ShellyAPIClient{}
	shellyClient.SetAPIKey("MjM4ODIzdWlkAADF348BEBF971B1AD87EAF753A4182CC1202C778454F445D2BEE68DB05A61AFB04661939C704494") // Set your actual API key here

	// Fetch the Shelly data using the client
	deviceID := "d48afc400484" // Replace with actual device ID if needed
	shellyData := shellyClient.Fetch(deviceID)

	// Enrich carbon intensity data with power usage from Shelly data
	for i := range ciPerMinuteArray {
		ciPerMinuteArray[i].Power = int(shellyData.Data.DeviceStatus.Switch0.Apower)
	}

	// Create GCEnergyReporting instance
	report := external.GCEnergyReporting{
		Name:            function_id,
		ExecutionTime:   300,    // Example value
		ElectricityUsed: 0.0317, // Example value
		Cost:            2.90,   // Example value
		CITotal:         totalCarbonIntensity,
		CIPerMinute:     ciPerMinuteArray,
		//ShellyData:      shellyData.Data,
	}

	// Set header and return the GCEnergyReporting object as JSON
	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(report); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

type MyResp struct {
	TotalCarbonIntensity int `json:"total_carbon_intensity"`
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.Write([]byte("Hello, world!"))
}
