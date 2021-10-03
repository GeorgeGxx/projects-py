# Vuelos con busqueda en amplitud

from arbol_2 import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):

    solucionado = False
    nodos_visitados = [] 
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo=nodos_frontera[0]
        # Extraer todo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
          # solución encontrada   
          solucionado = True
          return nodo       #nodos_visitados  
        else:
          #Expandir nodos hijo   (ciudades con conexion)
          dato_nodo = nodo.get_datos()
          lista_hijos = []
          for un_hijo in conexiones[dato_nodo]:
             hijo = Nodo(un_hijo)
             lista_hijos.append(hijo)
             if not hijo.en_lista(nodos_visitados)\
             and not hijo.en_lista(nodos_frontera):
                 nodos_frontera.append(hijo)
          nodo.set_hijos(lista_hijos)    
         
    
if __name__=="__main__": 
    conexiones = {
    'Taxquena':{'GAnaya'},
    'GAnaya':{'Taxquena','Ermita'},
    'Ermita':{'GAnaya','Portales'},
    'Portales':{'Ermita','Nativitas'}, 
    'Nativitas':{'Portales','VCortes'},
    'VCortes':{'Nativitas','Xola'},
    'Xola':{'VCortes','Viaducto'},
    'Viaducto':{'Xola','Chabacano'},
    'Chabacano':{'Viaducto','SAbad'},
    'SAbad':{'Chabacano','PSuarez'},
    'PSuarez':{'SAbad','Zocalo'},
    'Zocalo':{'PSuarez','Allende'},
    'Allende':{'Zocalo','BArtes'},
    'BArtes':{'Allende','Hidalgo'},
    'Hidalgo':{'BArtes','Revolucion','Juarez','Guerrero'},
    'Revolucion':{'Hidalgo','SanCosme'},
    'SanCosme':{'Revolucion','Normal'},
    'Normal':{'SanCosme','CMilitar'},
    'CMilitar':{'Normal','Popotla'},
    'Popotla':{'CMilitar','Cuitlahuac'},
    'Cuitlahuac':{'Popotla','Tacuba'},
    'Tacuba':{'Cuitlahuac','Panteones','SanJoaquin','Refineria'},
    'Panteones':{'Tacuba','Toreo'},
    'Toreo':{'Panteones'},

    'BMuerto':{'Mixcoac'},
    'Mixcoac':{'BMuerto','SanAntonio'},
    'SanAntonio':{'Mixcoac','SPPinos'},
    'SPPinos':{'SanAntonio','Tacubaya'},
    'Tacubaya':{'SPPinos','Constituyentes'},
    'Constituyentes':{'Tacubaya','Auditorio'},
    'Auditorio':{'Constituyentes','Polanco'},
    'Polanco':{'Auditorio','SanJoaquin'},
    'SanJoaquin':{'Polanco','Tacuba'},
    'Tacuba':{'SanJoaquin','Refineria','Cuitlahuac','Panteones'},
    'Refineria':{'Tacuba','Camarones'},
    'Camarones':{'Refineria','ASerdan'},
    'ASerdan':{'Rosario','Camarones'},
    'Rosario':{'ASerdan'},

    'Universidad':{'Copilco'},
    'Copilco':{'Universidad','MAQuevedo'},
    'MAQuevedo':{'Copilco','Viveros'},
    'Viveros':{'MAQuevedo','Coyoacan'},
    'Coyoacan':{'Viveros','Zapata'},
    'Zapata':{'Coyoacan','DivNorte'},
    'DivNorte':{'Zapata','Eugenia'},
    'Eugenia':{'DivNorte','Etiopia'},
    'Etiopia':{'Eugenia','CMedico'},
    'CMedico':{'Etiopia','HospGral'},
    'HospGral':{'CMedico','NHeroes'},
    'NHeroes':{'HospGral','Balderas'},
    'Balderas':{'NHeroes','Juarez'},
    'Juarez':{'Balderas','Hidalgo'},
    'Hidalgo':{'Juarez','Guerrero','BArtes','Revolucion'},
    'Guerrero':{'Hidalgo','Tlatelolco'},
    'Tlatelolco':{'Guerrero','LaRaza'},
    'LaRaza':{'Tlatelolco','Potrero'},
    'Potrero':{'LaRaza','18Marzo'},
    '18Marzo':{'IndVerdes','Potrero'},
    'IndVerdes':{'18Marzo'},

    'Tacubaya':{'Constituyentes','SPPinos','Patriotismo'},
    'Patriotismo':{'Tacubaya','Chilpancingo'},
    'Chilpancingo':{'Patriotismo','CMedico'},
    'CMedico':{'Chilpancingo','Etiopia','HospGral','LCardenas'},
    'LCardenas':{'CMedico','Chabacano'},
    'Chabacano':{'LCardenas','Viaducto','SAbad','Jamaica'},
    'Jamaica':{'Chabacano','Mixiuhca'},
    'Mixiuhca':{'Jamaica','Velodromo'},
    'Velodromo':{'Mixiuhca','CDeportiva'},
    'CDeportiva':{'Velodromo','Puebla'},
    'Puebla':{'CDeportiva','Pantitlan'},
    'Pantitlan':{'Puebla'},

    'LPaz':{'LReyes'},
    'LReyes':{'LPaz','SMartha'},
    'SMartha':{'LReyes','Acatitla'},
    'Acatitla':{'SMartha','PViejo'},
    'PViejo':{'Acatitla','Guelatao'},
    'Guelatao':{'PViejo','Tepalcates'},
    'Tepalcates':{'Guelatao','CSJuan'},
    'CSJuan':{'Tepalcates','AOriental'},
    'AOriental':{'CSJuan','Pantitlan'},
    'Pantitlan':{'AOriental','Puebla'},

    'ERosario':{'Tezozomoc'},
    'Tezozomoc':{'ERosario','Azcapotzalco'},
    'Azcapotzalco':{'Tezozomoc','Ferreria'},
    'Ferreria':{'Azcapotzalco','Norte45'},
    'Norte45':{'Ferreria','Vallejo'},
    'Vallejo':{'Norte45','IPetroleo'},
    'IPetroleo':{'Vallejo','LVista'},
    'LVista':{'IPetroleo','18Marzo'},
    '18Marzo':{'LVista','Potrero','IndVerdes','LVBasilica'},
    'LVBasilica':{'18Marzo','MCarrera'},
    'MCarrera':{'LVBasilica'},

    }
    
    estado_inicial = 'Guelatao'
    solucion = 'Ferreria'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado =[]
    nodo = nodo_solucion
    while nodo.get_padre() != None:
      resultado.append(nodo.get_datos())
      nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)
