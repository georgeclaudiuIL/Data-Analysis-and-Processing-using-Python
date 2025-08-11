
vocale = "aeiouAEIOU"
sir = "Salutare, ce mai faci?"


nou_sir = ""
for caracter in sir:
    if caracter not in vocale:
        nou_sir += caracter

print(nou_sir)

# SAU

print("".join(filter(lambda x: x not in vocale, sir)))

# SAU

def elimina_vocala(ch):
    return ch not in vocale
print("".join(filter(elimina_vocala, sir)))

# SAU

print("".join([ch for ch in sir if ch not in vocale]))