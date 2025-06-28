# === Importação das bibliotecas === 

from Crypto.PublicKey import RSA # Para geração de chaves RSA 

from Crypto.Cipher import PKCS1_OAEP # Para cifra RSA com padding OAEP 

from oqs import KeyEncapsulation # Para usar algoritmos pós-quânticos como Kyber 

import time # Para medir o tempo de execução 

 

# === Mensagem que será criptografada === 

mensagem = b'Teste de criptografia para TCC.' 

 

# === ALGORITMO CLÁSSICO: RSA === 

print("=== ALGORITMO CLÁSSICO: RSA ===") 

 

inicio_rsa = time.time() 

 

# Geração de par de chaves RSA (2048 bits) 

chave_rsa = RSA.generate(2048) 

chave_publica = chave_rsa.publickey() 

cifra_rsa = PKCS1_OAEP.new(chave_publica) 

 

# Criptografia da mensagem 

mensagem_criptografada = cifra_rsa.encrypt(mensagem) 

 

# Descriptografia da mensagem 

decifra_rsa = PKCS1_OAEP.new(chave_rsa) 

mensagem_decifrada = decifra_rsa.decrypt(mensagem_criptografada) 

 

fim_rsa = time.time() 

 

# Exibição dos resultados do RSA 

print(f"Tempo de execução (RSA): {fim_rsa - inicio_rsa:.4f} s") 

print(f"Tamanho da chave pública (RSA): {len(chave_publica.export_key())} bytes") 

print(f"Mensagem decifrada: {mensagem_decifrada.decode()}") 

 

# === ALGORITMO PÓS-QUÂNTICO: Kyber512 === 

print("\n=== ALGORITMO PÓS-QUÂNTICO: Kyber512 ===") 

 

inicio_kyber = time.time() 

 

# Inicializa o algoritmo de encapsulamento de chave Kyber512 

with KeyEncapsulation('Kyber512') as kem: 

public_key = kem.generate_keypair() # Gera par de chaves 

ciphertext, shared_secret_enc = kem.encap_secret(public_key) # Encapsulamento 

shared_secret_dec = kem.decap_secret(ciphertext) # Decapsulamento 

 

fim_kyber = time.time() 

 

# Exibição dos resultados do Kyber512 

print(f"Tempo de execução (Kyber512): {fim_kyber - inicio_kyber:.4f} s") 

print(f"Tamanho da chave pública (Kyber512): {len(public_key)} bytes") 

print(f"Segredo compartilhado (decifrado): {shared_secret_dec.hex()[:32]}...") 
