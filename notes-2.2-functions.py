#alex
#apr 3

#greeting = "hello"
#print(greeting * 10)

##print("the quick brown fox jumps over the lazy dog" * 3)

def stars(star):
    if star < 0:
        return "I can't do that"
    else:
        return "*" * star

print(stars(20))