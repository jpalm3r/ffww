from PIL import Image
import os


def resize_image(input_path, output_path, width):
    """Resizes an image to the specified width while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        img_resized = img.resize((width, new_height), Image.Resampling.LANCZOS)
        img_resized.save(output_path)
        print(f"Image saved to {output_path}")


def batch_resize_images(input_folder, output_folder, width):
    """Resizes all .png and .jpg images in a folder while maintaining aspect ratio."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(("png", "jpg", "jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, width)


if __name__ == "__main__":
    input_folder = "./figures/paallmeerr/"
    output_folder = "./figures/web_images/"
    width = 600  # Change to desired width

    batch_resize_images(input_folder, output_folder, width)