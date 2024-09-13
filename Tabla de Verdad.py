def tabla():
    n = int(input("Numero de filas: "))

    # Inicializar un diccionario para almacenar los valores de los bits
    valores = {}

    # Solicitar al usuario que ingrese un valor para cada bit y asignarlo a la variable correspondiente
    for i in range(n):
        variable = f"w{i + 1}"
        valor = input(f"Ingrese el valor de ({variable}): ")
        valores[variable] = valor

    # Solicitar al usuario que ingrese el umbral
    umbral = float(input("Ingrese el umbral: "))

    # Calcular el número total de combinaciones posibles
    bits = 2 ** n

    # Crear la expresión de la suma de los bits con sus respectivas variables
    sumatoria = " + ".join([f"x{i + 1}({variable})" for i, variable in enumerate(valores.keys())])

    # Imprimir encabezados de la tabla
    encabezado = "| " + " \t| ".join(
        [f"x{i + 1}" for i, variable in enumerate(valores.keys())]) + " \t| Operación \t| S  \t|"  f"S > {umbral}"
    print(encabezado)

    # Imprimir la línea separadora
    separador = "+" + "-" * ((n * 12) + (n * 3) + 13) + "+"
    print(separador)

    # Generar y mostrar todas las combinaciones posibles
    for i in range(bits):
        # Convertir el número entero en su representación binaria de n bits
        binario = bin(i)[2:].zfill(n)

        # Multiplicar cada bit de la tabla con su respectiva variable y calcular el resultado
        productos = [str(int(binario[j]) * int(valores[f"w{j + 1}"])) for j in range(n)]
        resultado = sum(int(producto) for producto in productos)

        # Verificar si el resultado es mayor que el umbral
        if resultado > umbral:
            mensaje = "SI"
            numero = "1"
        else:
            mensaje = "NO"
            numero = "0"

        # Crear la operación de suma de los bits con sus respectivas variables
        operacion = " + ".join([f"{binario[j]}({valores[f'w{j + 1}']})" for j in range(n)])

        # Imprimir las combinaciones | operacion | resultado | Si o no mayor al umbral
        fila = "|   " + " \t|   ".join(binario) + f" \t| {operacion} \t|   {numero} \t| {mensaje} \t|"
        print(fila)

        # Imprimir la línea separadora después de cada fila
        print(separador)

    # Imprimir la expresión de la suma
    print(f"Sumatoria: {sumatoria}")

tabla()
