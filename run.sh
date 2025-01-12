#!/bin/bash

# Nome da pasta e arquivos
APP_NAME="convert_file"
APP_DIR="$HOME/.${APP_NAME}"
MAIN_SCRIPT="main.sh"
BIN_NAME="ConvertFile"
BIN_PATH="/usr/local/bin/$BIN_NAME"

# Verifique se o script principal existe
if [ ! -f "$MAIN_SCRIPT" ]; then
  echo "Erro: O arquivo $MAIN_SCRIPT não foi encontrado."
  exit 1
fi

# Crie o diretório para armazenar o aplicativo no diretório home do usuário
if [ ! -d "$APP_DIR" ]; then
  echo "Criando diretório $APP_DIR..."
  mkdir -p "$APP_DIR"
fi

# Copie os arquivos do repositório para a pasta ~/.NameApp
echo "Copiando arquivos para $APP_DIR..."
cp -r ./* "$APP_DIR/"

# Torne o script principal executável
chmod +x "$APP_DIR/$MAIN_SCRIPT"

# Crie o link simbólico no diretório /usr/local/bin para facilitar a execução
if [ -f "$BIN_PATH" ]; then
  echo "Aviso: O link simbólico $BIN_PATH já existe. Substituindo..."
  sudo rm "$BIN_PATH"
fi
echo "Criando link simbólico para $BIN_PATH..."
sudo ln -s "$APP_DIR/$MAIN_SCRIPT" "$BIN_PATH"

# Informações finais
echo "O aplicativo foi instalado em $APP_DIR."
echo "Agora você pode executar o aplicativo com o comando '$BIN_NAME' em seu terminal."