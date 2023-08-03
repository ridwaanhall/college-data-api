import requests

def load_pt():
    try:
        url = "https://api-frontend.kemdikbud.go.id/loadpt"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}

def data_pt(link_pt):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/v2/detail_pt/{link_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}

def data_pt_prodi(link_pt):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/v2/detail_pt_prodi/{link_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
    
def data_pt_jumlah(link_pt):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/v2/detail_pt_jumlah/{link_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
    
def data_pt_dosen(link_pt):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/v2/detail_pt_dosen/{link_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}
    
def stat_pt(link_pt):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/stat_pt/{link_pt}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}