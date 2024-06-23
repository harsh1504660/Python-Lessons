

def greet(fx):
    def mfx():
        print("good morning ")
        fx()
        print("hanks")
    return mfx
@greet
def hello():
    print("hello world")





hello()
