from client import Client

def main():
    client_obj = Client("Gustavo", "Dias", "Rua A, 22", 51935728356, "gustavo.dias@gmail.com", "M")
    client_obj.change_cellphone(51910001000)


if __name__ == "__main__":
    main()