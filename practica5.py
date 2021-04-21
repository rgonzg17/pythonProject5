import numpy as np

alf="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()"
msj_cifrado="ÁeóÍ ebá 5b-CeóÍósUÍCs sÍ2UeÍÚLVVpt)utÍoáÍez2ehÍÍíN1mX-ñjA1E-OmimjX-wOyimj3wPFé13iAimÚj-mj31-OXwÚjF-OwjjbmYf2áUspY7ÍíPomY íYy3KYí ÚoPbbmEYÓ YP:3mbYyÁLÁYY4v6z6(znmsnzh(v:6zW6fW6zvoz(vóp-z6(6MpWÉzxpOFpzzÍ.íÍa3ñcahuiÍa.Í3uV Ía,ua úc.uVáúua3ñca5y(Zj9aa)r7NOFyWOwóyOÁNuukYóRYOKyRYKdRkÁy(OOIiPúGTókCF5yaó95FCyCsaTó)aQAQóiZGZ("

clave_cifrado = np.array([64,5])

modulo = len(alf)

posicion_espacio_alf = alf.index(" ")

def asignar_numeros(msj_cifrado2):
    posiciones_msj_cifrado = list()
    rdict = dict([(x[1], x[0]) for x in enumerate(alf)])
    for caracter in msj_cifrado2:
        posiciones_msj_cifrado.append(rdict[caracter])
    return posiciones_msj_cifrado

def calcular_clave_cifrado(generacion):
    clave_cifrado = np.array([pow(64,(generacion+1))%modulo, (5*(generacion+1))%modulo])
    return clave_cifrado


def calcular_clave_descifrado(clave_cifrado):
    inverso_1 = modInv(clave_cifrado[0], modulo)
    clave_descifrado = np.array([inverso_1, (-inverso_1 * clave_cifrado[1]) % modulo])
    return clave_descifrado

def cifrar():
    msj ="RUBEN GONZALEZ GONZALEZ"
    posiciones = asignar_numeros(msj)
    newMsj = ""
    for elemento in posiciones:
        codificacion = alf[(elemento*clave_cifrado[0]+clave_cifrado[1])%modulo]
        newMsj += codificacion

    print(newMsj)
    return newMsj


def practica5():
    generacion = 0
    newAlf = list()
    msj_cifrado1 = msj_cifrado
    while(generacion<9):
        clave_cifrado = calcular_clave_cifrado(generacion)
        print(clave_cifrado)
        clave_descifrado = calcular_clave_descifrado(clave_cifrado)
        print(clave_descifrado)
        posiciones_msj_cifrado = asignar_numeros(msj_cifrado1)
        i = 0
        for i in range(len(msj_cifrado1)):
            posiciones_msj_cifrado[i] = (posiciones_msj_cifrado[i] * clave_descifrado[0] + clave_descifrado[1]) % modulo

        print(posiciones_msj_cifrado)
        cadena_original:str = ''
        cadena:str = ''
        j = 0
        for elemento in posiciones_msj_cifrado:
            cadena_original += msj_cifrado1[j]
            cadena += (alf[elemento])
            if((posiciones_msj_cifrado[j-1]==posicion_espacio_alf) and (posiciones_msj_cifrado[j]==posicion_espacio_alf)):
                break
            j+=1

        newAlf.append(cadena)
        print(cadena)
        print(cadena_original)
        msj_cifrado1 = msj_cifrado1.replace(cadena_original,'')
        print(msj_cifrado1)
        generacion+=1

    print(newAlf)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modInv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

