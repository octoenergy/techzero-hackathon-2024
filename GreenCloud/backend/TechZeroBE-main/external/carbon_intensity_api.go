package external

import (
	"encoding/json"
	"fmt"

	"main/models"
	"net/http"
)

func GetCarbonIntensityApi(from string, to string, function_id string) models.CarbonResponse {

	url := fmt.Sprintf("https://api.carbonintensity.org.uk/regional/intensity/%s/%s/postcode/TF8", from, to)

	fmt.Println("\n" + url)

	resp, err := http.Get(url)

	if err != nil {
		fmt.Printf("Error while fetching carbon intensity data: %s", err)
	}

	fmt.Println(resp.Status)

	defer resp.Body.Close()

	var data models.CarbonResponse

	err = json.NewDecoder(resp.Body).Decode(&data)

	if err != nil {
		fmt.Printf("Error while fetching carbon intensity data: %s", err)
	}

	return data
}

func CalcCarbonIntensity(res models.CarbonIntensityResponse) (int, []CIPerMinute) {
	var arr []CIPerMinute
	totalCarbonIntensity := 0

	for _, datapoint := range res.Data {
		ci := CIPerMinute{
			Timestamp:       datapoint.From,
			CarbonIntensity: datapoint.Intensity.Forecast,
		}
		arr = append(arr, ci)
		totalCarbonIntensity += datapoint.Intensity.Forecast
	}

	return totalCarbonIntensity, arr
}

type CIPerMinute struct {
	Timestamp       string `json:"timestamp"`
	CarbonIntensity int    `json:"carbon_intensity"`
	Power           int    `json:"power_useage"`
}

type GCEnergyReporting struct {
	Name            string        `json:"name"`
	ExecutionTime   int           `json:"execution_time"`
	ElectricityUsed float32       `json:"electricity_used"`
	Cost            float32       `json:"cost"`
	CITotal         int           `json:"ci_total"`
	CIPerMinute     []CIPerMinute `json:"ci_per_minute"`
	//ShellyData      ShellyData    `json:"shelly_data"` // Add ShellyData field
}

// Name            string       `json:"name" fake:"{firstname}"`
// TimeTaken       int          `json:"time_taken" fake:"{number:1,1000}"`
// ElectricityUsed string       `json:"electricity_used" fake:"{number:1,1000}"`
// Cost            float32      `json:"cost" fake:"{number:1,1000}"`
// CarbonIntensity int          `json:"carbon_intensity" fake:"{number:1,1000}"`
// MemoryUsed      string       `json:"memory_used" fake:"{number:1,1024}"`
// TimeSeries      []TimeSeries `json:"timeseries" fakesize:"2,10"`
