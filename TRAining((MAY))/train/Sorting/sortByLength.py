def sort_words_by_length(s: str) -> str:
    words = []
    word = ""
    for ch in s:
        if ch == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += ch
    if word:
        words.append(word)

    length_map = {}
    lengths = []

    for word in words:
        l = 0
        for _ in word:
            l += 1
        if l not in length_map:
            length_map[l] = []
            lengths.append(l)
        length_map[l].append(word)

    for i in range(1, len(lengths)):
        key = lengths[i]
        j = i - 1
        while j >= 0 and lengths[j] > key:
            lengths[j + 1] = lengths[j]
            j -= 1
        lengths[j + 1] = key

    result = []
    for l in lengths:
        result.extend(length_map[l])

    final_str = ""
    for i in range(len(result)):
        final_str += result[i]
        if i != len(result) - 1:
            final_str += " "

    return final_str


print(sort_words_by_length("an apple a day keeps the doctor away"))