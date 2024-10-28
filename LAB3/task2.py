def find_common_participants(first_sentence, second_sentence, splitter=','):
    return sorted(list(set(first_sentence.split(splitter)).intersection(second_sentence.split(splitter))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, splitter='|'))
