import random

def difficulty_handler(input_string):
  while True:
    response = input(input_string)
    if response.lower() == 'easy' or response.lower() == 'hard':
      break
    print("I didn't understand that...")
  return response.lower()

def guess_handler(input_string):
  error_message = "Please enter a number between 1 and 100."
  while True:
    try:
      response = int(input(input_string))
      if response >= 1 and response <= 100:
        return response
    except ValueError:
      print(error_message)
    print(error_message)  

target_number = random.randint(1, 100)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
difficulty = difficulty_handler("Choose a difficulty. Type 'easy' or 'hard': ")
turns = 10
if difficulty == "hard":
  turns /= 2
  turns = int(turns)
while turns:
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = guess_handler("Make a guess: ")
  if guess == target_number:
    break
  elif guess > target_number:
    print("Too high.")
  else:
    print("Too low.")
  turns -= 1
  if turns: 
    print("Guess again.")
if turns:
  print(f"You got it! The answer was {target_number}")
else:
  print("You've run out of guesses. Refresh the page to run again.")
