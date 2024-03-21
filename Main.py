meme_dict - {
  "CRINGE": "Algo excepcionalmente raroembarazoso",
  "LOL": "Una respuesta común a algo gracioso",
  "WTF": "Estar abrumado",
  "NONONO": "Ligera desaprobación",
  "CREEPY": "Aterrador, siniestro",
  "ASH": "Ponerse agresivo/enojado"
}
print("¡Bienvenido al Diccionario Palabras De memes!")

for _ in range(5):
    word = input("Escribe la palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
      print(meme_dict[word])
    else:
      print("Lo siento, no se encontró tu palabra en el diccionario.")
      
print("iGracias por usar el Diccionario Buen dia")
