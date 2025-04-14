import json

def To_json():
    def to_json(self, saida):
        try:
            json.dump(self.__dict__)
            with open(saida, 'w') as file:
                json.dump(self.__dict__, file, indent=4, ensure_ascii=False) #converte o dicionário em JSON e salva no arquivo
        except TypeError as e:
            raise TypeError(f"Erro ao converter para JSON: {e}")
        