from PIL import Image, ImageDraw

# Specify the size and color of the image
image_size = (500, 500)
bg_color = (0, 0, 0)  # Black

# Create a new image with the specified size and color
image = Image.new("RGB", image_size, bg_color)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Specify the starting and ending points of the line
start_point = (10, 10)
end_point = (20, 555)

# Specify the color and thickness of the line
line_color = (255, 255, 255)  # White
line_thickness = 3

# Draw the line on the image
draw.line((start_point, end_point), fill=line_color, width=line_thickness)

# Specify the path to save the image
image_path = "./line_of_result.png"  # Replace with your desired path and filename

# Save the image to the specified path
image.save(image_path)

print(f"Image saved to: {image_path}")

# Show the image
image.show()