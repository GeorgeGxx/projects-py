# Red Hopfield
# Reconoce los caracteres 0,1 y 2

# Transformar representación gráfica en +1 y -1
def graf_a_valores(datos):
    datos = datos.replace(' ', '')  # quita espacios
    salida = []
    for i in range(len(datos)):
        if datos[i] == '.':
            salida.append(-1.0)
        else:
            salida.append(1.0)
    return salida

# Transformar valores -1 y +1 a la representación gráfica


def valores_a_graf(datos):
    salida = ''
    cont = 0
    for i in datos:
        cont = cont + 1
        if i == -1.0:
            salida = salida + '.'
        else:
            salida = salida + 'o'
        if cont % 5 == 0:
            salida = salida + '\n'  # Salto de linea
    return salida

# Calcula diferencial de energía


def denergia(linea):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    temp = 0.0
    for i in range(n_entradas):
        temp = temp + (pesos[linea][i]) * (nodos_entrada[i])
    return 2.0*temp - sum_lin_pesos[linea]

# Devuelve el valor -1 0 1


def discretizar(n):
    if n < 0.0:
        return -1.0
    else:
        return 1.0

# Entrenamiento de la red


def entrenar(datos_ent):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    # Actualizamos pesos
    for i in range(1, n_entradas):
        for j in range(i):
            for k in range(len(datos_ent)):
                datos = datos_ent[k]
                t = discretizar(datos[i]) * discretizar(datos[j])
                temp = float(int(t+pesos[i][j]))   # Truncar decimales
                pesos[i][j] = temp
                pesos[j][i] = temp                 # Es una matriz simétrica

# Actualizamos suma de las líneas de la matriz de pesos
    for i in range(n_entradas):
        sum_lin_pesos[i] = 0.0
        for j in range(i):
            sum_lin_pesos[i] = sum_lin_pesos[i] + pesos[i][j]

# Clasificar patrón de entrada


def clasificar(patron, iteraciones):
    global n_entradas, pesos, nodos_entrada, sum_lin_pesos
    nodos_entrada = patron[:]
    for i in range(iteraciones):
        for j in range(n_entradas):
          if denergia(j) > 0.0:
              nodos_entrada[i] = 1.0
          else:
              nodos_entrada[j] = -1.0
    return nodos_entrada


if __name__ == "__main__":
    datos_ent = [
        graf_a_valores('ooooo\
                     o...o\
                     o...o\
                     ooooo'),

        graf_a_valores('.oo..\
                     ..o..\
                     ..o..\
                     ..o..'),


        graf_a_valores('ooooo\
                     ...o.\
                     .o...\
                     ooooo')]

n_entradas = 20  # Números de nodos en la red
nodos_entrada = [0.0]*n_entradas
sum_lin_pesos = [0.0]*n_entradas
# Crear  matriz de pesos
pesos = []
for id in range(n_entradas):
    pesos.append([0.0]*n_entradas)
entrenar(datos_ent)
# Intentar reconocer el caracter distorsionado


caracter = graf_a_valores('ooooo\
                           o..oo\
                           oo...\
                           ooooo')
caracter = graf_a_valores('ooooo\
                           o...o\
                           oOo.o\
                           o...o\
                           ooooo')


reconocido = clasificar(caracter, 5)
print('Caracter introducido')
print(valores_a_graf(caracter))
print('Caracter reconocido')
print(valores_a_graf(reconocido))
