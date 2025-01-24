# frutas = ["banana","maça","uva","pera","manga"]

# for fruta in frutas:
#     print(fruta)
    
fruits = []

print("Digite 'sair' quando a lista estiver completa")
while True:
    fruit = input("Digite o nome da fruta:")
    if fruit == "sair":
        break
    fruits.append(fruit)
    
print(fruits)