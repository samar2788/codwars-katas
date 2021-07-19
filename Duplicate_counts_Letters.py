def duplicate_count(text):
    l = []
    if text == "":
        return 0
    else:
        text = text.lower()
        d = {}
        for i in range(len(text)):
            if text[i] in d.keys():
                d[text[i]] += 1
            else:
                d[text[i]] = 1
        for k, v in d.items():
            if v > 1:
                l.append(k)
        return len(l)


# print(duplicate_count(""), 0)
# print(duplicate_count("abcde"), 0)
# print(duplicate_count("abcdeaa"), 1)
#print(duplicate_count("abcdeaB"), 2)
#print(duplicate_count("Indivisibilities"), 2)
