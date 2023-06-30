def first_template(n):
    number1=input("Enter a number:")
    measure_of_time=input("Enter the measure of time:")
    mode_of_transportation=input("Enter the means of transportation:")
    adjective=input("Enter the adjective that describes the place:")
    adjective2=input("Enter an adjective to describe the noun:")
    noun=input("Enter the first noun:")
    color=input("Enter the color:")
    body_part=input("Enter the body part:")
    verb=input("Enter a verb:")
    number2=input("Enter a number:")
    noun2=input("Enter the noun2:")
    noun3=input("Enter the noun3 here:")
    body_part2=input("Enter the 2nd body part:")
    noun4=input("Enter the 4th noun:")
    adjective3=input("Enter an adjecive:")
    silly_word=input("Enter a silly word here:")
    noun5=input("Enter a noun here:")
    return f"hi {number1}, here are the {measure_of_time}, new {mode_of_transportation},{adjective3}, {adjective}," \
           f"{adjective2},{noun5},{silly_word},{noun4},{verb},{verb},{body_part2},{noun2},{number2},{body_part},{noun3},{color},{noun}"

print(first_template(1))