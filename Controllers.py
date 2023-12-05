import csv

def crear_registro(archivo, nuevo_registro):
    with open(archivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nuevo_registro)

def leer_registros(archivo):
    with open(archivo, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def actualizar_registro(archivo, id_actualizar, nuevo_registro):
    with open(archivo, mode='r') as file:
        rows = list(csv.reader(file))
        for i, row in enumerate(rows):
            if row[0] == id_actualizar:
                rows[i] = nuevo_registro

    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def borrar_registro(archivo, id_borrar):
    with open(archivo, mode='r') as file:
        rows = list(csv.reader(file))
        new_rows = [row for row in rows if row[0] != id_borrar]

    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

# Ejemplo de uso:
archivo_csv = 'contraseñas.csv'

# Crear registro
nuevo_registro = ['1', 'Correo', 'usuario1', 'contraseña123']
crear_registro(archivo_csv, nuevo_registro)

# Leer registros
print("Registros actuales:")
leer_registros(archivo_csv)

# Actualizar registro
id_actualizar = '1'
nuevo_registro_actualizado = ['1', 'Correo', 'usuario_actualizado', 'nueva_contraseña']
actualizar_registro(archivo_csv, id_actualizar, nuevo_registro_actualizado)

# Leer registros después de la actualización
print("\nRegistros después de la actualización:")
leer_registros(archivo_csv)

# Borrar registro
id_borrar = '1'
borrar_registro(archivo_csv, id_borrar)

# Leer registros después de borrar
print("\nRegistros después de borrar:")
leer_registros(archivo_csv)
