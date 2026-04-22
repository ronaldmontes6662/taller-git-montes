# SECCIÓN: Entradas
print("Bienvenido al Sistema ATM de Ronald Montes")
moneda = int(input("Ingrese Tipo de Moneda (1 para Bs, 2 para $): "))

print("Monto a Solicitar")
monto = int(input("Ingrese el monto (numero entero): "))

print("Tipo de Cuenta")
cuenta = int(input("Ingrese Tipo de cuenta (1 para ahorro, 2 para corriente): "))

# SECCIÓN: Validaciones
# Validar si es múltiplo de 10
if monto % 10 != 0:
    print("Error: Monto no compatible con denominaciones disponibles") 
    exit() # Esto detiene el programa al instante

# Validar límites de seguridad
if moneda == 2 and monto > 500:
    print("Transacción denegada: Excede limite diario")
    exit()
elif moneda == 1 and monto > 10000:
    print("Transacción denegada: Excede limite diario")
    exit()

# SECCIÓN: Cálculos de Desglose
comision = 0
if cuenta == 2:
    comision = monto * 0.05 # 

total_debitar = monto + comision 

billetes_100 = monto // 100 
resto = monto % 100 

billetes_50 = resto // 50
resto = resto % 50

billetes_20 = resto // 20
resto = resto % 20

billetes_10 = resto // 10
resto = resto % 10

# SECCIÓN: Salida
match moneda:
    case 1:
        tipo_moneda = "Bs."
    case 2:
        tipo_moneda = "$"
        
print(f"\n--- Resumen de Retiro ---")
print(f"Billetes de 100: {billetes_100}")
print(f"Billetes de 50: {billetes_50}")
print(f"Billetes de 20: {billetes_20}")
print(f"Billetes de 10: {billetes_10}")

print(f"\nTotal debitado: {total_debitar} {tipo_moneda}")