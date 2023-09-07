import os
from PIL import Image

def enlarge_images_in_folder(input_folder, output_folder, factor):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                image = Image.open(input_path)
                new_width = int(image.width * factor)
                new_height = int(image.height * factor)
                resized_image = image.resize((new_width, new_height), Image.BICUBIC)
                resized_image.save(output_path)

                print(f"Enlarged and saved: {output_path}")

def main():
    input_folder = input("Enter the path of the folder: ")
    output_folder = input("Enter the path of the folder where you need to download the enlarged files: ")

    enlargement_factor = input("Enter the enlargement factor (ex: 2.0, 3.0, 4.0): ")
    enlargement_factor = float(enlargement_factor)

    enlarge_images_in_folder(input_folder, output_folder, enlargement_factor)

if __name__ == "__main__":
    main()
