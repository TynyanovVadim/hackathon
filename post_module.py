import requests

def get_adresses(lat, lon, radius):
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": "Token 6c720422292d7d674024c2413379ea5d9a9d44d1" }
    api_adresses = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/address"
    api_geo_post = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/postal_unit"
    api_code_post = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/postal_unit"

    params = {"lat": lat, "lon": lon, "radius_meters": radius}

    post = requests.get(api_geo_post, headers=headers, params=params)
    adresses = requests.get(api_adresses, params=params, headers=headers)

    if (not post.ok and not adresses.ok) or \
       (not post.json()["suggestions"] and not adresses.json()["suggestions"]):
        return {}, {}

    if (not post.json()["suggestions"]):
        params = {"query": adresses.json()["suggestions"][0]["data"]["postal_code"]}
        post = requests.get(api_code_post, headers=headers, params=params) 

    if (adresses.ok and post.ok):
        return adresses.json(), post.json()

