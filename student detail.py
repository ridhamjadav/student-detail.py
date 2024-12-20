students = {}

def sort_key(student):
    return student[1]  

while True:
    print("\n1. Add\n2. Update\n3. Delete\n4. Results\n5. Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        student_id = input("ID: ")
        marks = {}
        num_subjects = int(input("Subjects: "))
        for _ in range(num_subjects):
            sub, mark = input("Subject, Marks: ").split()
            marks[sub] = int(mark)
        students[student_id] = marks

    elif choice == '2':
        student_id = input("ID: ")
        if student_id in students:
            num_subjects = int(input("Subjects to update: "))
            for _ in range(num_subjects):
                sub, mark = input("Subject, Marks: ").split()
                students[student_id][sub] = int(mark)

    elif choice == '3':
        student_id = input("ID: ")
        students.pop(student_id, None)

    elif choice == '4':
        results = []
        for student_id, marks in students.items():
            total = sum(marks.values())
            percentage = total / len(marks) if marks else 0
            results.append((student_id, total, percentage))
        
        results.sort(key=sort_key, reverse=True)  
        
        print(f"{'Rank':<5} {'ID':<10} {'Total':<10} {'Percentage':<10}")
       
        for rank, (student_id, total, percentage) in enumerate(results[:10], start=1):
            
            print(f"{rank:<5} {student_id:<10} {total:<10} {percentage:.2f}%")

    elif choice == '5':
        break