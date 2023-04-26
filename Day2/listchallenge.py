#!/usr/bin/env python3

def main():
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]
    wordbank.append(4)
    num = int(input("a number between 0 and 11: "))
    student= tlgstudents[num]
    print(f"{student} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
