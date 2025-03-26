from traductor import Translator

def traducir_ingles_espanol(texto):
    traductor = Translator()
    traduccion = traductor.translate(texto, src='en', dest='es')
    return traduccion.text

# Ejemplo de uso
texto_ingles = "Hello, how are you?"
texto_traducido = traducir_ingles_espanol(texto_ingles)
print(f"Traducción: {texto_traducido}")
