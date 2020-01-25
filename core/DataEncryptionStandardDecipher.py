from core import Tools


def run(key, binaries):
    if len(key) != 64:
        raise Exception("The key must be 64-bit size")
    elif len(binaries) % 64 > 0:
        raise Exception("The message must be 64-bit multiple size")

    key = [int(char) for char in key]
    binaries = [int(char) for char in binaries]

    constants = Tools.constants()

    PI   = constants["PI"][0]
    PI_I = constants["PI_I"][0]
    E    = constants["E"][0]
    CP_1 = constants["CP_1"][0]
    CP_2 = constants["CP_2"][0]
    S    = constants["S"]
    PERM = constants["PERM"][0]

    """
    Permutation de CP_1 par key
    """
    CP_1_K = Tools.permutation(key, CP_1, 64)

    G = CP_1_K[0:28]
    D = CP_1_K[28:56]

    """
    16 fois :
        Ecraser G et D par leur décalé de 1 bit vers la gauche
        Kn est le résultat de la permutation par CP_2 de la concaténation de G et D
    """
    Kn = [0 for i in range(16)]
    for i in range(len(Kn)):
        G = Tools.leftShift(G)
        D = Tools.leftShift(D)

        Kn[i] = Tools.permutation(G + D, CP_2, 56)

    """
    Paquetage de binaries
    """
    Mn = Tools.wrap(binaries)
    chunks = list()

    for chunk in Mn:
        PI_Mn_ = chunk
        """
        Permutation de PI par PI_Mn_
        """
        Mn_ = Tools.permutation(PI_Mn_, PI, 64)

        G = Mn_[0:32]
        D = Mn_[32:64]

        for i in range(16):
            PSEDXorKnXorG = D[:]

            """
            Permutation de E par G (expension sur 48 bits)
            """
            ED = Tools.permutation(G, E, 48)

            """
            Calculer ED ^ Kn
            """
            EDXorKn = Tools.xor(ED, Kn[15 - i])

            """
            Découpage de EDXorKn en blocs de 6 bits
            """
            Bn = [
                EDXorKn[0:6],
                EDXorKn[6:12],
                EDXorKn[12:18],
                EDXorKn[18:24],
                EDXorKn[24:30],
                EDXorKn[30:36],
                EDXorKn[36:42],
                EDXorKn[42:48]
            ]
            SEDXorKn = list()

            for j in range(8):
                n1 = Tools.sumBinary([Bn[j][0], Bn[j][5]])
                """
                (B1[0] << 1) | B1[5]
                """
                m1 = Tools.sumBinary(Bn[j][1:5])
                """
                (B1[1] << 3) | (B1[2] << 2) | (B1[3] << 1) | B1[4]
                """

                Sn = S[j][n1][m1]
                SEDXorKn += Tools.toBinary(Sn, 4)

            """
            Permutation de SEDXorKn par PERM
            """
            PSEDXorKn = Tools.permutation(SEDXorKn, PERM, 32)

            D = G[:]
            """
            Calculer PSEDXorKn ^ PSEDXorKn
            """
            G = Tools.xor(PSEDXorKnXorG, PSEDXorKn)

        Mn_ = G + D

        """
        Permutation de PI_I par Mn_
        """
        chunks += Tools.permutation(Mn_, PI_I, 64)

    return Tools.toString(chunks)
