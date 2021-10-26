#Caio Ruan Soares Sousa - Ciência da Computação - Noite
#25/11/2021
pokémons = []
while True:
 print("=====================================================")
 print("1.Adicionar pokémons\n2.Remover pokémons\n3.Listar pokémons\n4.Pokémon por letra inicial\n5.Sair")
 opçoes = input("Escolha uma opção: ")
 if opçoes == "1":
      adicionar_pokémon = input("Adicione um pokémon: ") 
      pokémons.append(adicionar_pokémon)
      print(", ".join(pokémons))
 elif opçoes == "2":
     print(", ".join(pokémons))
     remover_pokémon = input("Remova um pokémon: ")
     pokémons.remove(remover_pokémon)
     print(", ".join(pokémons))
 elif opçoes == "3":
     print(f"foram encontrados {len(pokémons)} pokémons.")
     print(", ".join(pokémons))
 elif opçoes == "4":
     inicial = input("Inicial do pokémon: ")
     for i in pokémons:
         if i[0] == inicial.lower() or i[0] == inicial.upper():
             print(i)
 elif opçoes == "5":
     break
 else:
     print("Escolha uma opção válida!")
print("Boa sorte na jornada!")

  

  
  
   


  