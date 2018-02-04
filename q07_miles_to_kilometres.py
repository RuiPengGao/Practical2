#miles to kilometers

print("Miles\tKilometers\tKilometres\tMiles")

for i in range(0,10):
    Miles1 = i + 1
    Kilo1 = Miles1 * 1.609
    Kilo2 = 20 + (i * 5)
    Miles2 = Kilo2 / 1.609
    print ("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(Miles1, Kilo1, Kilo2, Miles2))
