# TechZeroBE
A back end API for the Tech Zero hackathon

## Usage
- Make sure you have Go 1.22.4 or above installed.
- Use `go run *.go` (or `make up` with Make installed) to run the application

## Development
- If you have `make` installed, you can use `make lint` to run `golangci-lint run`

## Endpoints
`GET /health`
- This is a health check route.
  
`GET /my_response`
- Returns some dummy data.
  
`GET /energy`
- Inputs:
  - `from` (URL query parameter, can take a date or ISO8601 time)
  - `to` (URL query parameter, can take a date or ISO8601 time)
  - `functionId` (URL query parameter, just put whatever you want here)
- Outputs:
  - An object array where each object has the following fields:
    - `timestamp` (an ISO8601 compliant timestamp)
    - `carbon_intensity` (an integer representing grams of carbon intensity per kilowatt hour)

- Example:
   http://localhost:8080/energy?from=2023-06-01T06:00:00Z&to=2023-06-01T18:00:00Z&functionId=667aa0c384809f8a29ddc2f9