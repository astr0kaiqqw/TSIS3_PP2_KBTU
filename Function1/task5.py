def generate_permutations(string, current, result):
    if len(current) == len(string):
        result.append(current)
        return
    for i in range(len(string)):
        if string[i] not in current: 
            generate_permutations(string, current + string[i], result)

def print_permutations(string):
    result = []
    generate_permutations(string, "", result)
    for perm in result:
        print(perm)
user_input = input("Enter a string: ")
print("Permutations of the string:")
print_permutations(user_input)
