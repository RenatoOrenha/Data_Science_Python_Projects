# Escolha aleatória das frutas para a Salada

frutas = ["maçã", "banana", "uva", "pêra",
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

from random import choice

fruta_1 = choice(frutas)
fruta_2 = choice(frutas)
fruta_3 = choice(frutas)

if fruta_2 == fruta_1:
    fruta_2 = choice(frutas)

if fruta_3 == fruta_1 or fruta_3 == fruta_2:
    fruta_3 = choice(frutas)
else:
    print('A salada de frutas surpresa é composta por {}, {} e {}.'.format(fruta_1, fruta_2, fruta_3))