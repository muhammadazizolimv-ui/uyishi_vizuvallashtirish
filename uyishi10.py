import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha_ball = sum(ballar) / len(ballar)

print(f"Eng yuqori ball: {eng_yuqori}")
print(f"Eng past ball: {eng_past}")
print(f"O'rtacha ball: {ortacha_ball:.2f}")

plt.bar(ismlar, ballar, color="coral")
plt.title("O‘quvchilarning imtihon natijalari")
plt.xlabel("O‘quvchilar")
plt.ylabel("Ballar")
plt.grid(axis="y", linestyle="--")

plt.savefig("oquvchilar_natijasi.png")
plt.show()
