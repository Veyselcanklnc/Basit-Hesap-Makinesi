print("""**********
      'q' Tuşu ile Ayrılabilirsiniz.
      '1' Tuşu ile Toplayabilirsiniz.
      '2' Tuşu ile Çıkartabilirsiniz.
      '3' Tuşu ile Çarpabilirsiniz.
      '4' Tuşu ile Bölebilirsiniz.    
      **********""")
while True:
    islem = input("Çıkış için 'q' Tuşuna basabilirsiniz.")
    if islem == 'q':
        print("Çıkıyorum.")
        quit()
    elif islem == '1':
        print("----TOPLAMA İŞLEMİ----")
        sayi1 = int(input("1.Sayıyı Giriniz."))
        sayi2 = int(input("2.Sayıyı Giriniz."))
        print("{}  +  {}  =  {}".format(sayi1,sayi2, sayi1+sayi2))
    elif islem == '2':
        print("----ÇIKARMA İŞLEMİ----")
        sayi1 = int(input("1.Sayıyı Giriniz."))
        sayi2 = int(input("2.Sayıyı Giriniz."))
        print("{}  -  {}  =  {}".format(sayi1,sayi2, sayi1-sayi2))
    elif islem == '3':
        print("----ÇARPMA İŞLEMİ----")
        sayi1 = int(input("1.Sayıyı Giriniz."))
        sayi2 = int(input("2.Sayıyı Giriniz."))
        print("{}  *  {}  =  {}".format(sayi1,sayi2, sayi1*sayi2))
    elif islem == '4':
        print("----BÖLME İŞLEMİ----")
        sayi1 = int(input("1.Sayıyı Giriniz."))
        sayi2 = int(input("2.Sayıyı Giriniz."))
        print("{}  /  {}  =  {}".format(sayi1,sayi2, sayi1/sayi2))
    else:
        print("Sıkıntı Var.")

        
        