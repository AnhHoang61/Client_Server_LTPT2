import socket
import threading


def handle_client(client_socket, client_address):
    print(f"Đã chấp nhận kết nối từ {client_address}")

    # Nhận mảng từ client
    data = client_socket.recv(4096).decode('utf-8')
    print(f"Đã nhận dữ liệu từ {client_address}: Mảng: {data}")

    # Chuyển đổi chuỗi nhận được trở lại thành danh sách các số nguyên
    array = list(map(int, data.split()))

    #  Tính tổng mảng
    result = sum(array)

    # Gửi kết quả lại cho client
    client_socket.send(str(result).encode('utf-8'))

    # Đóng kết nối
    client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    # print("Server đang lắng nghe trên cổng 9999")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    main()
