# DataEncryptionStandard

## Commandes utiles

```bash
# Ces trois commandes ont exactement la même fonction

echo toto | python3 DataEncryptionStandardCli.py --stdin --cipher --key="0101111001011011010100100111111101010001000110101011110010010001" > cipher.txt
python3 DataEncryptionStandardCli.py --message="toto" --cipher --key="0101111001011011010100100111111101010001000110101011110010010001" > cipher.txt
echo toto > message.txt && python3 DataEncryptionStandardCli.py --file="message.txt" --cipher --key="0101111001011011010100100111111101010001000110101011110010010001" > cipher.txt
```

## Déchiffrer un exemple

```bash
python3 DataEncryptionStandardCli.py  --decipher --file="Samples/Messages/Chiffrement_DES_de_1.txt" --key-file="Samples/Messages/Clef_de_1.txt" --encoding="ISO-8859-1"
```

## Windows VS Unix

```bash
# Unix
echo toto | python3 DataEncryptionStandardCli.py --stdin --cipher --key="0101111001011011010100100111111101010001000110101011110010010001" | python DataEncryptionStandardCli.py --stdin --decipher --key="0101111001011011010100100111111101010001000110101011110010010001"

# Windows (changer l'encodage)
echo toto | python DataEncryptionStandardCli.py --stdin --cipher --key="0101111001011011010100100111111101010001000110101011110010010001" --encoding="ISO-8859-1" | python DataEncryptionStandardCli.py --stdin --decipher --key="0101111001011011010100100111111101010001000110101011110010010001" --encoding="ISO-8859-1"
```
