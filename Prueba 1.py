# Programa Interactivo en Python

# 1. El programa pide datos al usuario y los guarda en "variables"
nombre = input("¿Cómo te llamas? ")
print("¡Un gusto saludarte, " + nombre + "!")

# 2. Trabajando con números y lógica
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Ya eres mayor de edad legalmente.")
else:
    anios_faltantes = 18 - edad
    print("Eres menor de edad. Te faltan " + str(anios_faltantes) + " años para cumplir 18.")

# 3. Una pregunta técnica
interes = input("¿Qué carrera te llama más la atención? ")
print("¡Excelente elección! " + interes + " es una carrera con un futuro brillante.")
