def print_formatted(number):
    space = len(bin(number)[2::])
    for i in range(1,number+1):
        dec = str(i)
        octal = oct(i)[2::]
        hexa = hex(i)[2::]
        if hexa.isalpha:hexa = hexa.upper()
        binaire = bin(i)[2::]
        print(" "*(space-len(dec))+dec, " "*(space+1-len(octal))+octal, " "*(space+1-len(hexa))+hexa," "*(space+1-len(binaire))+binaire, sep="" )

number = 17
print_formatted(number)