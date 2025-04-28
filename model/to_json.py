import json

class To_json:
    @staticmethod
    def save_object(objeto, saida):
        try:
            with open(saida, 'r', encoding='utf-8') as file:
                dados_existentes = json.load(file)
                if not isinstance(dados_existentes, list):
                    dados_existentes = [dados_existentes]
        except (FileNotFoundError, json.JSONDecodeError):
            dados_existentes = []
        dados_existentes.append(objeto.__dict__)
        with open(saida, 'w', encoding='utf-8') as file:
            json.dump(dados_existentes, file, indent=4)

    @staticmethod
    def save_users(users, saida):
        try:
            with open(saida, 'w', encoding='utf-8') as file:
                json.dump(users, file, indent=4)
        except Exception as e:
            raise Exception(f"Erro ao salvar usuários: {e}")

    @staticmethod
    def load_users(saida):
        try:
            with open(saida, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
