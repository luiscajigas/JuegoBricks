import pytest
from unittest.mock import patch
from googletrans.models import Translated
from traductor import Translator
from traductor import traducir_ingles_espanol  # Asegúrate de importar correctamente tu función

# ==============================
# Prueba: Traducción inglés-español
# ==============================
@patch.object(Translator, 'translate')
def test_traducir_ingles_espanol(mock_translate):
    """Verifica que la función traduzca correctamente utilizando un mock."""
    
    # Simulamos la respuesta de la API
    mock_translate.return_value = Translated(src='en', dest='es', origin="Hello", text="Hola")

    texto = "Hello"
    resultado = traducir_ingles_espanol(texto)

    assert resultado == "Hola", f"Se esperaba 'Hola', pero se obtuvo {resultado}"
    mock_translate.assert_called_once_with(texto, src='en', dest='es')
