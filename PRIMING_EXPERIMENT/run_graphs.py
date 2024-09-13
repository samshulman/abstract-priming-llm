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

# graph_names = ["n7line_rooms", "n7line_friends", "n7line_flowers", "n7tree_rooms", "n7tree_friends", "n7tree_flowers", "n13line_rooms", "n13line_friends", "n13line_flowers", "n15star_rooms", "n15star_friends", "n15star_flowers", "n16cluster_rooms", "n16cluster_friends", "n16cluster_flowers"]
graph_names = ["n15star_rooms", "n15star_friends", "n15star_flowers", "n16cluster_rooms", "n16cluster_friends", "n16cluster_flowers"]

for graph_title in graph_names:
    graph_name = graph_title

    file_name = f"{graph_name}_questions.jsonl"


    def run_evaluation(client, model, graph_type, q_type):
        with open(file_name, "r") as f:
            lines = f.readlines()
        lines = [json.loads(line.strip()) for line in lines if line.strip()]  
        for num, line in enumerate(lines):
        
            results_dict = {}
            
            # check if no prime question type 
            if q_type == "No Prime Question":
                
                completion = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an AI assisant designed to help answer questions about various scenarios. Please answer based on the provided information",
                        },
                        {
                            "role": "user",
                            "content": line[q_type],
                        }
                    ],
                    temperature=0,
                )

            else: 

                user1_message = f"{q_type} User1"
                assisant_message = f"{q_type} Assistant"
                user2_message = f"{q_type} User2"

                completion = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an AI assisant designed to help answer questions about various scenarios. Please answer based on the provided information",
                        },
                        {
                            "role": "user",
                            "content": line[user1_message],
                        },
                        {
                            "role": "assistant",
                            "content": format_content(line[assisant_message]),
                        },
                        {
                            "role": "user",
                            "content": line[user2_message],
                        }
                    ],
                    temperature=0,
                )

            full_response = completion.choices[0].message.content
            answer_string = f"{q_type} Answer"
            stripped_ans = extract_path(full_response)
            results_dict["Question Type"] = q_type
            results_dict["Correct Answer"] = line[answer_string]
            results_dict["full responses"] = full_response
            results_dict["stripped response"] = stripped_ans
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


    q_types = ["No Prime Question", "Both Prime Question", "Lexical Prime Question", "Structural Prime Question", "Unrelated Prime Question"]
        
        
    for q in q_types:
            
        jsons = []

        graph = graph_name

        print(graph + " " + q + " " + "starting")
        run_evaluation(client, model, graph, q)
        print(graph + " " + q + " " + "done")
        
        file_path = f"{graph}_results_{model_name}.json"
        
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
