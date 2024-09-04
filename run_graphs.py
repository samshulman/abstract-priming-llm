import logging
import json
import argparse
import os
import numpy as np
from collections import defaultdict
from openai import OpenAI
import re
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# file_name = "n13line_rooms_questions.jsonl"
# graph_name = "n13line_room"



file_name = "n15star_flowers_questions.jsonl"
graph_name = "n15star_flowers"


def run_evaluation(client, model, graph_type, q_type):
    with open(file_name, "r") as f:
        lines = f.readlines()
    lines = [json.loads(line.strip()) for line in lines if line.strip()]  
    for num, line in enumerate(lines):


        results_dict = {}
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": line["Description"] + " " + line[q_type],
                }
            ],
            temperature=0,
        )

        full_response = completion.choices[0].message.content
        answer_string = f"{q_type} Answer"
        stripped_ans = extract_path(full_response)
        results_dict["Question Type"] = q_type
		# results_dict["prompts"] = line[q_type]
		# results_dict["root"] = line["Root"]
        results_dict["correct answers"] = line[answer_string]
        results_dict["full responses"] = full_response
        results_dict["stripped response"] = stripped_ans
		# print(results_dict)
        jsons.append(results_dict)

def extract_path(response):
    return response.split(',')




model = "gpt-4-0613"
model_name = "gpt4"

# model = "gpt-3.5-turbo-0613"
# model_name = "gpt3.5"


# graphs = ['n7line', 'n7tree', 'n13line', 'n15star', 'n16cluster', 'n21star']

q_types = ["No Prime Question", "Both Prime Question", "Lexical Prime Question", "Structural Prime Question"]

# for graph_sel in graphs:
	
	
for q in q_types:
		
    jsons = []

    graph = graph_name

    print(graph + " " + q + " " + "starting")
    run_evaluation(client, model, graph, q)
    print(graph + " " + q + " " + "done")
       
    file_path = f"{graph}_results.json"
    
    # Read existing data
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            try:
                existing_data = json.load(json_file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    
    # Append new data
    existing_data.extend(jsons)
    
    # Write back to file
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
