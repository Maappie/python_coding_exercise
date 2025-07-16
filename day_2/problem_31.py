# Create a hash of hashes to represent two different students and their grades in Math and English. Print the English grade of the second student

def create_hash_of_hashes():
    students = dict(
        student_1 = dict(Math = 90, English = 85),
        student_2 = dict(Math = 80, English = 95)
    )
    return students

students = create_hash_of_hashes()

print(f"Grade in english: {students["student_2"]["English"]}")   

