import MySQLdb
import random 

#Conexión a la base de datos
miConexion = MySQLdb.connect( host='localhost', user='root', password='', db ='score_app' )
cursor = miConexion.cursor()



username = input('Ingrese su nombre de usuario: ')

cursor.execute("SELECT * FROM score WHERE username =%s", (username,))
result = cursor.fetchone()

if result is None:
    cursor.execute("INSERT INTO score (username, score) VALUES (%s, %s)", (username,0))
    miConexion.commit()

puntuacion = 0

while True:
    n = random.randint(0,10)
    print(n)
    guess = int(input('Ingrese un número'))

    if guess == n:
        puntuacion += 1
        print(f'Felicidades acertaste el número, tu puntuación es de: {puntuacion} puntos')
        
    else:
        print(f'Fallaste, el número era {n} y elegiste {guess}, puntuación :{puntuacion} ')
        cursor.execute("UPDATE score SET score=%s WHERE username =%s", (puntuacion, username))
        miConexion.commit()
        break

cursor.execute("SELECT * FROM score ORDER BY score DESC")
resultados = cursor.fetchall()

print("Tabla de Clasificación:")
print("ID    |   USER      |   SCORE |")
print("-"* 30)

for fila in resultados:
    print(f'{fila[0]:<3}   |{fila[1]:<10}   |{fila[2]:<3}   |')
cursor.close()
miConexion.close()