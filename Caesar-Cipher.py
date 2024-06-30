chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuzwxyz']

# Encode
def encode(message, offset=14):
# Message is the first variable being the string to encode and the second variable being offset.
# Traditionally a caesar cipher will incorporate a ROT13 but in this case im rotating the numbers by 14.I chose this as a student of history as a nod to the the Vigenère cipher not cracked untill 1863.
    enc_chars = str.maketrans(
        f'{chars[0]}{chars[1]}',
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}'
    )
# This concatenates both alphbet strings where they shift
    return str.translate(message, enc_chars)

# Decode
def decode(message,offset=14):
    dec_char = str.maketrans(
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}',
        f'{chars[0]}{chars[1]}'
    )
    return str.translate(message,dec_char)

get_option = input("Choose [E]ncode or [D]ecode (Default: E): ")
if get_option == 'e':
    message = input('Enter your transmission: ')
    offset =int(input('Choose the shift (1-26): '))
    if offset < 1 or offset > 26:
        raise Exception(f'Invalid entry: {offset}')
    else:
        print(f'Your Encoded transmission: {encode(message, offset)}')
elif get_option == 'D':
    message = input('Enter your encoded transmission: ')
    offset =int(input('Choose the shift (1-26): '))
    if offset < 1 or offset > 26:
        raise Exception(f'Invalid entry: {offset}')
    else:
        print(f'Your decoded transmission: {decode(message, offset)}')
else:
    raise Exception(f'Invalid option: {get_option}')