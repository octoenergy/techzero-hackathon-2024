package models

import (
	"time"
)

type CarbonResponse struct {
	Data CarbonIntensityResponse `json:"data"`
}

type CarbonIntensityResponse struct {
	RegionId  int    `json:"regionid"`
	Shortname string `json:"shortname"`
	Postcode  string `json:"postcode"`
	Data      []Data `json:"data"`
}

type Data struct {
	From          string          `json:"from"`
	To            string          `json:"to"`
	Intensity     Intensity       `json:"intensity"`
	GenerationMix []GenerationMix `json:"generationmix"`
}

type Intensity struct {
	Forecast int    `json:"forecast"`
	Index    string `json:"index"`
}

type GenerationMix struct {
	Fuel string  `json:"fuel"`
	Perc float32 `json:"perc"`
}

type MyResponse struct {
	Name            string       `json:"name" fake:"{firstname}"`
	TimeTaken       int          `json:"time_taken" fake:"{number:1,1000}"`
	ElectricityUsed string       `json:"electricity_used" fake:"{number:1,1000}"`
	Cost            float32      `json:"cost" fake:"{number:1,1000}"`
	CarbonIntensity int          `json:"carbon_intensity" fake:"{number:1,1000}"`
	MemoryUsed      string       `json:"memory_used" fake:"{number:1,1024}"`
	TimeSeries      []TimeSeries `json:"timeseries" fakesize:"2,10"`
}

type TimeSeries struct {
	Timestamp       time.Time `json:"timestamp"`
	ElectricityUsed string    `json:"electricity_used" fake:"{number:1,1000}"`
	Cost            float32   `json:"cost" fake:"{price:1,100}"`
	CarbonIntensity string    `json:"carbon_intensity" fake:"{number:1,1000}"`
	MemoryUsed      string    `json:"memory_used" fake:"{number:1,1024}"`
}
