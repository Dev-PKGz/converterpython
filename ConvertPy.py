import os
import subprocess
import sys

def verificar_instalacao_pyinstaller():
    try:
        # Tenta importar o PyInstaller
        import PyInstaller
        print("PyInstaller já está instalado.")
    except ImportError:
        print("PyInstaller não está instalado. Instalando agora...")
        # Tenta instalar o PyInstaller usando pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def criar_executavel():
    try:
        # Pede ao usuário para digitar o nome do script Python
        nome_do_script = input("Digite o nome do script Python (ex: meu_script.py): ")

        # Verifica se o arquivo existe e se está no mesmo diretório
        if not os.path.exists(nome_do_script):
            print(f"O arquivo {nome_do_script} não foi encontrado.")
            return

        # Verifica se o nome do script termina com .py
        if not nome_do_script.endswith('.py'):
            print("O arquivo fornecido não é um script Python.")
            return

        # Mostra a mensagem de progresso
        print("Conversão em andamento, aguarde...")

        # Comando para converter o script em executável usando PyInstaller
        comando = ['pyinstaller', '--onefile', nome_do_script]

        # Executa o comando sem exibir a saída e os erros (stdout e stderr são redirecionados para DEVNULL)
        with open(os.devnull, 'w') as null:
            subprocess.call(comando, stdout=null, stderr=null)

        # Mensagem de sucesso
        print(f"Arquivo executável criado com sucesso para {nome_do_script}. Verifique a pasta 'dist'.")

        # Espera o usuário apertar qualquer tecla para finalizar
        input("Para finalizar, aperte qualquer tecla...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Verifica se o PyInstaller está instalado e instala se necessário
    verificar_instalacao_pyinstaller()
    
    # Inicia o processo de criação do executável
    criar_executavel()
