from category import Category
from client import Client

def main():
    categoria = Category(1234, "Ferramentas", "Categoria que representa ferramentas")
    categoria.list_category_info()
    
    client_obj = Client("Gustavo", "Dias", "Rua A, 22", 51935728356, "gustavo.dias@gmail.com", "M")
    client_obj.change_cellphone(51910001000)

if __name__ == "__main__":
    main()