def intro(name):
    print(f'hello i am {name} welcome to the party')
    print("how are you")

intro("zaidi")
intro("murtaza")


def intro2(name,age,city):
    return f"hi my name is {name},and age is {age},and i live in {city}"

result = intro2('zaid',17,'KPK')
print(result)

def intro3(count):
    if (count == 2):
        return
    print(f"hi i am intro3 and my count is{count}")
    count = count +1
    intro3(count)

intro3(0)
    

