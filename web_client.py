import socket

def client_program():
    serverAddress = "localhost" # alamat server
    serverPort = 8000  # nomor port server

    clientSocket = socket.socket()  # instantiate
    clientSocket.connect((serverAddress, serverPort))  # connect ke server

    file = "index.html" # nama file html yang direquest

    clientSocket.send(f'GET /{file} HTTP/1.1\r\nHost: {serverAddress}:{serverPort}\r\n\r\n'.encode()) # mengirim request file dengan protokol dan alamat serta port server

    message = "" # variabel untuk menyimpan response dari server
    while True: # looping untuk menerima reponse dari server
        clientSocket.settimeout(5) # jika tidak ada data baru yang masuk dalam lima detik, maka berhenti menerima data dari server
        new = clientSocket.recv(1024).decode() # decode data yang diterima dan diubah menjadi string agar bisa diprint
        message = message + new # menambahkan data baru ke data yang lama
        if len(new) == 0: # jika tidak ada data baru (artinya semua data sudah diterima), maka keluar dari looping
            break # keluar dari looping
    print("Response:", message) # print response dari server

    clientSocket.close()  # menutup koneksi dengan server


if __name__ == '__main__':
    client_program()