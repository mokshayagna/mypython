word1 = "abc"
word2 = "pqrst"
result = []
word2_index = 0
for char in word1:
    result.append(char)
    if word2_index < len(word2):
        result.append(word2[word2_index])
        word2_index = word2_index + 1
if word2_index < len(word2):
    result.extend(word2[word2_index:])

final_result = ''.join(result)

seperated_words = ' '.join(final_result)
print(seperated_words)
  
  # a p b q c r s t