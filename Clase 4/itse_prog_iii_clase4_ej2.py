"""
Crea un función “ConvertirEspaciado”, que reciba como parámetro un 
texto y devuelve una cadena con un espacio adicional tras cada 
letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un 
programa principal donde se use dicha función
"""


def convertir_espaciado(texto):
    texto_espaciado = ""
    for letra in texto:
        if letra != " ":
            texto_espaciado += letra + " "
    return texto_espaciado


print(convertir_espaciado(input("Ingrese un texto: ")))
