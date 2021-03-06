import argparse
import pila
import errores
def cargar_codigo(archivo):
    """ Pre: El archivo debe existir y se tiene que poder leer
        Post: Devuelve una lista con los comandos que reconoce
        un interprete de matacerebros
    """
    with open(archivo) as archivo_matacerebros:
        comandos_matacerebro = "<>+-[]."
        comandos_archivo = []
        pila_saltos = pila.Pila()
        pos_actual = 0
        for linea in archivo_matacerebros:
            for caracter in linea:
                if caracter in comandos_matacerebro:
                    if caracter == "[":
                        pila_saltos.apilar([caracter,pos_actual])
                        comandos_archivo.append([caracter,pos_actual])
                        pos_actual+=1
                        continue
                    elif caracter == "]":
                        try:
                            if pila_saltos.ver_tope()[0]  == "[":
                                posicion_anterior = pila_saltos.desapilar()[1]
                                comandos_archivo[posicion_anterior][1] = pos_actual
                                comandos_archivo.append([caracter,posicion_anterior])
                                pos_actual+=1
                                continue
                        except pila.PilaVaciaError:
                            raise errores.MCSyntaxError
                    comandos_archivo.append(caracter)
                    pos_actual+=1
    if pila_saltos.esta_vacia():
        return comandos_archivo
    else: raise errores.MCSyntaxError
#Este codigo devuelve la lista de cada comando pero en cada corchete "[" o "]" guarda la posicion del corchete asociado            
def main():
    parser = argparse.ArgumentParser(description='Interprete de codigo MataCerebros')
    parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
    parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
    args = parser.parse_args()

    nombre_archivo = args.archivo #Esto es un string, que vendria a tener 
    modo_debug = args.debug #si en la linea de comandos le pasas aparte del nombre, "-d", esto guarda True

    lista_comandos = cargar_codigo(nombre_archivo)
    
    
main()
