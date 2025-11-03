# Décima segunda parte - Parte Final - o código completo funcional

# Importação das funções criandas anteriormente necessárias para o funcionamento da criptografia
from get_keys import gen_keys
from save_key import save_key
from load_key import load_key
from text_to_bytes import text_to_bytes
from bytes_to_text import bytes_to_text
from decrypt_text import decrypt
from encrypt_text import encrypt

# Garante que este arquivo sera executado diretamente
if __name__ == "__main__":

    # Ínicio do menu da criptografia
    while True:
        print("       Criptografia RSA")
        print("-" * 30)
        print("1. gerar chave publica e privada")
        print("2. para carregar últimas chaves salvas")
        print("3. codificar mensagem")
        print("4. decodificar mensagem")
        print("5. Como usar o programa - guia")
        print()
        # Seleção de opção
        opt = int(input("digite o número de sua opção: "))


        # Opção 1 - Gerar chaves
        if opt == 1:
            # armazena o retorno da função em variáveis
            chave_publica, chave_privada = gen_keys(bits=512)
            # salva as chaves em arquivos de texto
            save_key("chave_publica.txt", chave_publica)
            save_key("chave_privada.txt", chave_privada)
            print()
            print("--- CHAVES GERADAS ---")
            print()
            print("Sua chave pública é: ", chave_publica)
            print()
            print("Sua chave privada é: ", chave_privada)
            print()
            print("-" * 30)

            continue
        
        # Opção 2 - carregar últimas chaves geradas
        elif opt == 2:
            # Uso das funções de carregar chave
            load_key("chave_publica.txt")
            load_key("chave_privada.txt")
            print()
            print("Sua chave pública é: ", chave_publica)
            print()
            print("Sua chave privada é: ", chave_privada)
            print()
            print("-" * 30)
            continue
        
        # Opção 3 - Criptografia de mensagem
        elif opt == 3:
            
            # Garantia de que o loop continuará até que a mensagem seja escrita corretamente
            while True:
                print()
                mensagem = input("Digite uma mensagem para criptografar (máximo 128 caracteres): ")
        
                if mensagem.strip() == "":
                    print("A mensagem não pode estar vazia.")
                    continue
                if len(mensagem) > 128:
                    print("Mensagem passa do limite de caracteres")
                    continue
                break
            
            # Inserção dos valores da chave pública 
            e = int(input("Digite o valor de e: "))
            print()
            n = int(input("Digite o valor de n: "))
            chave_publica = (e, n)

            # garantia de que as chaves estão completas
            if chave_publica is None:
                print("Gere ou carregue as chaves primeiro (Opção 1 ou 2)")
                continue
            
            # Conversão da mensagem para bytes
            texto_byte = text_to_bytes(mensagem)
            # Criptografia da mensagem transformada em bytes através da chave publica
            mensagem_encriptada = encrypt(texto_byte, chave_publica)
            
            print("---CRIPTOGRAFIA BEM-SUCEDIDA---")
            print()
            print("Mensagem original: ", mensagem)
            print()
            print("Mensagem criptografada: ", mensagem_encriptada)
            print()
                   
        # Opção 4 - Descriptografia da mensagem
        elif opt == 4:

            while True:
                print()
                # Entrada da mensagem como "int" para funcionamento pleno da descriptografia
                mensagem_encriptada = int(input("Digite a mensagem a ser descriptografada: "))

                #garantia de entrada correta da mensagem
                if mensagem_encriptada == 0:
                    print("A mensagem não pode estar vazia.")
                    continue
                
                break
            print()
            d = int(input("Digite o valor de d: "))
            print()
            n = int(input("Digite o valor de n: "))
            print()
            chave_privada = (d, n)

            # Mensagem descriptografada em sua forma de bytes original
            bytes_texto = decrypt(mensagem_encriptada, chave_privada)
            # Mensagem Original descriptografada
            mensagem_descriptada = bytes_to_text(bytes_texto)
            
            print("---DESCRIPTOGRAFIA BEM-SUCEDIDA---")
            print()
            print("Mensagem original: ", mensagem_descriptada)
            print()
        
        # Opção 5 - Guia de interface e uso
        elif opt == 5:
            print()
            print("O funcionamento do programa é simples!")
            print("Primeiramente você precisa gerar suas chaves, tanto a pública e a privada(caso ainda não as tenha), estas chaves")
            print("funcionam como uma fechadura e uma chave, onde o que foi encriptado com a pública só se é desencriptada pela privada.")
            print("Para gerar suas chaves basta selecionar a opção -1- no menu do programa que as chaves irão aparecer.")
            print("Caso ja tenha sido geradas anteriormente, basta apertar -2- para as carregar novamente.")
            print("Cada chave possui dois valores, a chave pública, necessária pra criptografia, tem os valores -e- e -n- separados por vírgula,")
            print("e a chave privada, necessária para a descriptografia, tem os valores -d- e -n- também separados por vírgula.")
            print("Estes valores serão requisitados pelo programa pra realizar a criptografia, basta copiar e colar quando solicitados.")
            print("É recomendado que jamais compartilhe a sua chave privada e que guarde ela com segurança, visto que pode decifrar qualquer")
            print("mensagem encriptada pela sua respectiva chave pública")
            print("")
            print("Para criptografar uma mensagem basta selecionar a opção -3- no menu e escrever a mensagem que será criptografada,")
            print("após isso, o programa ira solicitar os valores da chave pública, o primeiro valor -e- e o segundo valor -n-, automaticamente")
            print("após a entrada dos valores, sua mensagem encriptada ira aparecer, estando no formata de um número extenso")
            print("")
            print("Para descriptografar uma mensagem basta selecionar a opção -4- no menu e escrever a mensagem q será descriptografada,")
            print("após isso, o programa ira solicitar os valores da chave privada, o primeiro valor -d- e o segundo valor -n-, automaticamente")
            print("após a entrada dos valores, sua mensagem original ira aparecer, totalmente descriptografada")
            print("")

            continue

        else: 
            print("Opção inválida!")

            continue

