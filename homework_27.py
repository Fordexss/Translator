from googletrans import Translator

translator = Translator()
with open('My_favorite_game.txt', 'r', encoding="UTF-8") as file:

    if file.mode == 'r':
        contents = file.read()
        print(contents)

    result = translator.translate(contents, dest='en')
    print(result.text)

    with open('My_favorite_game_en.txt', 'w') as f:
        f.write(result.text)
