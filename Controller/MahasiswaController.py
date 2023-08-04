import requests
from urllib.parse import unquote


def hit_mhs(mahasiswa):
  # Decode the encoded mahasiswa parameter
  decoded_mahasiswa = unquote(mahasiswa)
  try:
    url = f"https://api-frontend.kemdikbud.go.id/hit_mhs/{decoded_mahasiswa}"
    response = requests.get(url)
    response.raise_for_status(
    )  # Raise an exception if the response status is not OK
    data = response.json()
    return data
  except requests.exceptions.RequestException:
    # If there is a network-related error, return a custom JSON response
    return {"message": "Internet is not available"}


def data_mahasiswa(id_mahasiswa):
  try:
    url = f"https://api-frontend.kemdikbud.go.id/detail_mhs/{id_mahasiswa}"
    response = requests.get(url)
    response.raise_for_status(
    )  # Raise an exception if the response status is not OK
    data = response.json()
    return data
  except requests.exceptions.RequestException:
    # If there is a network-related error, return a custom JSON response
    return {"message": "Internet is not available"}
