import numpy as np 
import json

def is_correct(stripped_responses, gold_labels):
    if len(stripped_responses) != len(gold_labels): return False
    for i in range(len(stripped_responses)):
            if gold_labels[i].lower().strip() in stripped_responses[i].lower().strip():
                pass
            else:
                return False
    return True

gpt4_file_paths = ["n16cluster_flowers_results_gpt4.json"]

for file_name in gpt4_file_paths:
    with open(file_name, 'r') as file:
    # with open("n7line_rooms_results_gpt4.json", 'r') as file:
    # with open("n7line_friends_results_gpt4.json", 'r') as file:
    # with open("n7line_flowers_results_gpt4.json", 'r') as file:
    # with open("n7tree_rooms_results_gpt4.json", 'r') as file:
    # with open("n7tree_friends_results_gpt4.json", 'r') as file:
    # with open("n7tree_flowers_results_gpt4.json", 'r') as file:
    # with open("n13line_rooms_results_gpt4.json", 'r') as file:
    # with open("n13line_friends_results_gpt4.json", 'r') as file:
    # with open("n13line_flowers_results_gpt4.json", 'r') as file:
    # with open("n15star_rooms_results_gpt4.json", 'r') as file:
    # with open("n15star_friends_results_gpt4.json", 'r') as file:
    # with open("n15star_flowers_results_gpt4.json", 'r') as file:
    # with open("n16cluster_rooms_results_gpt4.json", 'r') as file:
    # with open("n16cluster_friends_results_gpt4.json", 'r') as file:
    # with open("n16cluster_flowers_results_gpt4.json", 'r') as file:

    # with open("n7line_rooms_results_gpt3.5.json", 'r') as file:
    # with open("n7line_friends_results_gpt3.5.json", 'r') as file:
    # with open("n7line_flowers_results_gpt3.5.json", 'r') as file:
    # with open("n7tree_rooms_results_gpt3.5.json", 'r') as file:
    # with open("n7tree_friends_results_gpt3.5.json", 'r') as file:
    # with open("n7tree_flowers_results_gpt3.5.json", 'r') as file:
    # with open("n13line_rooms_results_gpt3.5.json", 'r') as file:
    # with open("n13line_friends_results_gpt3.5.json", 'r') as file:
    # with open("n13line_flowers_results_gpt3.5.json", 'r') as file:
    # with open("n15star_rooms_results_gpt3.5.json", 'r') as file:
    # with open("n15star_friends_results_gpt3.5.json", 'r') as file:
    # with open("n15star_flowers_results_gpt3.5.json", 'r') as file:

        data = json.load(file)
        no_prime= []
        both_prime = []
        lex_prime = []
        struct_prime = []
        unrelated_prime = []


        for item in data:
            if item["Question Type"] == "No Prime Question":
                no_prime.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "Both Prime Question":
                both_prime.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "Lexical Prime Question":
                lex_prime.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "Structural Prime Question":
                struct_prime.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "Unrelated Prime Question":
                unrelated_prime.append(is_correct(item["stripped response"], item["Correct Answer"]))
        
        print(file_name)
        print("No prime: ", np.mean(no_prime))
        print("Both prime: ", np.mean(both_prime))
        print("Lexical prime: ", np.mean(lex_prime))
        print("Structural prime: ", np.mean(struct_prime))
        print("Unrelated prime: ", np.mean(unrelated_prime))
