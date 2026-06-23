import sys
from PIL import Image, ImageOps


def main():
    validate_arguments()

    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    size = shirt.size

    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])


def validate_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_extensions = [".jpg", ".jpeg", ".png"]

    input_file = sys.argv[1].lower()
    output_file = sys.argv[2].lower()

    if not input_file.endswith(tuple(valid_extensions)):
        sys.exit("Invalid input")

    if not output_file.endswith(tuple(valid_extensions)):
        sys.exit("Invalid output")

    if input_file.split(".")[-1] != output_file.split(".")[-1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()