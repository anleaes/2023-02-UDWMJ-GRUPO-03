class Client:
   
    def __init__(self, first_name, last_name, adress, cell_phone, email, gender):
       self._first_name = first_name
       self._last_name = last_name
       self._adress = adress
       self._cell_phone = cell_phone
       self._email = email
       self._gender = gender

    def change_cellphone(self, new_cellphone):
        self._cell_phone = new_cellphone
        print(f"\nCellphone number changed! Your new number is: {self._cell_phone}")