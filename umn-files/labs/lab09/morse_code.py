morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}

string = input("Enter a message: ")
string = string.upper()
morse_string = ""
for i in range(len(string)):
	current_char = string[i]
	morse_string = morse_string + morse_dictionary[current_char] + " "

print(morse_string)
