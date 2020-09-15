a = "This website is for losers LOL!"
for i in a:
    if i in 'aeiouAEIOU':
        a=a.replace(i,'')
print(a)

#Alternative solution


# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")
