import random

while True:
  choices=["snake","water","gun"]
  n=input("\nEnter Snaker/Water/Gun ")
  n=n.lower()
  while n not in choices:
    n=input("Invalid choice. Choose Snake/Water/Gun")

  guess = random.choice(choices)
  if n==guess:
    print(f"\nYou both chose {n}\n")
    print("There is a tie\n")
  elif (n=="Snake" and guess=="Gun") or (n=="Water" and guess=="Snake") or (n=="Gun" and guess =="Water"):
    print(f"\nYour choice is {n}")
    print(f"Computer choice is {guess}\n")
    print("You lost!!!\n")
  else:
    print(f"\nYour choice is {n}")
    print(f"Computer choice is {guess}\n")
    print("You won!!!\n")

  s=input("Do you want to continue(Y/N): ")
  if s.upper()!='Y':
    break
