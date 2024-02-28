class con:

    def __init__(self):
        print("constructor is called")
    def __del__(self):
        print("detsructor is called ")
c=con()
del c
        
