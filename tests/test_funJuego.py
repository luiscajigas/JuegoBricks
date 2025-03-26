import pytest
from io import StringIO
import sys

# Código a probar
def iniciar_juego():
    print("¡Iniciando juego!!!")

def mover_personaje(direccion):
    print(f"Moviendo personaje hacia {direccion}")

def finalizar_juego():
    print("¡Fin del juego!!")

# ==============================
# Prueba 1: Iniciar juego
# ==============================
def test_iniciar_juego(capsys):
    """Verifica que iniciar_juego imprime el mensaje correcto."""
    iniciar_juego()
    captured = capsys.readouterr()
    assert "¡Iniciando juego!!!" in captured.out

# ==============================
# Prueba 2: Mover personaje
# ==============================
@pytest.mark.parametrize("direccion", ["izquierda", "derecha", "arriba", "abajo"])
def test_mover_personaje(capsys, direccion):
    """Verifica que mover_personaje imprime el mensaje correcto."""
    mover_personaje(direccion)
    captured = capsys.readouterr()
    assert f"Moviendo personaje hacia {direccion}" in captured.out

# ==============================
# Prueba 3: Finalizar juego
# ==============================
def test_finalizar_juego(capsys):
    """Verifica que finalizar_juego imprime el mensaje correcto."""
    finalizar_juego()
    captured = capsys.readouterr()
    assert "¡Fin del juego!!" in captured.out
