import numpy as np

math_scores = np.array([78, 85, 96, 70, 88])
science_scores = np.array([82, 79, 91, 68, 85])
english_scores = np.array([75, 80, 89, 72, 84])

student_scores = np.column_stack((math_scores, science_scores, english_scores))
print("Student Scores (Rows=Students, Cols=Subjects):\n", student_scores)

flattened = student_scores.flatten()
print("\nFlattened Scores:\n", flattened)

mean_scores = np.mean(student_scores, axis=0)
max_scores = np.max(student_scores, axis=0)
min_scores = np.min(student_scores, axis=0)
std_scores = np.std(student_scores, axis=0)

print("\nMean per subject:", mean_scores)
print("Max per subject:", max_scores)
print("Min per subject:", min_scores)
print("Std Dev per subject:", std_scores)

transposed_scores = student_scores.T
print("\nTransposed Scores:\n", transposed_scores)

first_group, second_group = np.vsplit(student_scores, [3])
print("\nFirst 3 Students:\n", first_group)
print("Last 2 Students:\n", second_group)

math, science, english = np.hsplit(student_scores, 3)
print("\nMath Column:\n", math)
print("Science Column:\n", science)
print("English Column:\n", english)

np.save('student_scores.npy', student_scores)
np.savetxt('student_scores.txt', student_scores, fmt='%d', delimiter=',')

loaded_npy = np.load('student_scores.npy')
loaded_txt = np.loadtxt('student_scores.txt', delimiter=',')

print("\nLoaded from .npy:\n", loaded_npy)
print("\nLoaded from .txt:\n", loaded_txt)

computer_scores = np.array([85, 87, 90, 78, 92])
student_scores_extended = np.column_stack((student_scores, computer_scores))
print("\nExtended Scores with Computer Subject:\n", student_scores_extended)

student_averages = np.mean(student_scores_extended, axis=1)
print("\nStudent Averages:", student_averages)

np.savetxt('averages.txt', student_averages, fmt='%.2f')

print("\nProject Complete: Arrays created, processed, saved, loaded, and extended!")
