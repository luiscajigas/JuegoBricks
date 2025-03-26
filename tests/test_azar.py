import pytest
import random
from src.azar import adivina_el_numero  # Asegúrate de importar correctamente tu función

# ==============================
# Prueba 1: Adivinar el número correctamente
# ==============================
def test_adivina_el_numero_acierto(monkeypatch, capsys):
    """Simula que el número secreto es 75 y se adivina correctamente."""
    
    def mock_randint(a, b):
        return 75  # Fijamos el número secreto en 75

    monkeypatch.setattr(random, "randint", mock_randint)

    simulacion = [10, 50, 75]  # Intentos simulados, el tercero es correcto
    adivina_el_numero(simulacion)

    captured = capsys.readouterr()  # Captura la salida impresa

    assert "Intento 3: 75" in captured.out
    assert "¡Felicidades! Adivinaste el número en 3 intentos." in captured.out

# ==============================
# Prueba 2: No adivinar el número
# ==============================
def test_adivina_el_numero_fallo(monkeypatch, capsys):
    """Simula que el número secreto es 42, pero no se adivina."""
    
    def mock_randint(a, b):
        return 42  # Fijamos el número secreto en 42

    monkeypatch.setattr(random, "randint", mock_randint)

    simulacion = [10, 20, 30, 50, 60]  # Ninguno es correcto
    adivina_el_numero(simulacion)

    captured = capsys.readouterr()

    assert "El número secreto era 42." in captured.out

# ==============================
# Prueba 3: Número muy alto o bajo
# ==============================
def test_adivina_el_numero_alto_bajo(monkeypatch, capsys):
    """Simula que se hacen intentos bajos y altos antes de acertar."""
    
    def mock_randint(a, b):
        return 55  # Número secreto 55

    monkeypatch.setattr(random, "randint", mock_randint)

    simulacion = [10, 90, 50, 55]  # Se pasa de bajo a alto y luego acierta
    adivina_el_numero(simulacion)

    captured = capsys.readouterr()

    assert "Muy bajo, intenta de nuevo." in captured.out
    assert "Muy alto, intenta de nuevo." in captured.out
    assert "¡Felicidades! Adivinaste el número en 4 intentos." in captured.out
