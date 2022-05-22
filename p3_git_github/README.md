# Práctica 3. Git y GitHub

## Instrucciones 

#### 1. Colócate dentro de tu carpeta practicas_genomica_computacional e inicializala como un repositorio local de git.

**Comando**
```
git init
```

**Salida**
```
ayuda: Usando 'master' como el nombre de la rama inicial. Este nombre de rama predeterminado
ayuda: está sujeto a cambios. Para configurar el nombre de la rama inicial para usar en todos
ayuda: de sus nuevos repositorios, reprimiendo esta advertencia, llama a:
ayuda:
ayuda:  git config --global init.defaultBranch <nombre>
ayuda:
ayuda: Los nombres comúnmente elegidos en lugar de 'master' son 'main', 'trunk' y
ayuda: 'development'. Se puede cambiar el nombre de la rama recién creada mediante este comando:
ayuda:
ayuda:  git branch -m <nombre>
Inicializado repositorio Git vacío en /home/dulma/Documentos/Facultad/Genomica_Computacional/practicas_genomica_computacional/.git/
```

#### 2. Agrega al área de espera todo el contendio de ésta carpeta.

**Comando**
```
git add ./*
```

**Salida**
```
~/Doc/F/Genomica_Computacional/practicas_genomica_computacional master +13 > 
```
(Se agregaron 13 archivos)


#### 3. Haz un primera confirmación de todo el contenido con el mensaje “Prácticas de Genomica Computacional”.

**Comando**
```
git commit -m "Prácticas de Genomica Computacional"
```

**Salida**
```
[master (commit-raíz) 224d095] Prácticas de Genomica Computacional
 13 files changed, 238240 insertions(+)
 create mode 100644 minipracticas/mp1_MonteroRasgado_DulceMaria.ipynb
 create mode 100644 minipracticas/mp2_MonteroRasgado_DulceMaria.ipynb
 create mode 100644 "p1_dogma_central/p1_IbarraGisselle_MonteroMar\303\255a.py"
 create mode 100644 p2_ngs_bash/data/filtered/barplot_data.txt
 create mode 100644 p2_ngs_bash/data/filtered/cp_Bacillus_cereus.gff3
 create mode 100644 p2_ngs_bash/data/raw_data/Bacillus_cereus.fasta
 create mode 100644 p2_ngs_bash/data/raw_data/Bacillus_cereus.fastq
 create mode 100644 p2_ngs_bash/data/raw_data/Bacillus_cereus.gb
 create mode 100644 p2_ngs_bash/data/raw_data/Bacillus_cereus.gff3
 create mode 100644 p2_ngs_bash/figures/barplot.png
 create mode 100644 p2_ngs_bash/scripts/.ipynb_checkpoints/Parte III-checkpoint.ipynb
 create mode 100644 p2_ngs_bash/scripts/Parte III.ipynb
 create mode 100644 p2_ngs_bash/scripts/p2_Montero_Dulce.ipynb
```


#### 4. Crea un archivo .md en tu carpeta p1_dogma_central que describa qué hace tu programa. Si hay funciones dentro, qué hace cada función.

**Comando**
```
touch README.md
```

**Comando**
```
nano README.md  # escribimos la descripción del programa
```
```
cat README.md
```

**Salida**
```
El programa pide  al usuario una cadena de DNA y el usuario ingresa la cadena en minúsculas o mayúsculas, y el programa arroja:

- La validación de la cadena, si la cadena no es válida lo indica  en un mensaje y termina el programa.

- Arroja la cadena complementaria.

- Arroja la cadena transcrita (mRNA).

- Verifica que la cadena tenga un codón de inicio, sino es así, que arroja un mensaje.

- Si la cadena tiene un codón de inicio, arroja la cadena de aminoácidos (cadena traducida).


En nuestro programa hay un total de cinco funciones:

- Validación. Esta función valida la secuencia de DNA que proporcione el usuario.
- Complementaria. Esta función obtiene la secuencia complementaria de DNA en caso de ser válida la secuencia.
- Transcripcion. Esta función devuelve la secuencia de RNA después de la transcripción.
- codon_inicio. Esta función indica si la secuencia de RNA tiene un codón de inicio.
- aminoacidos. Esta función obtiene la secuencia de aminoácidos en caso de encontrar un codón de inicio.
```


