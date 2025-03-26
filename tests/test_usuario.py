import pytest
import random
import string
from src.usuario import generar_usuario, generar_contraseña, crear_cuenta  # Asegúrate de importar correctamente

# ==============================
# Prueba 1: Generar Usuario
# ==============================
def test_generar_usuario(monkeypatch):
    """Verifica que generar_usuario genera un usuario con el formato correcto."""
    
    def mock_randint(a, b):
        return 123  # Simulamos que siempre se genera el número 123

    monkeypatch.setattr(random, "randint", mock_randint)

    usuario = generar_usuario("Juan", "López")
    
    assert usuario == "juanlopez123", f"Se esperaba 'juanlopez123', pero se obtuvo '{usuario}'"

# ==============================
# Prueba 2: Generar Contraseña
# ==============================
def test_generar_contraseña():
    """Verifica que la contraseña generada tenga la longitud esperada y contenga caracteres válidos."""
    
    contraseña = generar_contraseña(12)

    assert len(contraseña) == 12, f"La contraseña debe tener 12 caracteres, pero tiene {len(contraseña)}"
    assert any(c.islower() for c in contraseña), "La contraseña debe tener al menos una letra minúscula"
    assert any(c.isupper() for c in contraseña), "La contraseña debe tener al menos una letra mayúscula"
    assert any(c.isdigit() for c in contraseña), "La contraseña debe tener al menos un número"
    assert any(c in string.punctuation for c in contraseña), "La contraseña debe tener al menos un símbolo"

# ==============================
# Prueba 3: Crear Cuenta
# ==============================
def test_crear_cuenta(monkeypatch):
    """Verifica que crear_cuenta devuelve un usuario y una contraseña válidos."""
    
    def mock_randint(a, b):
        return 456  # Simulamos que siempre se genera el número 456

    monkeypatch.setattr(random, "randint", mock_randint)

    usuario, contraseña = crear_cuenta("Ana", "Gómez")

    assert usuario == "anagómez456", f"Se esperaba 'anagómez456', pero se obtuvo '{usuario}'"
    assert isinstance(contraseña, str) and len(contraseña) > 8
