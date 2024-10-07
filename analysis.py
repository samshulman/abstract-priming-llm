import numpy as np 
import json

def is_correct(stripped_responses, gold_labels):
    if len(stripped_responses) != len(gold_labels): return False
    for i in range(len(stripped_responses)):
            if str(gold_labels[i]).lower().strip() in stripped_responses[i].lower().strip():
                pass
            else:
                return False
    return True

gpt4_file_paths = ["n7fork_results_gpt4.json"]

q_types = ["Mapping, Room Desc, Room Question", 
 "Mapping, Color Desc, Color Question",
 "Room Desc, Mapping, Room Question", 
 "Color Desc, Mapping, Color Question",
 "Mapping, Color Desc, Room Question",
 "Mapping, Room Desc, Color Question",
 "Color Desc, Mapping, Room Question",
 "Room Desc, Mapping, Color Question",
 "Mapping, Mixed Desc, Room Question",
 "Mapping, Mixed Desc, Color Question",
 "Mixed Desc, Mapping, Room Question",
 "Mixed Desc, Mapping, Color Question"]

for file_name in gpt4_file_paths:
    with open(file_name, 'r') as file:

        data = json.load(file)

        mrr = []
        mcc = []
        rmr = []
        cmc = []

        mcr = []
        mrc = []
        cmr = []
        rmc = []

        mxr = []
        mxc = []
        xmr = []
        xmc = []


        for item in data:
            if item["Question Type"] == "Mapping, Room Desc, Room Question":
                mrr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mapping, Color Desc, Color Question":
                mcc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Room Desc, Mapping, Room Question":
                rmr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Color Desc, Mapping, Color Question":
                cmc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mapping, Color Desc, Room Question":
                mcr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mapping, Room Desc, Color Question":
                mrc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Color Desc, Mapping, Room Question":
                cmr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Room Desc, Mapping, Color Question":
                rmc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mapping, Mixed Desc, Room Question":
                mxr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mapping, Mixed Desc, Color Question":
                mxc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mixed Desc, Mapping, Room Question":
                xmr.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
            elif item["Question Type"] == "Mixed Desc, Mapping, Color Question":
                xmc.append(is_correct(item["Stripped Response"], item["Correct Answer"]))
        
        print(file_name)
        print("Mapping, Room Desc, Room Question: ", np.mean(mrr))
        print("Mapping, Color Desc, Color Question: ", np.mean(mcc))
        print("Room Desc, Mapping, Room Question: ", np.mean(rmr))
        print("Color Desc, Mapping, Color Question: ", np.mean(cmc))
        print("Mapping, Color Desc, Room Question: ", np.mean(mcr))
        print("Mapping, Room Desc, Color Question: ", np.mean(mrc))
        print("Color Desc, Mapping, Room Question: ", np.mean(cmr))
        print("Room Desc, Mapping, Color Question: ", np.mean(rmc))
        print("Mapping, Mixed Desc, Room Question: ", np.mean(mxr))
        print("Mapping, Mixed Desc, Color Question: ", np.mean(mxc))
        print("Mixed Desc, Mapping, Room Question: ", np.mean(xmr))
        print("Mixed Desc, Mapping, Color Question: ", np.mean(xmc))
