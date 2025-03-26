import pytest
from io import StringIO
import sys
from src.matematicas import tablas_de_multiplicar  # Asegúrate de importar correctamente la función

# ==============================
# Prueba: Tablas de multiplicar
# ==============================
def test_tablas_de_multiplicar(capsys):
    """Verifica que la función imprime correctamente las tablas de multiplicar del 1 al 10."""
    tablas_de_multiplicar()  # Ejecuta la función
    
    captured = capsys.readouterr()  # Captura la salida impresa
    salida = captured.out.split("\n")  # Convierte la salida en una lista de líneas

    # Verifica que las líneas de la tabla de multiplicar sean correctas
    expected_lines = []
    for i in range(1, 11):
        expected_lines.append(f"Tabla del {i}:")
        for j in range(1, 11):
            expected_lines.append(f"{i} x {j} = {i * j}")
        expected_lines.append("-")

    # Comparamos línea por línea
    assert salida[:-1] == expected_lines, "La salida de la función no coincide con la esperada"
