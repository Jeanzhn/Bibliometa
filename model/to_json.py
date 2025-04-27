import json

def To_json():
    def to_json(self, saida):
        try:
            dados_existentes = []
            try:
                with open(saida, 'r') as file:
                    dados_existentes = json.load(file)
                    if not isinstance(dados_existentes, list):
                        dados_existentes = [dados_existentes]
            except (FileNotFoundError, json.JSONDecodeError):
                dados_existentes = []
            dados_existentes.append(self.__dict__)
            with open(saida, 'w') as file:
                json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
        except TypeError as e:
            raise TypeError(f"Erro ao converter para JSON: {e}")

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

def load_users():
    with open('user.json', 'r') as f:
        return json.load(f)
        