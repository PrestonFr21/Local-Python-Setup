def greeting():
    print("Wassup Everyone")

def pack(food, drinks, clothes):
    return [food, drinks, clothes]

def eat_lunch(my_list):
    if len == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I'll eat my {my_list[0]}")
            else:
                print(f"Next I'll eat my {my_list[i]}")


greeting()
print(pack("food","drinks", "clothes"))
eat_lunch([])
eat_lunch(["apple", "bagel", "yogurt"])