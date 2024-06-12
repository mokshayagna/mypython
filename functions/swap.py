old_string = "Hi, Welcome. Altran is in Bengaluru, Hyderabad, and in Mumbai."
if "#$#" not in old_string:
    support_string = old_string.replace(',','#$#')
    temp_string = support_string.replace('.',',')
    new_string = temp_string.replace('#$#','.')
print(new_string)


def main():
    old_string = "Hi, Welcome. Altran is in Bengaluru, Hyderabad, and in Mumbai."
if "#$#" not in old_string:
    