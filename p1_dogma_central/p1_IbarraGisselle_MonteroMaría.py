#Equipo:
#Ibarra Moreno Gisselle
#Montero Rasgado Dulce María

def validacion(secuencia):
    invalid = ["B","D","E","F", "H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","U","V","W","X","Y","Z"]
    for i in secuencia:
        if i in invalid:
            print("La secuencia de DNA no es válida.")
            return False

    return True


def complementaria(secuencia):
    complementaria = ""
    for a in secuencia:
        if a == "A":
            complementaria += "T"
        elif a == "T":
            complementaria += "A"
        elif a == "C":
            complementaria += "G"
        elif a == "G":
            complementaria += "C"
    return complementaria


def transcripcion(secuencia):
    """
    Recibe una secuencia y regresa la transcripción a mRNA
    """
    mrna=''
    for b in secuencia:
        if b == 'T':
            mrna+='A'
        elif b == 'A':
            mrna+='U'
        elif b == 'G':
            mrna+='C'
        elif b == 'C':
            mrna+='G'
    return mrna

def codon_inicio(secuencia):
    """
    Indica si una secuencia tiene un codón de inicio
    """
    return secuencia[0:3] == 'ATG'


def aminoacidos(secuencia):
    sec_aminoacidos=''
    for i in range(3,len(secuencia),3):
        codon=secuencia[i:i+3]
        sec_aminoacidos+=aa[codon]+" "
    return sec_aminoacidos


def main(secuencia):
    #valida la secuencia
    if validacion(secuencia):
        #Regresa la cadena complementaria
        print("La secuencia complementaria es: ", complementaria(secuencia))
        #Regresa la transcripción
        t=transcripcion(secuencia)
        print("La transcripción es:",t)
        #Indica si tiene un codón de inicio
        if codon_inicio(secuencia):
            #Regresar cadena de aminoácidos
            a=aminoacidos(t)
            print("Cadena de aminoacidos:",a)
            return a
        else:
            print('No tiene codón de inicio')



if __name__ =='__main__':
    aa = {"UUU": "Fenilananina", "UUC": "Fenilananina", # 2
          "UUA": "Leucina", "UUG":"Leucina", "CUU":"Leucina", "CUC":"Leucina", "CUA":"Leucina", "CUG": "Leucina", # 6
          "AUU": "Isoleucina", "AUC": "Isoleucina", "AUA": "Isoleucina", # 3
          "AUG":"Metionina", # 1
          "GUU":"Valina", "GUC":"Valina", "GUA":"Valina", "GUG":"Valina", # 4
          "UCU": "Serina", "UCC": "Serina", "UCA": "Serina", "UCG": "Serina", # 4
          "CCU":"Prolina", "CCC":"Prolina", "CCA":"Prolina", "CCG":"Prolina", # 4
          "ACU":"Treonina", "ACC":"Treonina", "ACA":"Treonina", "ACG":"Treonina", # 4
          "GCU":"Alanina", "GCC":"Alanina", "GCA":"Alanina", "GCG":"Alanina",
          "UAU":"Tirosina", "UAC":"Tirosina", # 2
          "CAU":"Histidina", "CAC":"Histidina", # 2
          "CAA":"Glutamina", "CAG":"Glutamina",
          "AAU":"Asparagina", "AAC":"Asparagina",
          "AAA":"Lisina", "AAG":"Lisina",
          "GAU":"Acido Aspartatico", "GAC":"Acido Aspartatico",
          "GAA":"Acido Glutamico", "GAG":"Acido Glutamico",
          "UGU":"Cisteina", "UGC":"Cisteina",
          "UGG":"Triptofano",
          "CGU":"Arginina", "CGC":"Arginina", "CGA":"Arginina", "CGG":"Arginina",
          "AGU":"Serina", "AGC":"Serina",
          "AGA":"Arginina", "AGG":"Arginina",
          "GGU":"Glicina", "GGC":"Glicina", "GGA":"Glicina", "GGG":"Glicina",
          "UAA":"-", "UAG":"-", "UGA":"-"}

    secuencia = input("Ingrese una cadena de DNA:")
    secuencia = secuencia.upper()

    main(secuencia)
