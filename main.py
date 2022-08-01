from src import req_mario

def main():
    saludo = req_mario.Bienvenida('Proyecto Base')
    print(saludo.mostrar_mensaje())

main()