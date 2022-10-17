'''' online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online'''

def online_count(dictionary):
    count = 0
    for values in dictionary.values():
        if values == 'online':
            count +=1
    return count
statuses = {
    "Alice":"online",
    "Bob":"Offline",
    "Eve":"online",
}
obj = online_count(statuses)
print(obj)