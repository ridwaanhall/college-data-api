import requests

def load_prodi():
    try:
        url = "https://api-frontend.kemdikbud.go.id/loadprodi"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
    
def load_detail_prodi(id_sp):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/loadprodi/{id_sp}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}

def data_prodi(link_prodi):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/detail_prodi/{link_prodi}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
