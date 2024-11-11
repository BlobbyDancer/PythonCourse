# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, divider=','):
    participants_1 = group1.split(divider)
    participants_2 = group2.split(divider)
    matching_participants = set(participants_1) & set(participants_2)
    sorted_matching_participants = sorted(matching_participants)
    return sorted_matching_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, divider=';')
print(result)