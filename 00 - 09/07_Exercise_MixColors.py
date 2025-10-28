# User Input
color1 = input('Enter First Color (red, blue, yellow): ').lower()
color2 = input('Enter Second Color (red, blue, yellow): ').lower()
colors = [color1, color2]

print('-'*50)
print(f"Let's mix {color1} + {color2}")

# Calculate New Color
if color1 == color2:
    print("You are mixing the same color!")
    print(f'{color1} + {color2} = {color1}')

elif 'red' in colors and 'blue' in colors:
    print(f'{color1} + {color2} = Purple')

elif 'red' in colors and 'yellow' in colors:
    print(f'{color1} + {color2} = Orange')

elif 'blue' in colors and 'yellow' in colors:
    print(f'{color1} + {color2} = Green')