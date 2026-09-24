import math
class GradeSystem:
    def __init__(self):
        self.num_students = 0
        self.scores = []
        self.grades = []
        self.grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    def students(self):
        try:
            self.num_students = int(input("Enter the number of students: "))
            if self.num_students <= 0:
                raise ValueError("Number of students must be a positive integer.")
            return self.num_students
        except ValueError as e:
            print(e)
            return self.students()

    def question(self):
        num_students = self.students()
        
        for s in range(num_students):
            try:
                score = float(input("Enter the score (0-200): "))
                grade = self.score_to_grade(score)
                self.scores.append(score)
                self.grades.append(grade)
                self.grade_counts[grade] += 1
                #print(f"The grade for the score {score} is: {grade}") #To verify the grade for each score entered
            except ValueError as e:
                print(e)
    
    def score_to_grade(self, score):
            if score < 0 or score > 200:
                raise ValueError("Score must be between 0 and 200.")
            return self.calculate_grade(score)
    
    def calculate_grade(self, score):
        if score >= 190:
            return 'A'
        elif score >= 160:
            return 'B'
        elif score >= 130:
            return 'C'
        elif score >= 100:
            return 'D'
        else:
            return 'F'
                

if __name__ == "__main__":
    grade_system = GradeSystem()
    grade_system.question()
    
    print("\nGrade Distribution:")
    for grade, count in grade_system.grade_counts.items():
        print(f"{grade}: {count}")