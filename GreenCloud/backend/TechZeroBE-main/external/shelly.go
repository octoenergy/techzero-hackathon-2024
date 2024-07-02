package external

import (
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"strings"
)

type ShellyAPIClient struct {
	ApiKey string
}

func (s *ShellyAPIClient) SetAPIKey(key string) {
	s.ApiKey = key
}

func (s *ShellyAPIClient) Fetch(id string) ShellyResponse {
	// Encode the request parameters as x-www-form-urlencoded
	data := url.Values{}
	data.Set("auth_key", s.ApiKey)
	data.Set("id", id)

	encodedData := data.Encode()
	resp, err := http.Post("https://shelly-100-eu.shelly.cloud/device/status", "application/x-www-form-urlencoded", strings.NewReader(encodedData))

	if err != nil {
		fmt.Printf("Error while fetching Shelly data: %s", err)
		return ShellyResponse{}
	}
	defer resp.Body.Close()

	var result ShellyResponse
	err = json.NewDecoder(resp.Body).Decode(&result)
	if err != nil {
		fmt.Printf("Error while decoding response: %s", err)
	}

	return result
}

type ShellyRequest struct {
	ApiKey string `json: "auth_key"`
	Id     string `json: "id"`
}

type ShellyResponse struct {
	IsOk bool       `json:"is_ok"`
	Data ShellyData `json:"data"`
}

type ShellyData struct {
	DeviceStatus DeviceStatus `json:"device_status"`
}

type DeviceStatus struct {
	Switch0 Switch `json:"switch:0"`
}

type Switch struct {
	Aenergy Aenergy `json:"aenergy"`
	Apower  float32 `json:"apower"`
}

type Aenergy struct {
	ByMinute []float64 `json:"by_minute"`
	MinuteTS int       `json:"minute_ts"`
	Total    float64   `json:"total"`
}
