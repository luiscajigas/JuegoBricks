def tablas_de_multiplicar():
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("-")

# Ejecutar función
tablas_de_multiplicar()