#### 5. Agrega la modificación de la instrucción anterior a tu área de éspera y luego haz la confirmación que lleve el siguiente mensaje “Descripcion de programa.”

**Comando**
```
git add README.md
```

**Salida**
```
~/Doc/F/Genomica_Computacional/practicas_genomica_computacional/p1_dogma_central master +1 >  
```

**Comando**
```
git commit -m "Descripcion deprograma."
```

**Salida**
```
[master ac91d09] Descripcion de programa.
 1 file changed, 20 insertions(+)
 create mode 100644 p1_dogma_central/README.md
```


#### 6. Checa el historial de confirmaciones que has hecho.

**Comando**
```
git log
```

**Salida**
```
commit ac91d09a6a779e7367c994dee389dbc167e9a1ec (HEAD -> master)
Author: Dulma <anathema.26@ciencias.unam.mx>
Date:   Sat May 21 19:09:19 2022 -0500

    Descripcion de programa.

commit 224d0953ea9e457623910fe01ccfb26cf14d6c05
Author: Dulma <anathema.26@ciencias.unam.mx>
Date:   Sat May 21 18:29:54 2022 -0500

    Prácticas de Genomica Computacional
```


#### 7. Checa en qué rama te encuentras.

**Comando**
```
git branch
```

**Salida**
```
* master
```


#### 8. Conecta éste repositorio local a tu repositorio remoto.
**Comando**
```
git remote add origin https://github.com/Dulma-mora/GC---Practicas---Dulce-Montero.git
git branch -M main
git push -u origin main
```

**Salida**
```
error: remoto origin ya existe.
Username for 'https://github.com': Dulma-mora
Password for 'https://Dulma-mora@github.com':
Enumerando objetos: 27, listo.
Contando objetos: 100% (27/27), listo.
Compresión delta usando hasta 8 hilos
Comprimiendo objetos: 100% (26/26), listo.
Escribiendo objetos: 100% (27/27), 3.72 MiB | 543.00 KiB/s, listo.
Total 27 (delta 1), reusados 0 (delta 0), pack-reusados 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/Dulma-mora/GC---Practicas---Dulce-Montero.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```


#### 9. Crea un archivo README.md en tu repositorio remoto que contenga:
- A modo de encabezado: “Prácticas - Genómica computacional - 2022”
- Luego una línea en blanco.
- En la tercera línea tu nombre completo en negritas.
- OPCIONAL: Una descripción del contenido de éste repositorio.

**Comando**
```
touch README.md
```

**Comando**
```
nano README.md # escribir el contenido
```
**Comando**
```
cat README.md
```

**Salida**
```
# Prácticas - Genómica computacional - 2022

**Dulce María Montero Rasgado**

En este repositorio se encuentran todas las prácticas realizadas en el curso Genómica Computacional durante el semestre 2022-2

Ponme 10 Naye :)
```


#### 10. Agrega las modificaciones de tu repositorio remoto a tu repositorio local.

**Comando**
```
git add README.md
git commit -m "agregar README general"
gith push
```

**Salida**
```
Username for 'https://github.com': Dulma-mora
Password for 'https://Dulma-mora@github.com':
Enumerando objetos: 4, listo.
Contando objetos: 100% (4/4), listo.
Compresión delta usando hasta 8 hilos
Comprimiendo objetos: 100% (3/3), listo.
Escribiendo objetos: 100% (3/3), 449 bytes | 449.00 KiB/s, listo.
Total 3 (delta 1), reusados 0 (delta 0), pack-reusados 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Dulma-mora/GC---Practicas---Dulce-Montero.git
   ac91d09..339bf50  main -> main
```
