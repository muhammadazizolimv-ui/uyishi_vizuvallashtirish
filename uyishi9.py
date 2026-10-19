import matplotlib.pyplot as plt

kunlar = ["Dush", "Sesh", "Chor", "Pay", "Juma", "Shan", "Yak"]
faollik = [3, 5, 2, 6, 4, 7, 5]

plt.plot(kunlar, faollik, marker="o", color="teal")
plt.title("Haftalik faollik grafigi")
plt.xlabel("Kunlar")
plt.ylabel("Soat")
plt.grid(True)

plt.savefig("natija.png")
plt.show()