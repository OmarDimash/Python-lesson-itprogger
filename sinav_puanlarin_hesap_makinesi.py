# 2 siniv sinaflari 
vize = int(input("vize sonucu:"))
final = int(input("final sonucu:"))
ort = vize * 0.5 + final * 0.5
print(ort)

if ort >= 50:
    print("Tebrikler, sınavı geçtin. Sınav puanın:", ort)
else:
    print("Sınavı geçemedin. Çalışmaya devam et. Sınav puanın:", ort)
