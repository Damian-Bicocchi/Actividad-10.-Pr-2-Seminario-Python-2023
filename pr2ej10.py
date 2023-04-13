def punto_a_relacionar(nombre,n1,n2):
    """
        * Retorna un diccionario con el nombre como clave y el valor es una tupla 
          con las notas correspondientes.

        * Requiere tres argumentos posicionales iterables, de los cuales el primero 
          sera la clave del diccionario, asi que es necesario que sea el iterable con 
          los nombres.
        * Los otros dos seran los valores de cada clave, que estaran almacenados dentro
          del diccionario en una tupla.
    """

    diccionario_intermedio = dict(zip(nombre,zip(n1,n2)))
    
    return diccionario_intermedio
    
def punto_b_promedio(un_diccionario):
    """
        * Retorna un diccionario con el nombre como clave y como valor el promedio
          de la colección de enteros (Si el value de una key es vacío almacena 0).

        * Requiere un diccionario en formato {key: coleccion de enteros}.
    """

    calc_prom = lambda notas : sum(notas) / len(notas) if len(notas) != 0 else 0

    todos_los_prom = map(calc_prom, un_diccionario.values())

    diccionario_intermedio = dict(zip(un_diccionario.keys(),todos_los_prom))  
    
    return diccionario_intermedio

def punto_c_promedio_general(un_diccionario):
    """
        *Retorna el promedio de las colecciones de enteros definidas como values
         en un diccionaro. Si esta vacío retorna 0.

        *Requiere un diccionario de formato key : coleccion enteros  
    """
    calc_prom = lambda notas: sum(notas) / len(notas) if len(notas) != 0 else 0

    notas = map(calc_prom, un_diccionario.values())

    prom = sum(notas) / len(un_diccionario) if len(un_diccionario) != 0 else 0
    
    return prom
    
def punto_d_promedio_mas_alto(un_diccionario):
    """
        *Retorna la key del diccionario cuyo colección de enteros tiene el promedio más 
        alto
        
        *Requiere un diccionario de formato key : coleccion de enteros
    """

    diccionario_intermedio = punto_b_promedio(un_diccionario)

    mas_alto = max(diccionario_intermedio, key = lambda n: diccionario_intermedio[n])

    return mas_alto

def punto_e_nota_baja(un_diccionario):
    """
        *Retorna la clave del parametro diccionario cuya colección de enteros contiene
         el valor más bajo.

        *Requiere como argumento un diccionario de la forma
         {clave : entero} ó {clave : coleccion de enteros}.
    """

    dic_bajo = dict({key : min(coleccion) for key,coleccion in un_diccionario.items()})

    bajo = min(dic_bajo, key = lambda n: dic_bajo[n])

    return bajo

nombres = '''
'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 
'Facundo', 'Francisca', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 
'Jonathan', 'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 
'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 
'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' 
'''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42,16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87,91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#Limpieza de string
nombres_limpios = nombres.replace(",","")
nombres_limpios = nombres_limpios.replace("'", "")

#Generar lista y formatear cada nombre
nombres_limpios = nombres_limpios.split()
nombres_limpios = list(map(lambda x: x.capitalize() ,nombres_limpios))


#Punto A
estructura_A_todos = punto_a_relacionar(nombres_limpios,notas_1,notas_2)

#Punto B
diccionario_promedio = punto_b_promedio(estructura_A_todos)

#Punto C
promedio_general = punto_c_promedio_general(estructura_A_todos)
print(f"Promedio general del curso = {promedio_general:.2f}")

#Punto D
alumno_mas_alto = punto_d_promedio_mas_alto(estructura_A_todos)
print(f"Estudiante con promedio mas alto : {alumno_mas_alto}")

#Punto E
alumno_mas_bajo = punto_e_nota_baja(estructura_A_todos)
print(f"Estudiante con la nota mas baja : {alumno_mas_bajo}")