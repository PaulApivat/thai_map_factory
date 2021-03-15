# Thai Map Factory

Using Google Maps API to locate factories in Thailand

## Motivation

1. Broadly, to see how _data_ can be used to address air pollution.
2. To obtain factory coordinates in Thailand.
3. To see data contained in Pollutant Release and Transfer Register and see what we can start with.

### Outcome

To see if we can build a proxy PRTR dataset for Thailand.

### Phase 1

### Phase 2

## Code, Libraries and Resources Used

### Documentation

### Python

### R

## Documenting Progress

## Getting Data

### Google Places API

1. Consult [documentation](https://developers.google.com/maps/documentation/places/web-service/search) for "Nearby Search Requests" in Places API.
2. Example API call:

https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY

3. Parameters for the API call include:

- location (lat,long)
- key=YOUR_API_KEY
- type=factory
- keyword=chemical

### Coordinates for Thai Cities

For initial prototyping, this is a small 16 city sample from LatLong.net

## EDA

### Visualization

## Analysis

## Results

## Presentation / Productionization
