def greet(hello):
    def mfx(*args, **kwargs):
        print("hi karan..")
        hello(*args, **kwargs)
        print("thanks karan..")

    return mfx


@greet
def hello():
    print("Hello")

hello()