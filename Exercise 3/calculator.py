import arithmetic

while True:

    user_nums = raw_input("> ").split(" ")

    if user_nums[0] == "q":
        quit()

    elif len(user_nums) == 3:
        num1 = int(user_nums[1])
        num2 = int(user_nums[2])

        if user_nums[0] == "+":
            print arithmetic.add(num1, num2)

        elif user_nums[0] == "-":
            print arithmetic.subtract(num1, num2)

        elif user_nums[0] == "*":
            print arithmetic.multiply(num1, num2)

        elif user_nums[0] == "pow":
            print arithmetic.power(num1, num2)

        elif user_nums[0] == "mod":
            print arithmetic.mod(num1, num2)
            
        elif user_nums[0] == "/":
            num1 = float(user_nums[1])
            num2 = float(user_nums[2])
            print arithmetic.divide(num1, num2)

    elif len(user_nums) == 2:
        num1 = int(user_nums[1])

        if user_nums[0] == "square":
            print arithmetic.square(num1)

        elif user_nums[0] == "cube":
            print arithmetic.cube(num1)

    else:
        print "Uh oh!"

