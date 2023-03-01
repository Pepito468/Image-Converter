#Libs
import argparse
from PIL import Image

def convert_image_to_webp(input_file_path, output_file_path, output_format):
    # Open the input image using PIL
    with Image.open(input_file_path) as img:
        # Convert the image to RGBA mode if it's not already in that mode
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Save the image in the specified output format with a quality of 90
        img.save(output_file_path, output_format, quality=90)

if __name__ == "__main__":
    #Args
    par = argparse.ArgumentParser(description="Convert an input image to WebP or png format.")
    par.add_argument("input_file_path", help="path to the input image file")
    par.add_argument("-png", action="store_true", help="convert the output to PNG format")
#DOES NOT WORK    par.add_argument("-jpeg", action="store_true", help="convert the output to JPEG format")
    par.add_argument("-webp", action="store_true", help="convert the output to WebP format (default)")
    args = par.parse_args()

    #Outputs
    if args.png:
        output_format = "PNG"
#    elif args.jpeg:
#        output_format = "JPEG"
    else:
        output_format = "WEBP"

    output_file_path="NEW_"+str(args.input_file_path)

    #Function
    convert_image_to_webp(args.input_file_path, output_file_path, output_format)
