import socket
import random


def generate_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    # Tạo một mảng ngẫu nhiên với N > 100 phần tử
    n = 10
    array = generate_random_array(n)
    array_str = ' '.join(map(str, array))
    print("Mảng khởi tạo", array)
    # Gửi mảng đến server
    client.send(array_str.encode('utf-8'))

    # Nhận kết quả từ server
    result = client.recv(4096).decode('utf-8')

    # Hiển thị kết quả
    print(f"Đã nhận kết quả từ server: {result}")

    # Đóng kết nối
    client.close()


if __name__ == "__main__":
    main()
