import turtle


# Simplified simulation of complex values (replace this section with actual complex function or data generation)
def fake_complex_function(y):
    real_part = y / max(1, abs(y))  # Simplified real part
    imag_part = y * 0.1  # Simplified imaginary part
    return real_part, imag_part


# Generate points along the critical line
real_part = 0.5  # Constant real part in this simplified version
start, stop, num = -30, 30, 1000
step = (stop - start) / (num - 1)
imaginary_parts = [start + step * i for i in range(num)]  # Using list comprehension instead of np.linspace

# Calculate fake complex function values instead of zeta function
complex_values = [fake_complex_function(y) for y in imaginary_parts]

# Extract real and imaginary parts
real_values = [z[0] for z in complex_values]
imaginary_values = [z[1] for z in complex_values]

# Set up Turtle
turtle.speed(0)
screen = turtle.Screen()
screen.setworldcoordinates(start, min(real_values + imaginary_values), stop, max(real_values + imaginary_values))

# Draw grid with numbers
turtle.penup()
turtle.goto(start, 0)
turtle.pendown()
turtle.goto(stop, 0)

# Add number labels on x-axis
for i in range(start, stop + 1, int((stop - start) / 10)):
    turtle.penup()
    turtle.goto(i, 0)
    turtle.pendown()
    turtle.write(str(i), align="center")

turtle.penup()
turtle.goto(0, min(real_values + imaginary_values))
turtle.pendown()
turtle.goto(0, max(real_values + imaginary_values))

# Calculate step value ensuring it's not zero
step_value = int((max(real_values + imaginary_values) - min(real_values + imaginary_values)) / 10)
if step_value == 0:
    step_value = 1  # Ensure step is at least 1 to avoid zero step error

# Add number labels on y-axis
for i in range(int(min(real_values + imaginary_values)), int(max(real_values + imaginary_values)) + 1, step_value):
    turtle.penup()
    turtle.goto(0, i)
    turtle.pendown()
    turtle.write(str(i), align="left")

# Draw real part
turtle.penup()
turtle.goto(imaginary_parts[0], real_values[0])
turtle.pendown()
turtle.color('blue')
for x, y in zip(imaginary_parts, real_values):
    turtle.goto(x, y)

# Draw imaginary part
turtle.penup()
turtle.goto(imaginary_parts[0], imaginary_values[0])
turtle.pendown()
turtle.color('red')
for x, y in zip(imaginary_parts, imaginary_values):
    turtle.goto(x, y)

# Finish
turtle.hideturtle()
turtle.done()