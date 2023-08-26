def josephus(num_soldiers, step):
    soldiers = list(range(1, num_soldiers + 1))
    killed_soldiers = []

    index = 0
    while len(soldiers) > 0:
        index = (index + step - 1) % len(soldiers)
        killed = soldiers.pop(index)
        killed_soldiers.append(killed)

    return killed_soldiers

num_soldiers = 41  
step = 3 

killed_soldiers = josephus(num_soldiers, step)
print("Soldiers killed in order:", killed_soldiers)
