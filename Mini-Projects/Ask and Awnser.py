#Ask and Awnser Program

def questions():
    q1 = "How often do you eat?\n"
    q2 = "Would you say you were happy?\n"
    q3 = "How old were you when you first found out you were adoped?\n"
    questions = [q1,q2,q3]
    awnsers = []
    for q in questions:
        awnser = input(q)
        awnsers.append(awnser)
        print("Your awnser was: " + awnser)
        print(awnsers)




if __name__ == "__main__":
    questions()