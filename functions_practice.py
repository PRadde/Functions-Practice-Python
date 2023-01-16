def hello():
    print("Ohh, Hello I didn't see you there.")

def pack(x,y,z):
    return [x,y,z]

def eat_lunch(lunch_food):
    if len(lunch_food) == 0:
        print("Mylunchbox is empty!")
    else:
        for i in range(len(lunch_food)):
            if i == 0:
                print(f"First I eat {lunch_food[0]}")
            else:
                print(f"Next I eat {lunch_food[i]}")

hello()
print(pack("apple","pickle","banana"))
eat_lunch([])
eat_lunch(["apple","pickle","peanutbutter","cheese"])