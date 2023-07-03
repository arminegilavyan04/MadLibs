import random
choice_template= input("Please choose your desired number(1,2 or 3). If you don't have a choice-select 'r':")
def first_template():
    number=input("Enter a number:")
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
    adjective3=input("Enter an adjective:")
    silly_word=input("Enter a silly word here:")
    return f''' It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. 
                There are nurses here who have {color} {body_part}.If someone wants to come into my room I told them that they have to {verb} first. 
                I’ve decorated my room with {number2} {noun2}.
                Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. 
                I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun} !'''


def second_template():
    persons_name=input("Enter a person name:")
    noun=input("Enter a noun:")
    adjective_feeling=input("Enter an adjective that describes a feeling:")
    verb=input("Enter a verb:")
    adjective_feeling2 = input("Enter an adjective that describes a feeling:")
    animal=input("Enter an animal:")
    verb2=input("Enter a verb:")
    color=input("Enter a color:")
    verb_ing=input("Enter a verb ending in ing:")
    adverb_ly=input("Enter an adverb ending in ly:")
    number=input("Enter a number:")
    measure_of_time=input("Enter the measure of time:")
    silly_word=input("Enter a silly word:")
    noun2=input("Enter a noun here:")
    return f'''This weekend I am going camping with {persons_name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent. 
           I am {adjective_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. 
           While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}. 
           Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}.
           If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!'''


def third_template():
    persons_name=input("Enter a person name:")
    adjective = input("Enter an adjective:")
    adjective2=input("Enter an adjective:")
    magical_creatures=input("Enter a plural example of magical creatures:")
    adjective3=input("Enter an adjective:")
    room=input("Enter a room name in a house:")
    color=input("Enter a color:")
    animal = input("Enter an animal:")
    noun=input("Enter a noun here:")
    noun2=input("enter a noun:")
    place=input("Enter a place here:")
    noun3=input("Enter a plural example of a noun:")
    adjective4=input("Enter an adjective:")
    noun4=input("Enter a plural form of a noun:")
    number=input("Enter a number:")
    time_measure=input("Enter a time measure:")
    verb=input("Enter a verb ending with ing:")
    adjective5=input("Enter an adjective:")
    noun5=input("Enter a noun:")
    return f'''Dear {persons_name}, I am writing to you from a {adjective} castle in an enchanted forest. 
           I found myself here one day after going for a ride on a {color} {animal} in {place}. 
           here are {adjective2} {magical_creatures} and {adjective3} {magical_creatures} here! 
           fn the {room} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}.
           It feels as though I have lived here for {number} {time_measure}." 
           I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!'''


def choices(choice_template):
    number=['1','2','3']
    if choice_template == "1":
        print(first_template())
    elif choice_template == "2":
        print(second_template())
    elif choice_template == "3":
        print(third_template())
    elif choice_template == "r":
        random_state = random.choice(number)
        return choices(random_state)
    else:
        print("Sorry, we don't have a template like that")

choices(choice_template)
