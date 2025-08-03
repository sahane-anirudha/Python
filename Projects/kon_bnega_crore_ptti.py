questions = [
    ["What is the national animal of India?", "Tiger", "Lion", "Elephant", "Leopard", 1],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", 3],
    ["Who invented the light bulb?", "Isaac Newton", "Albert Einstein", "Thomas Edison", "Nikola Tesla", 3],
    ["Which is the largest continent?", "Africa", "Europe", "Asia", "Australia", 3],
    ["Which instrument measures temperature?", "Barometer", "Thermometer", "Hygrometer", "Altimeter", 2],
    ["What is H2O commonly known as?", "Salt", "Acid", "Water", "Hydrogen", 3],
    ["What color do you get when you mix red and white?", "Pink", "Purple", "Orange", "Brown", 1],
    ["Which bird is known for mimicking human speech?", "Parrot", "Pigeon", "Crow", "Sparrow", 1],
    ["How many planets are in the Solar System?", "7", "8", "9", "10", 2],
    ["Which is the largest internal organ in the human body?", "Heart", "Liver", "Lung", "Kidney", 2]
]


for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check whether the answer is correct or not............

    a=int(input("Enter your Answer .1 for a,2 for b,3 for c,4 for d:"))
    if(question[5]==a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the Correct answer was{question[5]}")
        print("Better luck next time !!!")
        break