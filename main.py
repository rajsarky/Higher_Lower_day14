from game_data import data
import art
import random

total_point = 0

print(art.logo)


def point_calculator(points):
    global total_point
    total_point += points


def get_total_points():
    return total_point


def random_selection():
    return random.sample(data, k=2)


def compare():
    random_search_terms = random_selection()
    choice1 = random_search_terms[0]
    choice2 = random_search_terms[1]
    print(f"Compare A: {choice1["name"]}, {choice1["description"]}, from {choice1["country"]}")
    print(art.vs)
    print(f"Compare B: {choice2["name"]}, {choice2["description"]}, from {choice2["country"]}")

    while True:
        choice = input("Who has more followers? Type 'A' or 'B':   \n").lower()
        if choice == "a" or choice == "b":
            break
    if choice == "a":
        if choice1["follower_count"] > choice2["follower_count"]:
            point_calculator(1)
            print(f"You're right! Current score: {get_total_points()}")
            compare()
        else:
            print(f"Sorry, that's wrong. Final score: {total_point}")
    else:
        if choice2["follower_count"] > choice1["follower_count"]:
            point_calculator(1)
            print(f"You're right! Current score: {get_total_points()}")
            compare()
        else:
            print(f"Sorry, that's wrong. Final score: {total_point}")


compare()
