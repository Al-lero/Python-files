scores_list = []
start_student = 0
start_course = 0

number_of_student = int(input("Enter number of student: "))

courses_number = int(input("Enter number of courses: "))

for i in range(start_student, number_of_student):
	scores_list = []
	for j in range(start_course, courses_number):
		scores = int(input("Enter scores for student" + str(start_student+1) + "  " + "course" + str(start_course+1) + " : "))
		start_course += 1
		if (scores >= 0 and scores <= 100):
			scores_list.append(j)
start_student += 1
	

		  