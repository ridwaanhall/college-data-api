from flask import Flask, request, redirect, url_for, jsonify
from urllib.parse import quote
from Controller import MahasiswaController, PerguruanTinggiController

app = Flask(__name__)

@app.route("/")
def home():
  return {
    'owner': [
      {
      'name'   : 'Ridwan Halim',
      'address': 'Madinah, Saudi Arabia',
      'my_wife': 'Hafidhah Afkariana'
      }
    ],
    'social media': [
      {
      'instagram': 'https://www.instagram.com/ridwaanhall',
      'facebook' : 'https://www.facebook.com/ridwaanhall',
      'tiktok'   : 'https://www.tiktok.com/@ridwaanhall',
      'twitter'  : 'https://twitter.com/ridwaanhall',
      'threads'  : 'https://www.threads.net/@ridwaanhall',
      'linkedin' : 'https://www.linkedin.com/in/ridwaanhall',
      'github'   : 'https://github.com/ridwaanhall',
      'replit'   : 'https://replit.com/@ridwaanhall',
      'telegram' : 'https://t.me/ridwaanhall'
      }
    ]
  }

@app.route('/hit_mhs', methods=['GET', 'POST'])
def hit_mhs():
  if request.method == 'POST':
    # Get the input from the form
    mahasiswa = request.form['mahasiswa']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('hit_mhs_detail', mahasiswa=mahasiswa))
  else:
    # Display the input form
    return '''
    <p>bisa input NIM, nama, nama + kampus, dll.</p>
    <form method="post" action="/hit_mhs">
      <label for="mahasiswa">Mahasiswa:</label>
      <input type="text" id="mahasiswa" name="mahasiswa" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/hit_mhs/<string:mahasiswa>', methods=['GET'])
def hit_mhs_detail(mahasiswa):
  encoded_mahasiswa = quote(mahasiswa)
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
    <p>input id mahasiswa</p>
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

@app.route('/data_pt', methods=['GET', 'POST'])
def data_pt():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt">
      <label for="link_pt">Mahasiswa:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt/<string:link_pt>', methods=['GET'])
def data_pt_detail(link_pt):
  data = PerguruanTinggiController.data_pt(link_pt)
  return jsonify(data)

@app.route('/data_pt_prodi', methods=['GET', 'POST'])
def data_pt_prodi():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_prodi_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_prodi">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_prodi/<string:link_pt>', methods=['GET'])
def data_pt_prodi_detail(link_pt):
    data = PerguruanTinggiController.data_pt_prodi(link_pt)
    return jsonify(data)

@app.route('/data_pt_jumlah', methods=['GET', 'POST'])
def data_pt_jumlah():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_jumlah_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_jumlah">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_jumlah/<string:link_pt>', methods=['GET'])
def data_pt_jumlah_detail(link_pt):
    data = PerguruanTinggiController.data_pt_jumlah(link_pt)
    return jsonify(data)

@app.route('/data_pt_dosen', methods=['GET', 'POST'])
def data_pt_dosen():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_dosen_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_dosen">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_dosen/<string:link_pt>', methods=['GET'])
def data_pt_dosen_detail(link_pt):
    data = PerguruanTinggiController.data_pt_dosen(link_pt)
    return jsonify(data)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)