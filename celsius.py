inp = float(input("Jaka dzisiaj temperatura?(stopnie celsiusza)"))
if inp < 10:
    print("zimno")
elif inp < 20:
    print("chodno")
elif inp < 30:
    print("ciepo")
else:
    print("gorąco")