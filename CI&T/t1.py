# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input
def say_hello(name):
    # You can print to STDOUT for debugging like you normally would:
    print(name)

    if (name == ''):
        msg= 'Hello there!'
    else:
        msg = "Hello, %s!" % name
    # but you need to return the value in order to complete the challenge 
    return (msg) # TODO: return correct value

print(say_hello("Emerson"))
print(say_hello(""))
