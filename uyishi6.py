import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

eng_kop = mahsulotlar[sotuv.index(max(sotuv))]
eng_kam = mahsulotlar[sotuv.index(min(sotuv))]
print(f"Eng ko'p sotilgan: {eng_kop}")
print(f"Eng kam sotilgan: {eng_kam}")

plt.bar(mahsulotlar, sotuv, color="purple")
plt.title("Bir haftalik mahsulot savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.show()