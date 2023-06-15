import turtle
import xml.etree.ElementTree as ET

def draw_svg(svg_file):
    # Create a turtle instance
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Set initial position and color
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(2)
    t.speed(3)

    # Iterate through SVG elements
    for element in root.iter():
        if element.tag == '{http://www.w3.org/2000/svg}path':
            # Handle path commands
            path_data = element.get('d')
            commands = parse_path_commands(path_data)

            for command in commands:
                if command[0] == 'M':
                    x, y = command[1:]
                    t.penup()
                    t.goto(x, -y)
                    t.pendown()
                elif command[0] == 'L':
                    x, y = command[1:]
                    t.goto(x, -y)

    # Close the turtle graphics
    screen.exitonclick()

def parse_path_commands(path_data):
    commands = []
    current_command = ''
    command_data = []

    for char in path_data:
        if char.isalpha():
            if current_command:
                commands.append((current_command, command_data))
                command_data = []
            current_command = char
        elif char.isdigit() or char in ('.'):
            command_data.append(float(char))

    if current_command:
        commands.append((current_command, command_data))

    return commands

# Usage
draw_svg('imagebyzaid.svg')
