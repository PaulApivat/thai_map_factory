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

1. Using API Keys ([link](https://developers.google.com/maps/documentation/places/web-service/get-api-key))
2. Getting started with Google Maps Platform ([link](https://developers.google.com/maps/gmp-get-started#api-key))
3. Place Search ([link](https://developers.google.com/maps/documentation/places/web-service/search))
4. Google Cloud Platform [link](https://console.cloud.google.com/)

### Other Resources

1. Google Maps Data API YouTube clip from [Stevesie Data](https://www.youtube.com/watch?v=tj6vjmqQTvg)
2. Stevesie Google Maps Data Scraping API ([wrapper](https://stevesie.com/apps/google-maps-api))
3. Stevesie Google Maps Nearby Place Search - Data API Endpoint ([link](https://stevesie.com/apps/google-maps-api/nearby-place-search))
4. Most comprehensive Lat/Long info for Thailand courtesy of [Spicydog](https://github.com/spicydog/thailand-province-district-subdistrict-zipcode-latitude-longitude)
5. Thai Zip Code latitude and longitude JSON [link](https://github.com/rathpanyowat/Thai-zip-code-latitude-and-longitude/blob/master/data.json)

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
- radius (in meters; 50k max)

### Coordinates for Thai Cities

For initial prototyping, this is a small 16 city sample from [LatLong.net](https://www.latlong.net/category/cities-221-15.html)

## EDA

### Visualization

## Analysis

## Results

## Presentation / Productionization
