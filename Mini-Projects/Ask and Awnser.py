#Ask and Awnser Program

def questions():
    q1 = "How often do you eat?\n"
    q2 = "Would you say you were happy?\n"
    q3 = "How old were you when you first found out you were adoped?\n"
    questions = [q1,q2,q3]

    for q in questions:
        input(q)



if __name__ == "__main__":
    questions()