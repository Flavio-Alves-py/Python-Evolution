#Ask and Awnser Program

def questions():
    q1 = "How often do you eat?"
    q2 = "Would you say you were happy?"
    q3 = "How old were you when you first found out you were adoped?"
    questions = [q1,q2,q3]

    for q in questions:
        input(q,"\n")



if __name__ == "__main__":
    questions()