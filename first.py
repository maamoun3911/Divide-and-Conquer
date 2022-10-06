counters = {"target_Conter" : 0, "secondary_Counter" : 0}

numberStudying = lambda number: "even" if number %2 == 0 else "odd"

def Division(food:list):
    result = numberStudying(food[0])
    if result == "even":
        food = [int(food[0]/2), int(food[0]/2)] + food[1:]
    elif result == "odd":
        food = [int(food[0]/2), int(food[0]/2)+1] + food[1:]
    return food

def func(food:list, target:int):

    try:
        if food[0] == target:
            food = food[1:]
            counters["target_Conter"] += 1
            return func(food, target)
        elif food[0] != target and food[0] > target:
            Divide = Division(food)
            return func(Divide,target)
        elif food[0] != target and food[0] < target:
            food = food[1:]
            counters["secondary_Counter"] += 1
            return func(food, target)

    except IndexError:
        return counters

print(func([7, 6, 4, 9, 5, 11], 3))
