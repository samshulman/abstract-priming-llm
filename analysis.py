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

gpt4_file_paths = ["n7tree_rooms_results_gpt4.json"]

for file_name in gpt4_file_paths:
    with open(file_name, 'r') as file:

        data = json.load(file)
        ac = []
        an = []
        pc = []
        pn = []
        mc = []
        mn = []


        for item in data:
            if item["Question Type"] == "abstract desc characteristic question":
                ac.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "abstract desc name question":
                an.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "path desc characteristic question":
                pc.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "path desc name question":
                pn.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "mixed desc characteristic question":
                mc.append(is_correct(item["stripped response"], item["Correct Answer"]))
            elif item["Question Type"] == "mixed desc name question":
                mn.append(is_correct(item["stripped response"], item["Correct Answer"]))
        
        print(file_name)
        print("AC: ", np.mean(ac))
        print("AN: ", np.mean(an))
        print("PC: ", np.mean(pc))
        print("PN: ", np.mean(pn))
        print("MC: ", np.mean(mc))
        print("MN: ", np.mean(mn))
