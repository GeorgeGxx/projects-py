# clasificador spam ingenuo bayes

def lista_palabras(texto):
    palabras = []
    palabras_tmp= texto.lower().split()
    for p in palabras_tmp:
        if p not in palabras and len(p)> 2:
            palabras.append(p)
    return palabras

def entrenar(textos):
    c_palabras={}
    c_categorias={}
    c_textos = 0
    c_tot_palabras = 0
    
    # añadir al diccionario las categorías

    for t in textos:
        c_textos= c_textos + 1
        if t[1] not in c_categorias:
            c_categorias[t[1]] = 1
        else:    
            c_categorias[t[1]] = c_categorias[t[1]] + 1
            
     # añadir palabras en el diccionario
          
    for t in textos:
         palabras= lista_palabras(t[0])
              
    for  p in palabras:
         if p not in c_palabras:
             c_tot_palabras = c_tot_palabras + 1
             c_palabras[p] = {}
             for c in c_categorias:
                 c_palabras[p][c] = 0
         c_palabras[p][t[1]]=c_palabras[p][t[1]] + 1
         
    return  (c_palabras, c_categorias, c_textos, c_tot_palabras)

def clasificar(texto, c_palabras, c_categorias, c_textos, c_tot_palabras):
    categoria =""
    prob_categoria = 0
    for c in c_categorias:
        # probabilidad en la categoria
        prob_c= float(c_categorias[c])/float(c_textos)
        palabras=lista_palabras(texto)
        prob_total_c = prob_c
        for p in palabras:
            # Probabilidad de la palabra
            if p in c_palabras:
                prob_p=float(c_palabras[p][c])/float(c_tot_palabras)
                # Probabilidad P(categoria/palabra)
                prob_cond = prob_p/prob_c
                # Probabilidad P(palabra/categoria)
                prob = (prob_cond * prob_p)/prob_c
                prob_total_c = prob_total_c * prob
            if prob_categoria < prob_total_c:
                categoria = c
                prob_categoria =prob_total_c
    return(categoria,prob_categoria)


if __name__=="__main__":
    textos = [
        ["Siga derecho y de vuelta en la siguiente calle", "español"],
        ["Siga", "español"],
        ["derecho", "español"],
        ["vuelta", "español"],
        ["siguiente", "español"],
        ["calle", "español"],
        ["La Inteligencia Artificial es una disciplina muy interesante", "español"],
        ["Allez tout droit et prenez la prochaine rue", "frances"],
        ["Intelligence Artificialle est une discipline tres interessante", "frances"]]
        
p,c,t,tp = entrenar(textos)

#clase = clasificar("Siga derecho y aprenda Inteligencia Artificial",p,c,t,tp)
#clase = clasificar("Intelligence Artificialle est une discipline",p,c,t,tp)
clase = clasificar("Intelligence Artificialle est une inteligencia",p,c,t,tp)
#clase = clasificar("Siga derecho y rue droit Inteligencia Artificial",p,c,t,tp)
print (str(clase)) 
