show_instructions = input("have you played before?").lower()

if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

elif show_instructions == "no" or show_instructions == "n":
    print("instructions placeholder")

else:
    print("error. please answer yes or no")
