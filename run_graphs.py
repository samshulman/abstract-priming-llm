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


graph_strings = ['n7line', 'n7tree', 'n7fork', 'n7star', 'n7bone']
graph_strings_double = ['n7line_double', 'n7tree_double', 'n7fork_double', 'n7star_double', 'n7bone_double']



def run_evaluation(client, model, graph_type, q_type):
    with open(file_name, "r") as f:
        lines = f.readlines()
    lines = [json.loads(line.strip()) for line in lines if line.strip()]  
    for num, line in enumerate(lines):
    
        results_dict = {}
        print(num, "line starting")

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assisant designed to help answer questions about various scenarios. Please answer based on the provided information.",
                },
                {
                    "role": "user",
                    "content": line[q_type],
                }
            ],
            temperature=0,
        )

        full_response = completion.choices[0].message.content
        answer_string = f"{q_type} Answer"
        stripped_ans = extract_path(full_response)
        results_dict["Question Type"] = q_type
        results_dict["Correct Answer"] = line[answer_string]
        results_dict["Full Responses"] = full_response
        results_dict["Stripped Response"] = stripped_ans
        jsons.append(results_dict)
        print(num, "line done")

def extract_path(response):
    response_list = response.split(', ')
    for response in response_list:
        response = response.strip().lower()
        response = response.replace("room", "").replace(" ", "")
    return response_list

def format_content(content):
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        return ' '.join(map(str, content))
    else:
        return str(content)



model = "gpt-4-0613"
model_name = "gpt4"

# model = "gpt-3.5-turbo-0613"
# model_name = "gpt3.5"

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
    
for graph_name in graph_strings:
    
    file_name = f"{graph_name}_questions.jsonl"

    for q in q_types:
            
        jsons = []

        print(graph_name + " " + q + " " + "starting")
        run_evaluation(client, model, graph_name, q)
        print(graph_name + " " + q + " " + "done")
        
        file_path = f"{graph_name}_results_{model_name}.json"
        
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
