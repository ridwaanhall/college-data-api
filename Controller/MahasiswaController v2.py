import requests
from urllib.parse import unquote

def hit_mhs(mahasiswa):
    # Decode the encoded mahasiswa parameter
    decoded_mahasiswa = unquote(mahasiswa)

    try:
        url = f"https://api-frontend.kemdikbud.go.id/hit_mhs/{decoded_mahasiswa}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}

    if "mahasiswa" not in data:
        # If "mahasiswa" field is not present in the JSON, return an empty list
        return {"mahasiswa": []}

    mahasiswa_list = []
    for mhs in data["mahasiswa"]:
        # Check if "text" and "website-link" fields are present
        if "text" in mhs and "website-link" in mhs:
            text = mhs["text"]
            if f"Cari kata kunci {mahasiswa} pada Data Mahasiswa" in text:
                # If the specific string is found in the "text" field, return an empty list
                return {"mahasiswa": []}

            nama_nipd, rest = text.split(", PT : ")

            # Check if ", Prodi: " is present in the rest string
            if ", Prodi: " in rest:
                pt_prodi_parts = rest.split(", Prodi: ")
                pt = pt_prodi_parts[0].strip()
                prodi = pt_prodi_parts[1].strip()
            else:
                pt = ""  # Set pt to an empty string if not available
                prodi = ""  # Set prodi to an empty string if not available

            website_link_parts = mhs["website-link"].split("/")
            link_mhs = website_link_parts[-1]

            nipd_start = nama_nipd.find("(") + 1
            nipd_end = nama_nipd.find(")")
            nipd = nama_nipd[nipd_start:nipd_end]

            mahasiswa_data = {
                "nipd": nipd,
                "nm_mhs": nama_nipd[:nipd_start - 1],
                "prodi": prodi,
                "pt": pt,
                "link_mhs": mhs["website-link"]
            }
            mahasiswa_list.append(mahasiswa_data)

    result = {"mahasiswa": mahasiswa_list}
    return result

def data_mahasiswa(link_mhs):
    try:
        url = f"https://api-frontend.kemdikbud.go.id/detail_mhs/{link_mhs}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not OK
        data = response.json()
    except requests.exceptions.RequestException:
        # If there is a network-related error, return a custom JSON response
        return {"message": "Internet is not available"}

    datastatuskuliah = data["datastatuskuliah"]
    datastudi = data["datastudi"]
    dataumum = data["dataumum"]

    # Remove the leading "/data_prodi/" and "/data_pt/" from link_prodi and link_pt
    #link_prodi = dataumum.get("link_prodi", "").split("/")[-1]
    #link_pt = dataumum.get("link_pt", "").split("/")[-1]

    result = {
        "datastatuskuliah": datastatuskuliah,
        "datastudi": datastudi,
        "dataumum": dataumum
    }
    return result
