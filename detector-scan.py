import socket
import os

os.system("clear")

cor1 = "\033[35m"
cor2 = "\033[32m"
norm = "\033[m"

print(f"""{cor1}

           _______
          /   {cor2}|{cor1}   \\
        /|  {cor2}--0--{cor1}  |
       |  \\___{cor2}|{cor1}___/
       \  _/
        |/

{norm}DETECTOR DE SCAN

>>> TODOS OS LOGS DE SCAN FICARAM SALVOS EM UM ARQUIVO TXT
CHAMADO [ istorico.txt ]

>>> PARE O SCAN SELECIONANDO [ CTRL, c ]

""")

host = str(input("SEU IP DA REDE LOCAL: "))
porta = 8080

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    servidor.bind((host, porta))
except:
    porta = 443
    servidor.bind((host, porta))
servidor.listen(40)

print(f"[{cor1}+{norm}]_[{cor2}SERVIDOR{norm}]_[{cor2}HOST:{host}{norm}]_[{cor2}PORTA:{porta}{norm}]")
print("\nESPERANDO CONEXÕES...")

while True:
    conn, addr = servidor.accept()
    print("SCAN DETECTADO:", addr)
    conn.close()
    with open("istorico.txt", "a") as arquivo:
        arquivo.write(f"{addr} | {conn}\n")
