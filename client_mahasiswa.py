# Import library http client dan json
import http.client
import json

# Inisialisasi ip dan port server
ip_server = "127.0.0.1"
port_server = 7777

# 1. Fungsi menambhakan data mahasiswa
def add_mahasiswa():
    # Membuat koneksi http client ke ip dan port server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Mendefinisikan header HTTP
    header = {"Content-Type" : "application/json"}
    #Definisi data yang akan ditambahkan
    mhs = {
        "nim" : 110,
        "nama": "Reza"
    }
    # Convert data dictionary menjadi string
    json_mahasiswa = json.dumps(mhs)
    # Mengirim request ke server dengan method POST
    conn.request("POST", "/mahasiswa", json_mahasiswa, header)
    # Mendapatkan respon dari server
    data = conn.getresponse().read()
    # Decode data respon server
    data = data.decode('ascii')
    # Cetak data respon server
    print(data)

# 2. Fungsi untuk mengupdate data mahasiswa berdasarkan ID
def update_mahasiswa(id):
    # Membuat koneksi http client ke ip dan port server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Mendefinisikan header HTTP
    header = {"Content-Type" : "application/json"}
    # Data baru yang akan menggantikan data lama
    mhs = {
        "nama": "Nanda"
    }
    # Convert data dictionary menjadi string
    json_mahasiswa = json.dumps(mhs)
    # Mengirim request ke server dengan method PUT dengan input ID
    conn.request("PUT", "/mahasiswa/"+ str(id), json_mahasiswa, header)
    # Mendapatkan respon dari server
    data = conn.getresponse().read()
    # Decode data respon server
    data = data.decode('ascii')
    # Cetak data respon server
    print(data)

# 3. Hapus data mahasiswa berdasarkan ID
def del_mahasiswa(id):
    # Membuat koneksi http client ke ip dan port server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Mengirim request ke server dengan method DELETE dengan input ID
    conn.request("DELETE", "/mahasiswa/"+str(id))
    # Mendapatkan respon dari server
    data = conn.getresponse().read()
    # Decode data respon server
    data = data.decode('ascii')
    # Cetak data respon server
    print(data)

# 4. Fungsi mendapatkan semua data mahasiswa
def get_mahasiswa():
    # Membuat koneksi http client ke ip dan port server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Mengirim request ke server dengan method GET
    conn.request("GET", "/mahasiswa")
    # Mendapatkan respon dari server
    data = conn.getresponse().read()
    # Decode data respon server
    data = data.decode('ascii')
    # Cetak data respon server
    print(data)

# 5. Mendapatkan 1 data mahasiswa berdasarkan ID
def get_one_mahasiswa(id):
    # Membuat koneksi http client ke ip dan port server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Mengirim request ke server dengan method GET dengan input ID
    conn.request("GET", "mahasiswa/"+str(id))
    # Mendapatkan respon dari server
    data = conn.getresponse().read()
    # Decode data respon server
    data = data.decode('ascii')
    # Cetak data respon server
    print(data)

add_mahasiswa()
update_mahasiswa(234)
del_mahasiswa(123)
get_mahasiswa()
get_one_mahasiswa(234)
