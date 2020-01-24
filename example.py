import glob
import re

import ConvAlphaBin
import DataEncryptionStandard

"""
Test 1
"""
key = "0101111001011011010100100111111101010001000110101011110010010001"
binaries = "1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"

encrypted_binaries = DataEncryptionStandard.compute(key, binaries, DataEncryptionStandard.Method.Cipher)
decrypted_binaries = DataEncryptionStandard.compute(key, encrypted_binaries, DataEncryptionStandard.Method.Decipher)

assert binaries in decrypted_binaries, "[Test 1] Messages are different"

binaries = DataEncryptionStandard.compute("0101111001011011010100100111111101010001000110101011110010010001", ConvAlphaBin.conv_bin("toto"), DataEncryptionStandard.Method.Cipher)
print(binaries)
# print(ConvAlphaBin.nib_vnoc(DataEncryptionStandard.compute("0101111001011011010100100111111101010001000110101011110010010001", "000000011001010010111100100101010100010001011000111011100000100000", DataEncryptionStandard.Method.Decipher)))
exit()

"""
Test 2
"""
key = "0101111001011011010100100111111101010001000110101011110010010001"
binaries = ConvAlphaBin.conv_bin("Hello world")

encrypted_binaries = DataEncryptionStandard.compute(key, binaries, DataEncryptionStandard.Method.Cipher)
decrypted_binaries = DataEncryptionStandard.compute(key, encrypted_binaries, DataEncryptionStandard.Method.Decipher)

assert binaries in decrypted_binaries, "[Test 2] Messages are different"

"""
Test 3
"""
for encrypted_filename in glob.glob("Samples/Messages/Chiffrement_DES_de_*.txt"):
    capture = re.search(".+?([0-9]+)\.txt", encrypted_filename)
    if capture:
        index = capture.group(1)
        with open("Samples/Messages/Clef_de_" + index + ".txt", mode="r", encoding="ISO-8859-1") as key_file:
            key = key_file.read()
            with open(encrypted_filename, mode="r", encoding="ISO-8859-1") as encrypted_file:
                encrypted_message = encrypted_file.read()
                encrypted_binaries = ConvAlphaBin.conv_bin(encrypted_message)

                decrypted_binaries = DataEncryptionStandard.compute(key, encrypted_binaries, DataEncryptionStandard.Method.Decipher)
                decrypted_message = ConvAlphaBin.nib_vnoc(decrypted_binaries)

                print("-------------------------------------------------------------------------------------------------------------")
                print("Contenu du fichier " + encrypted_filename)
                print("-------------------------------------------------------------------------------------------------------------")
                print(decrypted_message)

                """
                with open("Samples/Resultats/Dechiffrement_DES_de_" + index + ".txt", mode="w", encoding="UTF-8") as file:
                    file.write(decrypted_message)
                """
