import requests
from urllib.parse import unquote

def hit(dsn_prodi_pt):
    # Decode the encoded dsn_prodi_pt parameter
    decoded_dsn_prodi_pt = unquote(dsn_prodi_pt)
    try:
        url = f"https://api-frontend.kemdikbud.go.id/hit/{decoded_dsn_prodi_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}