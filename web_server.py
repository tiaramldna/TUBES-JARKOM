from socket import * #membuat socket pada program
import sys #terminasi program
serverSocket = socket(AF_INET, SOCK_STREAM) #pembuatan socket server dengan 2 parameter yang pertama adalah AF_INET (menggunakanprotokol Ipv4), yang kedua yaitu SOCK_STREAM (yang berarti soket TCP (bukan soket UDP)
serverAddress = "localhost" # alamat server
serverPort = 8000  # nomor port server
serverSocket.bind((serverAddress, serverPort)) #menetapkan alamat server dan nomor port 8000 ke socket server
serverSocket.listen(1) #membuat server mendengarkan permintaan koneksi TCP dari klien dengan jumlah maksimum koneksi antrian setidaknya 1
while True: #sebuah fungsi yang akan berjalan jika kondisi di atas true atau benar
    print('Ready to serve...') #mencetak string 'Ready to serve'
    connectionSocket, addr = serverSocket.accept() #memanggil accept untuk serversocket dimana akan membuat soket baru di server yaitu connectionsocket
    try:
        message = connectionSocket.recv(1024).decode() #menerima pesan permintaan dari client
        filename = message.split()[1] #memecah pesan request client untuk mengambil data kedua yang berisi nama file html yang diminta
        f = open(filename[1:]) #membuka file
        outputdata = f.read() #read file html
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) #mengirim satu baris header dari HTTP ke socket
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode()) #mengirim isi file yang diminta ke klien
        for i in range(0, len(outputdata)): #perulangan untuk mengirimkan data file html ke client
            connectionSocket.send(outputdata[i].encode()) #mengirimkan data html ke client
        connectionSocket.send("\r\n".encode()) #mengirimkan baris kosong
        connectionSocket.close() #menutup koneksi socket
    except IOError:
        connectionSocket.send("HTTP/1.1 404 File Not Found\r\n".encode()) #mengirim pesan respon jika file tidak ditemukan atau not found
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode()) #memberi info ke browser bahwa server akan mengirimkan file html
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode()) #mengirimkan codingan html agar pada browser terlihat pesan error
    connectionSocket.close() #menutup koneksi socket
serverSocket.close() #menutup socket server
sys.exit() #keluar dari program 
