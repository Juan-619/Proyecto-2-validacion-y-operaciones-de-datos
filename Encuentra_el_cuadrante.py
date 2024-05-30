def get_coordinates():

    # Solicita al usuario que ingrese las cordenadas X e Y.
    # Retorna las coordenadas como una tupla.
    while True:
        try:
            x = float(input("Enter X: "))
            y = float(input("Enter Y: "))
            if x == 0 or y == 0:
                print("Coordinates cannot be zero. Please enter non-zero values.")
            else:
                return x, y
        except ValueError:
            print("Invalid  input. Please enter numerical values.")

def identify_quadran(x, y):

    # Identifica en que cuadrante se encuentran las coordenadas (x, y).
    # Inprime el cuadrante correspondiente.

    if x > 0 and y > 0:
        print("The point is in Quadrant I.")
    elif x < 0 and y > 0:
        print("The pint is in Quadrant II.")
    elif x < 0 and y < 0:
        print("The point is in Quadrant III.")
    elif x > 0 and y < 0:
        print("The point is in Quadrant IV.")

def main():

    # Funcion principal que coordina la obtencion de las coordenadas
    # y la identificacion del cuadrante.

    x, y = get_coordinates()
    identify_quadran(x, y)


 # Entrada del programa
if __name__ == "__main__":
    main()