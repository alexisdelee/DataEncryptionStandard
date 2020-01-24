import glob
import re

import DESEncrypt
import DESDecrypt
import ConvAlphaBin

"""
Test 1
"""
key = "0101111001011011010100100111111101010001000110101011110010010001"
binaries = "1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"

encrypted_binaries = DESEncrypt.run(key, binaries)
decrypted_binaries = DESDecrypt.run(key, encrypted_binaries)

assert binaries in decrypted_binaries, "[Test 1] Messages are different"

"""
Test 2
"""
key = "0101111001011011010100100111111101010001000110101011110010010001"
binaries = ConvAlphaBin.conv_bin("Hello world")

encrypted_binaries = DESEncrypt.run(key, binaries)
decrypted_binaries = DESDecrypt.run(key, encrypted_binaries)

assert binaries in decrypted_binaries, "[Test 2] Message are different"

"""
Test 3
"""
for encrypted_filename in glob.glob("Messages/Chiffrement_DES_de_*.txt"):
    capture = re.search(".+?([0-9]+)\.txt", encrypted_filename)
    if capture:
        index = capture.group(1)
        with open("Messages/Clef_de_" + index + ".txt", mode="r", encoding="ISO-8859-1") as key_file:
            key = key_file.read()
            with open(encrypted_filename, mode="r", encoding="ISO-8859-1") as encrypted_file:
                encrypted_message = encrypted_file.read()
                encrypted_binaries = ConvAlphaBin.conv_bin(encrypted_message)

                decrypted_binaries = DESDecrypt.run(key, encrypted_binaries)
                decrypted_message = ConvAlphaBin.nib_vnoc(decrypted_binaries)

                print("-------------------------------------------------------------------------------------------------------------")
                print("Contenu du fichier " + encrypted_filename)
                print("-------------------------------------------------------------------------------------------------------------")
                print(decrypted_message)

                """
                with open("Resultats/Dechiffrement_DES_de_" + index + ".txt", mode="w", encoding="UTF-8") as file:
                    file.write(decrypted_message)
                """
