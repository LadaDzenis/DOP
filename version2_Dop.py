student1 = input("Доброго времени суток! "
                "Назовите имя студента. ")
input_mark1 = input("Введите оценки через запятую: ")
mark1_list = input_mark1.split(',')
mark1 = [int(mark1.strip()) for mark1 in mark1_list]
total_sum = sum(mark1)
total_count = len(mark1)
average_mark1 = total_sum/total_count
average_score = {}
average_score[student1] = average_mark1
# print(average_score)

student2 = input("Назовите имя второго студента. ")
input_mark2 = input("Введите оценки через запятую: ")
mark2_list = input_mark2.split(',')
mark2 = [int(mark2.strip()) for mark2 in mark2_list]
total_sum = sum(mark2)
total_count = len(mark2)
average_mark2 = total_sum/total_count
average_score[student2] = average_mark2

student3 = input("Назовите имя следующего студента. ")
input_mark3 = input("Введите оценки через запятую: ")
mark3_list = input_mark3.split(',')
mark3 = [int(mark3.strip()) for mark3 in mark3_list]
total_sum = sum(mark3)
total_count = len(mark3)
average_mark3 = total_sum/total_count
average_score[student3] = average_mark3

student4 = input("Назовите имя следующего студента. ")
input_mark4 = input("Введите оценки через запятую: ")
mark4_list = input_mark4.split(',')
mark4 = [int(mark4.strip()) for mark4 in mark4_list]
total_sum = sum(mark4)
total_count = len(mark4)
average_mark4 = total_sum/total_count
average_score[student4] = average_mark4

student5 = input("Назовите имя заключительного студента. ")
input_mark5 = input("Введите оценки через запятую: ")
mark5_list = input_mark5.split(',')
mark5 = [int(mark5.strip()) for mark5 in mark5_list]
total_sum = sum(mark5)
total_count = len(mark5)
average_mark5 = total_sum/total_count
average_score[student5] = average_mark5

print(average_score)

