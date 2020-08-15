def num_key_strokes(text):
    return sum([1 if i in "abcdefghijklmnopqrestuvwxyz1234567890-=`];[',.\/ " else 2 for i in text]) 