#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

def main():
    amount = input("Enter the number of questions: ")
    difficulty = input("Enter the difficulty (easy, medium, or hard): ")
    q_type = input("Enter the type (multiple or boolean): ")
    URL= f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={q_type}"
    
    data= requests.get(URL).json()

    print(URL)

    for q_data in data["results"]:
        question = q_data["question"]
        correct_ans = q_data["correct_answer"]
        all_answers = [correct_ans] + q_data["incorrect_answers"]
        
        print(question)
        for answer in all_answers:
            print(f"- {answer}\n")



if __name__ == "__main__":
    main()

