def main():
    word_dict = {
        "riot" : "disturbance of the public peace by 3 or more persons assembled together and acting with a common intent",
        "nephron" : "It is the structural and functional unit of kidney",
        "mischievous" : "causing or showing a fondness for causing trouble in a playful way",
        "rendezvous" : "a meeting at an agreed time and place",
        "heir":"a person legally entitled to the property of another on that person's death",
        "matrix" : "the cultural,social or political environment in which something develops",
        "aisle" : "a passage between rows of seats in a building such as a train, theatre,church or an aircraft",
        "lettuce" : "a cultivated plant of the daisy family, with edible leaves that're eaten in salads",
        "elusive" : "difficult to find, catch or achieve",
        "expedite" : "make happen sooner or be accomplished more quickly"
    }

    while True:
        word = input("Enter a word to find it's meaning:")
        if word == "":
            break
        if word in word_dict:
            print(word,":",word_dict[word])
            
main()      



