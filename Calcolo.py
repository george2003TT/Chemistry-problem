#Calculate the maximum amount of Br2 obtainable by reacting 6.322 g of KMnO4 dissolved in 200mL of water and 60 mL of a 48 wt% HBr solution (d = 1.490 g/mL)

def massa_Br2(moles_HBr):
    return moles_HBr * 159.8

def moles_HBr(percentuale, densita, peso_molecolare):
    return (percentuale * densita * 60 / 1000) / peso_molecolare

percentuale = 48
densita = 1.490
peso_molecolare = 80.9

moles_HBr = moles_HBr(percentuale, densita, peso_molecolare)
massa_Br2 = massa_Br2(moles_HBr)

print("La quantità massima di Br2 ottenibile è di", massa_Br2, "grammi")