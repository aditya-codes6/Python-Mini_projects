import random
item_list = ["rock","scissor","paper"]
user = input("Enter you move [rock,paper,scissor]")
comp_choice = random.choice(item_list)
print(f"User choice is {user} & computer choice is {comp_choice}")

if user == comp_choice:
   print("Both are same : MATCH IS TIE")

elif user == "rock":
   if comp_choice == "paper":
      print("Paper Covers Rock : COMPUTER WIN")
   else:
      print("Rock Smashes Scissor : YOU WIN")


elif user == "paper":
   if comp_choice =="rock":
      print("Paper Covers Rock : YOU WIN")
   else:
      print("Scissor Cuts Paper : COMPUTER WIN")

elif user == "scissor":
   if comp_choice == "paper":
      print("Scissor Cuts Paper :YPU WIN")
   else:
      print("Rock Smashes Scissor : COMPUTER WIN")
     