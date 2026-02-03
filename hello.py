print("Hello Python from Visual Studio!")
s = "*"*30
print(s)
print("New project")
print(s)
def generate_squares(n):
    """Generate list of squares using list comprehension"""
    return [x ** 2 for x in range(n)]

def generate_squares(n):
    """Generate list of squares using for loop"""
    result = []
    for x in range(n):
        result.append(x ** 2)
    return result

if __name__ == "__main__":
    print("For loop version:")
    print(f"generate_squares(5) = {generate_squares(5)}")