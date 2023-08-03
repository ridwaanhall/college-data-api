import requests

def data_dosen(link_dosen):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/detail_dosen/{link_dosen}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
