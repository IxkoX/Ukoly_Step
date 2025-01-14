alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

alphabet_reverse = {value: key for key, value in alphabet.items()}


class Morse:
    def encode(self, text):
        """ implementuj tuto metodu, encode znamená zakódovat """
       # return '   '.join(' '.join(alphabet[char.upper()] for char in word if char.upper() in alphabet) for word in text.split(' '))
        
        words = text.split(' ')  # Rozdělení textu na jednotlivá slova
        encoded_words = []  # Pole pro zakódovaná slova
        
        for word in words:
            encoded_chars = []  # Pole pro zakódované znaky v jednom slově
            for char in word:
                upper_char = char.upper()  # Převod na velká písmena
                if upper_char in alphabet:  # Kontrola, zda je znak v abecedě
                    encoded_chars.append(alphabet[upper_char])  # Přidání Morseova kódu pro znak
            encoded_words.append(' '.join(encoded_chars))  # Spojení znaků jednoho slova
            
        return '   '.join(encoded_words)
    
    
    def decode(self, morse):
        """ implementuj tuto metodu, decode znamená dekódovat """
        #return ' '.join(''.join(alphabet_reverse[code] for code in word.split() if code in alphabet_reverse) for word in morse.split('   '))
        
        # Rozdělení Morseova textu na slova
        slova = morse.split('   ')

        # Převod každého slova z Morseova kódu do běžného textu
        prevedena_slova = []
        for word in slova:
            znaky = [alphabet_reverse[code] for code in word.split() if code in alphabet_reverse]
            prevedena_slova.append(''.join(znaky))

        # Spojení slov zpět do textu
        vysledek = ' '.join(prevedena_slova)
        return vysledek



morse = Morse()
print(morse.encode('SOME TEXT HERE'))
# toto by mělo vrátit:
# ... --- -- .   - . -..- -   .... . .-. .

print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
# toto by mělo vrátit:
# SOME TEXT HERE

# zde je tajná zakodáváná zpráva pro vás
print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))
