class ClientSocialNetwork:
    
    def __init__(self, client, social_network):
        self._client = client
        self._social_network = social_network
    

    def show_client_name_and_social_network(self):
        print(f"Client name: {self._client._first_name} {self._client._last_name}")
        print(f"Social Network: {self._social_network._name}")