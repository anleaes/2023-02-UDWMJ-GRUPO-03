class SocialNetwork:

    def __init__(self, name, description):
        self._name = name
        self._description = description

    def show_name(self):
        print(f"Name: {self._name}")

    def show_description(self):
        print(f"Description: {self._description}")