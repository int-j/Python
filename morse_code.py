def to_morse_code(input_text):
    converted_msg = ""

    for current_char in input_text.upper():
        if current_char == " ":
            converted_msg += " "
        else:
            converted_letter = convert_to_morse_code(current_char)
            converted_msg += converted_letter
            converted_msg += " "

    return converted_msg.strip()

def convert_to_morse_code(current_char):
    chars_to_morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    return chars_to_morse.get(current_char, "")

input_text = "HELLO WORLD"
morse_code = to_morse_code(input_text)

print(morse_code)
