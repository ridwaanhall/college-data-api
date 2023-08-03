from flask import Flask, request, redirect, url_for, jsonify
from urllib.parse import quote
from Controller import MahasiswaController, PerguruanTinggiController

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "url : ridwaanhall"

@app.route('/hit_mhs', methods=['GET', 'POST'])
def hit_mhs():
  if request.method == 'POST':
    # Get the input from the form
    mahasiswa = request.form['mahasiswa']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('hit_mhs_mhs', mahasiswa=mahasiswa))
  else:
    # Display the input form
    return '''
    <h2>bisa input NIM, nama, nama + kampus, dll.</h2>
    <form method="post" action="/hit_mhs">
      <label for="mahasiswa">Mahasiswa:</label>
      <input type="text" id="mahasiswa" name="mahasiswa" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/hit_mhs/<string:mahasiswa>', methods=['GET'])
def hit_mhs_mhs(mahasiswa):
  # Encode the mahasiswa parameter to handle special characters
  encoded_mahasiswa = quote(mahasiswa)
  # Use the encoded_mahasiswa as input for the MahasiswaController.hit_mhs() function
  data = MahasiswaController.hit_mhs(encoded_mahasiswa)
  return jsonify(data)

@app.route('/data_mahasiswa', methods=['GET', 'POST'])
def data_mahasiswa_home():
  if request.method == 'POST':
    # Get the input from the form
    id_mahasiswa = request.form['id_mahasiswa']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_mahasiswa', id_mahasiswa=id_mahasiswa))
  else:
    # Display the input form
    return '''
    <h2>input id mahasiswa</h2>
    <form method="post" action="/data_mahasiswa">
      <label for="mahasiswa">id mahasiswa:</label>
      <input type="text" id="id_mahasiswa" name="id_mahasiswa" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_mahasiswa/<string:id_mahasiswa>', methods=['GET'])
def data_mahasiswa(id_mahasiswa):
  data = MahasiswaController.data_mahasiswa(id_mahasiswa)
  return jsonify(data)

@app.route('/load_pt', methods=['GET'])
def load_pt():
  data = PerguruanTinggiController.load_pt()
  return jsonify(data)

@app.route('/data_pt/<string:link_pt>', methods=['GET'])
def data_pt(link_pt):
  data = PerguruanTinggiController.data_pt(link_pt)
  return jsonify(data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)