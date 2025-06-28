
# Comparação entre RSA e Kyber512

Este projeto realiza uma comparação prática entre o algoritmo de criptografia clássico RSA e o algoritmo pós-quântico Kyber512, avaliando tempo de execução, tamanho das chaves e viabilidade de uso.

## 📦 Pré-requisitos

Antes de rodar o código, é necessário ter os seguintes itens instalados no sistema:

* **Python 3.8+**
* **pip**
* **Virtualenv** (opcional, mas recomendado)

### 🧰 Bibliotecas necessárias

Instale as dependências principais:


pip install pycryptodome
pip install oqs

Se estiver usando um ambiente Linux (como Ubuntu ou Kali), pode ser necessário instalar o `liboqs`:

sudo apt update
sudo apt install cmake gcc python3-dev
git clone --depth 1 https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
python3 setup.py install

## ⚙️ Como executar

Crie  um ambiente virtual:

python3 -m venv venv
source venv/bin/activate

Execute o script:

python RSAvsKyber512.py

## 📋 O que o código faz?

* Gera chaves RSA (2048 bits) e simula uma criptografia e descriptografia.
* Executa o algoritmo Kyber512 (pós-quântico) usando encapsulamento/decapsulamento.
* Compara o tempo de execução e o tamanho das chaves.

## 🧪 Saída esperada

=== ALGORITMO CLÁSSICO: RSA ===
Tempo de execução (RSA): ...
Tamanho da chave pública (RSA): ...
Mensagem decifrada: ...

=== ALGORITMO PÓS-QUÂNTICO: Kyber512 ===
Tempo de execução (Kyber512): ...
Tamanho da chave pública (Kyber512): ...
Segredo compartilhado (decifrado): ...
