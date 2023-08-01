#21 last

def print_pattern(height):
    for i in range(height):
        for j in range(height * 2 - 1):
            if j >= height - i - 0 and j < height + i:
                print("_", end="")
            else:
                print("*", end="")
        print()


# Example usage
pattern_height = 9
print_pattern(pattern_height)
