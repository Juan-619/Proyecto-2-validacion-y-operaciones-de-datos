def get_word():

    # Solicita al usuario que ingrese una palabra.

    word = input("Enter a word: ")
    return word

def check_word_length(word):

    # Verifica la longitud de la palabra y proporciona mensajes adecuados.

    length = len(word)

    if 4 <= length <= 8:
        print("The word is correct.")
    elif length < 4:
        print(f"Letters are missing. it only has {length} letters.")
    else:
        print(f"Too many letters. it has {length} letters.")

def main():

    # Funcion principal que cordina la obtencion y verificacion de la palabra.

    word = get_word()
    check_word_length(word)                


    # Entrada del programa
if __name__ == "__main__":
    main()