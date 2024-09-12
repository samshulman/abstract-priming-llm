# 5 total  - 1 per q_type

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def calculate_accuracy(directory, q_type, model_name):
	# feed in test_results/gpt3.5 of test_results/gpt4

	# go through each graph's directory and find the file 
	# with the question type being targetted q_type

	graphs = ['n7line', 'n7tree', 'n13line', 'n15star', 'n16cluster', 'n21star']

	results = []

	for graph in graphs:
		graph_folder_path = f'{graph}_test_results_{model_name}'
		folder_path = os.path.join(directory, graph_folder_path)

		print(graph_folder_path)
		

		if os.path.exists(folder_path):
			res_filename = f'{graph}_results_{q_type}_{model_name}.json'
			res_filepath = os.path.join(folder_path, res_filename)

			

			if os.path.exists(res_filepath):
				with open(res_filepath, 'r') as file:
					data = json.load(file)
					total_prompts = 0
					total_correct = 0

					for item in data:
						total_prompts += 1
						stripped_response = item['stripped response'] if item['stripped response'] else ''
						if (q_type == "Room Question" or q_type == "Room QuestionB") and stripped_response != "the lobby":
							stripped_response = item['stripped response'][0]
						
						correct_ans = str(item['correct answers']).lower()
						print(stripped_response)
						print(correct_ans)

						if str(stripped_response) == str(correct_ans):
							total_correct += 1
					
					accuracy = total_correct / total_prompts if total_prompts > 0 else 0
					results.append({'graph': graph, 'total accuracy': accuracy})

	df = pd.DataFrame(results)
	print(df)
	df.to_csv(f'accuracy/{model_name}/{q_type}_accuracy_{model_name}.csv', index=False)
	
	graph_names = [result['graph'] for result in results]
	accuracies = [result['total accuracy'] for result in results]
	
	plt.bar(range(len(graph_names)), accuracies, align='center')
	plt.xlabel('Graph')
	plt.ylabel('Total Accuracy')
	plt.title(f'Accuracy Results for Different Graphs for {q_type}')
	plt.xticks(range(len(graph_names)), graph_names)  # Specify the tick labels
	plt.tight_layout()
	plt.show()



q_types = ['Path Question', 'Nstep Question', 'Nstep QuestionB', 'Room Question', 'Room QuestionB']
# model_name = "gpt 4"
model_name = "gpt3.5"

for q_type in q_types:
	calculate_accuracy(f'test_results/{model_name}', q_type, model_name)