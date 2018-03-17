# Import Library flask, request dan json
from flask import Flask, request
import json

# Nama Flask
app = Flask("Web App Mahasiswa")

# Data Mahasiswa
data_mahasiswa = [
    {
        "nim": 123,
        "nama": "Andi"
    },
    {
        "nim": 234,
        "nama": "Budi"
    }
]
# Deklarasi routing dengan method POST dan mendefinisikan fungsi
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    # Inisialisasi variabel nim dan nama yang direquest dari data json
    nim = request.json['nim']
    nama = request.json['nama']
    # Data baru yang akan ditambahkan
    mhs_baru = {
        "nim": nim,
        "nama": nama
    }
    # Menmabhakan nilai baru pada data mahasiswa
    data_mahasiswa.append(mhs_baru)
    # Mengembalikan string OK
    return "OK"

# Deklarasi routing dengan method PUT dan mendefinisikan fungsi
@app.route('/mahasiswa/<int:id>', methods=['PUT'])
def update_data_mahasiswa(id):
    # Inisialisasi variabel nama yang direquest dari data mahasiswa
    nama = request.json["nama"]
    # Seleksi kondisi untuk memilih data yang akan dirubah berdasarkan ID
    if data_mahasiswa[0]["nim"] == id:
        data_mahasiswa[0]["nama"] = nama
    elif data_mahasiswa[1]["nim"] == id:
        data_mahasiswa[1]["nama"] = nama
    # Mengembalikan nilai balik berupa string
    return "Data diupdate pada nim : " + str(id)

# Deklarasi routing dengan method DELETE dan mendefinisikan fungsi
@app.route('/mahasiswa/<int:id>', methods=['DELETE'])
def delete_mahasiswa(id):
    # Melakukan proses seleksi kondisi untuk menentukan data yang akan dihapus berdasarkan ID
    if data_mahasiswa[0]["nim"] == id:
        del data_mahasiswa[0]
    elif data_mahasiswa[1]["nim"] == id:
        del data_mahasiswa[1]
    else:
        print("Id not found")
    # Mengembalikan nilai balik berupa string
    return "Data dihapus pada nim : " + str(id)

# Deklarasi routing dengan method GET dan mendefinisikan fungsi
@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    # Inisialisasi variabel dengan nilai berupa hasil convert data dictionary menjadi string
    json_mahasiswa = json.dumps(data_mahasiswa)
    # Mengembalikan nilai balik berupa data yang diambil
    return json_mahasiswa

# Deklarasi routing dengan method GET dan mendefinisikan fungsi
@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_one_mahasiswa(id):
    # Seleksi kondisi untuk menentukan data yang akan ditampilkan berdasarkan ID serta mengembalikan nilai balik
    # berupa data yang dipilij
    if data_mahasiswa[0]["nim"] == id:
        one_mahasiswa = json.dumps(data_mahasiswa[0])
        return one_mahasiswa
    elif data_mahasiswa[1]["nim"] == id:
        one_mahasiswa = json.dumps(data_mahasiswa[1])
        return one_mahasiswa
    else:
        print("Id not found")

# Menjalakan program pada port tertentu
app.run(port=7777)