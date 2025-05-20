import plotext as plt

power_levels = {
    "Naruto": 9000,
    "Sasuke": 8500,
    "Madara": 12000,
    "Sakura": 5000,
}

personagens = list(power_levels.keys())
poder = list(power_levels.values())

plt.title("Niveis de poder so Naruto")
plt.xlabel("Personagens")
plt.ylabel("Niveis de poder")
plt.bar(personagens, poder)
plt.show()