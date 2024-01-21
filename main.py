from game_data import data
import art
import random

#TODO: from the list output the first information then ask if the second one has higher or lower follwer

total_point = 0

print(art.logo)


def random_selection():
    return random.choices(data, k=2)
def compare():
    random_search_terms = random_selection()
    choice1 = random_search_terms[0]
    choice2 = random_search_terms[1]
    print(f"Compare A: {choice1["name"]}, {choice1["description"]}, from {choice1["country"]}")
    print(art.vs)
    print(print(f"Compare A: {choice2["name"]}, {choice2["description"]}, from {choice2["country"]}"))

    while True:
        choice = input("Who has more followers? Type 'A' or 'B' ").lower()
        if choice == "a" or choice == "b":
            break
    if choice == "a":
        if choice1["follower_count"] > choice2["follower_count"]:





compare()