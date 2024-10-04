from game_data import data
from art import  logo, vs
import random
print(logo)

score = 0

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
       return user_guess == "a"
    else:
       return user_guess == "b"


account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")



    guess = input("Who has more followers? type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    a_followers_account = account_a["follower_count"]
    b_followers_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers_account, b_followers_account)

    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

