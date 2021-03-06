import sys
import codecs
import argparse

import ConvAlphaBin
import DataEncryptionStandard

def get_content(filename, encoding):
    with open(filename, mode="r", encoding=encoding) as file:
        return file.read()

def pretty_message(args):
    message = ""
    if args.stdin:
        message = sys.stdin.read()
    elif args.message:
        message = args.message
    elif args.file:
        message = get_content(args.file, args.encoding)

    # return message.rstrip()
    return message.strip()


parser = argparse.ArgumentParser()

parser.add_argument("-e", "--encoding", action="store", type=str, default="UTF-8")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-k", "--key", action="store", type=str)
group.add_argument("-kf", "--key-file", action="store", type=str)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-s", "--stdin", action="store_true")
group.add_argument("-m", "--message", action="store", type=str)
group.add_argument("-f", "--file", action="store", type=str)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--cipher", action="store_true", help="to use the encryption method on the data")
group.add_argument("-d", "--decipher", action="store_true", help="to use the decryption method on the data")

args = parser.parse_args()


if args.cipher:
    message = pretty_message(args)
    binaries = ConvAlphaBin.conv_bin(message)

    key = args.key if args.key else get_content(args.key_file, args.encoding)

    encrypted_binaries = DataEncryptionStandard.compute(key, binaries, DataEncryptionStandard.Method.Cipher)

    # after python 3.7: sys.stdout.reconfigure(encoding=args.encoding)
    sys.stdout = codecs.getwriter(args.encoding)(sys.stdout.detach())
    sys.stdout.write(ConvAlphaBin.nib_vnoc(encrypted_binaries))
    # print(ConvAlphaBin.nib_vnoc(encrypted_binaries), end="")
elif args.decipher:
    message = pretty_message(args)
    binaries = ConvAlphaBin.conv_bin(message, fix=True)

    key = args.key if args.key else get_content(args.key_file, args.encoding)

    decrypted_binaries = DataEncryptionStandard.compute(key, binaries, DataEncryptionStandard.Method.Decipher)

    # after python 3.7: sys.stdout.reconfigure(encoding=args.encoding)
    sys.stdout = codecs.getwriter(args.encoding)(sys.stdout.detach())
    sys.stdout.write(ConvAlphaBin.nib_vnoc(decrypted_binaries))
    # print(ConvAlphaBin.nib_vnoc(encrypted_binaries), end="")
