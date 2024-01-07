from PIL import Image


def resize_image(input_path, output_path, new_width):
    original_image = Image.open(input_path)

    # Calculate the proportional height based on the new width
    ratio = new_width / original_image.width
    new_height = int(original_image.height * ratio)

    # Resize the image
    resized_image = original_image.resize((new_width, new_height))

    # Save the resized image
    resized_image.save(output_path)


resize_image("burger.jpg", "resized_burger.jpg", 800)
