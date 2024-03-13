#alex feb 26

def say_hello():
    print("Hello")

def say_hello_params(name):
    print(f"Hello {name.capitalize()}!")
    
def how_big(num):
    if num < 0:
         return "Very small"
    if num < 10:
        return "Snall"
    if num < 100:
        return "Big"
    if num < 1000:
        return "Very Big"
    return "Giniminasouras"


# say_hello()
# say_hello_params("alex")
print(how_big(-1))
