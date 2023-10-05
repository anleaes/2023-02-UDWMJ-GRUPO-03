class Category:
   
    def __init__(self, id, name, description):
       self._id = id
       self._name = name
       self._description = description
    
    
    def list_category_info(self):
        print(f"\nCategoria: {self._name}")
        print(f"Descrição: {self._description}")
    