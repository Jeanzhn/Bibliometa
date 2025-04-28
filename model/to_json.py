import json

<<<<<<< HEAD
class To_json:
    @staticmethod
    def save_object(objeto, saida):
        try:
            dados_existentes = []
            try:
                with open(saida, 'r', encoding='utf-8') as file:
=======
def To_json():
    def to_json(self, saida):
        try:
            dados_existentes = []
            try:
                with open(saida, 'r') as file:
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
                    dados_existentes = json.load(file)
                    if not isinstance(dados_existentes, list):
                        dados_existentes = [dados_existentes]
            except (FileNotFoundError, json.JSONDecodeError):
                dados_existentes = []
<<<<<<< HEAD
            dados_existentes.append(objeto.__dict__)
            with open(saida, 'w', encoding='utf-8') as file:
                json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
        except TypeError as e:
            raise TypeError(f"Erro ao converter para JSON: {e}")

    @staticmethod
    def save_users(arquivo, users):
        try:
            with open(arquivo, 'w', encoding='utf-8') as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
        except Exception as e:
            raise Exception(f"Erro ao salvar usuários: {e}")

    @staticmethod
    def load_users(arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
=======
            dados_existentes.append(self.__dict__)
            with open(saida, 'w') as file:
                json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
        except TypeError as e:
            raise TypeError(f"Erro ao converter para JSON: {e}")
        
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
