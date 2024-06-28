original_string = "       Altran    is        a         Great     place    to   work                        "
strip_remove = original_string.strip()
#print(strip_remove)
split_string = strip_remove.split()
#print(split_string)
rectified_string = ' '.join(split_string)
print(rectified_string)