def step3(cipher_result_from_step2):


    while len(cipher_result_from_step2) < 114:
        cipher_result_from_step2+=cipher_result_from_step2

    return cipher_result_from_step2



def step2(cipher_result_from_step1):
    second_step = b""

    i = len(cipher_result_from_step1)-1

    while i >= 0:
        second_step+=bytes([cipher_result_from_step1[i]])
        i-=1

    return second_step


def decode_string(cipher, key, array_chelou, value_random):
    first_step = b""

    #array = [466, 59]

    i = len(cipher)-1

    while i >= 0:
        valid_index_for_key = ( ( ( (i + value_random) - array_chelou[ len(array_chelou) - 1] ) + 290 ) % len(key))

        last_byte = ord(cipher[i])
        actual_key_byte = ord(key[valid_index_for_key])

        logical = (( ~last_byte | ~actual_key_byte ) & ( last_byte | actual_key_byte ))

        first_step+=str.encode(chr(logical))
        i-=1




    print(f"Step 1 decoding: {first_step}")


    second_step = step2(first_step)

    print(f"Step 2 Reverse: {second_step}")

    third_step = step3(second_step)

    print(f"Step 3 Concatenate : {third_step}")


def decode_string_2(cipher, array_chelou, chelou2):
    final_string = b""

    d = ( ((489-array_chelou[len(array_chelou)-1]) + 290) % 21)

    i = 0
    while i < len(cipher):
        byte_cipher = ord(cipher[i])
        act = ord(chelou2[d])
        d+=1

        logical = (( ~byte_cipher & act ) | (~act & byte_cipher))

        final_string+=str.encode(chr(logical))
        i+=1


    print(final_string)



ci = '8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]8^;"E\\0`x~+N{\'x9O{+V]'
decode_string_2("M", [466, 212, 492], ci)
"""
cipher = '%mg\f\x1B\v"nq\\0\t\x15?\\r\x18\r\x1EA\x18\f\x13wC\b'

key = "2T]|_A+u!"


cipher = "sv\x0E'\x1C7\x1B \b60T|\n"
key = 'h0,%^Xkfz/ZG%P{Xd`C_Tfk:6'
decode_string(cipher, key, [466, 261], -28)
"""