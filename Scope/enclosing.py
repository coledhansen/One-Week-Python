def outer():
    animal = 'Secretary Bird'
    def inner():
        print("INSIDE INNER FUNC: ", animal)
        def third():
            print("INSIDER THIRD NESTED FUNC: ", animal)
        third()
    inner()

outer()
