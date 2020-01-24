#####################################################
#		   	 	DICTIONNAIRE BINAIRE 64				#
#####################################################

ALPHABET = ""
ALPHABET+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"#Les 26 lettres de l'alphabet en majuscule (0-25)
ALPHABET+="abcdefghijklmnopqrstuvwxyz"#Les 26 lettres de l'alphabet en minuscule (26-51)
ALPHABET+=" " #caractère 52 : espace
ALPHABET+="." #caractère 53 : point
ALPHABET+="," #caractère 54 : virgule
ALPHABET+="!" #caractère 55 : point d'exclamation
ALPHABET+="?" #caractère 56 : point d'intérogation
ALPHABET+="'" #caractère 57 : apostrophe
ALPHABET+='"' #caractère 58 : guillemet
ALPHABET+="é" #caractère 59 : e accent aïgu
ALPHABET+="è" #caractère 60 : e accent grave
ALPHABET+="à" #caractère 61 : a accent aïgu
ALPHABET+="-" #caractère 62 : tiret
ALPHABET+="\n" #caractère 63 : saut de ligne


#Dans cet alphabet les caractères vont de 0 à 63.
#En binaire ça donne un champ de valeur de 0 à 111111(=1+2+4+8+16+32=63)
#ALPHABETBINAIRE est un tableau avec les nombres en binaire
ALPHABETBINAIRE=dict()
for i in range(0, 64) :
	x=bin(i)
	y='00000'+x[2:]
	ALPHABETBINAIRE[i]=""
	for k in range(-6, 0, 1):
		ALPHABETBINAIRE[i]+=y[k]

#Renvoie la chaine de caractère txt avec uniquement les caractères de l'alphabet.
def FiltreTXT(txt) :
	res=""
	for c in txt :
		if(ALPHABET.find(c)!=-1) : res+=c
		elif(c=='ê' or c=='ë') : res+='e'
		elif(c=='â') : res+='a'
		elif(c=='ç') : res+='c'
		elif(c=='î') : res+='i'
		elif(c=='Ç') : res+='C'
		elif(c=='ù' or c=="û") : res+='u'
		elif(c=='ô') : res+='o'
		elif(c=='Ô') : res+='O'
		elif(c=='œ') : res+='oe'
		elif(c=="À") : res+='A'
		elif(c=="È" or c=="É") : res+='E'
	return res
	
#Prend en paramètre un texte et renvoie la chaine binaire associée (en suivant le dictionnaire)
def conv_bin(txt) :
	X=""
	for c in FiltreTXT(txt) : 
		i=ALPHABET.find(c)
		if(i!=-1) : X+=ALPHABETBINAIRE[i]
	return X

#Fait l'inverse de conv_bin : prend une chaine binaire et renvoie les caractères
def nib_vnoc(txt) :
	n=len(txt)
	res=""
	i=0
	while(i<n or i%6!=0) : 
		if(i%6==0) : paquet_binaire="" 
		try : c=txt[i]
		except : c="0"
		if(c=="1") : paquet_binaire+="1"
		else : paquet_binaire+="0"
		i+=1
		if(i%6==0) : 
			for b in ALPHABETBINAIRE : 
				if(ALPHABETBINAIRE[b]==paquet_binaire) :
					res+=ALPHABET[b]
					break
	
	return res

#Test
txt0 = "Je teste au stérone !? ^_^"
txt1 = conv_bin(txt0)
txt2 = nib_vnoc(txt1)
# print('txt0', txt0)
# print('txt1', txt1)
# print('txt2', txt2)
