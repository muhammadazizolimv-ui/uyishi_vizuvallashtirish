import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot, masofa, color="green", marker="o", linewidth=2.5)
plt.title("Sportchining yugurish masofasi")
plt.xlabel("Mashg‘ulot raqami")
plt.ylabel("Masofa (km)")
plt.grid(True, linestyle="--")
plt.show()

# Izoh:
# 1. Sportchining natijalari asosan o‘sish dinamikasiga ega bo‘lib, 1-mashg‘ulotdagi 2.0 km 6-mashg‘ulotga kelib 4.0 km ga yetgan.
# 2. Faqat 3-mashg‘ulotda masofa biroz (2.3 km gacha) qisqargan, qolgan barcha bosqichlarda barqaror o‘sish kuzatilgan.