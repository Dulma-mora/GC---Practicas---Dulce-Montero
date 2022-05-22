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
