import art
import game_data
import random
from replit import clear

def announce(celeb_a, celeb_b):
  print("")
  print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']} from {celeb_a['country']}")
  print(art.vs)
  print("")
  print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']} from {celeb_b['country']}")

def compare(celeb_a, celeb_b):
  if celeb_a['follower_count'] > celeb_b['follower_count']:
    return [celeb_a, 'A']
  return [celeb_b, 'B']

celeb_a = random.choice(game_data.data)
celeb_b = random.choice(game_data.data)
if celeb_a['name'] == celeb_b['name']:
  celeb_b = random.choice(game_data.data)
  
answer = compare(celeb_a, celeb_b)

score = 0

print(art.logo)
announce(celeb_a, celeb_b)
  
user_guess = input("Who has more followers? Type 'A' or 'B' ").upper()
while user_guess == answer[1]:
  score += 1
  clear()
  print(f"You are right! You score is: {score}")
  celeb_a = answer[0]
  celeb_b = random.choice(game_data.data)
  answer = compare(celeb_a, celeb_b)
  announce(celeb_a, celeb_b)
  user_guess = input("Who has more followers? Type 'A' or 'B' ").upper()
else:
  print(f"Sorry, that's wrong. Your final score is: {score}")