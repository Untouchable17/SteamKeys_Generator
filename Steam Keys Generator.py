import random
from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.geometry('350x200')
root['bg'] = '#202020'
root.iconbitmap('путь к иконке')
root.title('Steam Keys')


def script():
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    number = 1
    length = 5

    for x in range(number):
        key1 = ' '
        key2 = ' '
        key3 = ' '

        for y in range(length):
            key1 += random.choice(chars)
            key2 += random.choice(chars)
            key3 += random.choice(chars)

        game = ['Minecraft', 'The Last Of Us. Part 2', 'CyberPunk', 'HITMAN',
                'Dying Light', 'Watch Dogs', 'DIRT 5', 'Fallout', 'Stalker 2',
                'Grand Theft Auto V', 'Just Cause 4', 'Spelunky 2', 'Sims 4',
                'Assassin\'s Creed Valhalla', 'Biomutant', 'Maneater', 'Wizard']

        GameGen = random.choice(game)
        KeysGen = str(key1) + ' -' + str(key2) + ' -' + str(key3) + ' | ➡ ' + GameGen
        result['text'] = KeysGen

        with open('SteamKeys.txt', 'a', encoding='utf-8') as file:
            file.write('\n' + str(KeysGen))


# Label instruction for Tkinter
text = Label(text='Steam Keys Generator v2.0',
             font='Roboto 13',
             bg='#202020',
             fg='#FF9C09',
             pady=20)
btn = Button(text='Сгенерировать Ключ',
             fg='white',
             bg='#414141',
             command=script)
result = Label(font='Roboto 10',
               bg='#202020',
               fg='#FF9C09',
               pady=20,
               text='')
text2 = Label(text='KℝYℙ₮Oℕ ₮EAM',
              font='Roboto 10',
              bg='#202020',
              fg='#11699A')
text3 = Label(text='✘ SecDet Samurai ✘',
              font='Roboto 10',
              bg='#202020',
              fg='#E76161')


def main():
    text.pack()
    btn.pack()
    result.pack()
    text2.pack()
    text3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
