
import zipfile
import os

def extract_zip(zip_path, extract_path='./'):
    """
    Extrai um arquivo ZIP para o diretório especificado
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        print(f"Arquivo extraído para: {extract_path}")

# Exemplo de uso
if __name__ == "__main__":
    zip_file = "./attached_assets/Bibliometa.zip"
    extract_zip(zip_file, "./bibliometa")
