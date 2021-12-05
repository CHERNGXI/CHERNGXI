import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=500):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixels//80] for pixels in pixels])
    return(characters)

def main(new_width=500):
    path = input("Enter a valid pathname to an image:\n")
    image = PIL.Image.open(path)
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not valid pathname to an image.")

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)

    with open("ascii_image.txt", "w")as f:
        f.write(ascii_image)

    a_file = open("ascii_image.txt", "r")
    contents = str(a_file.read())
    unicode_text1 = u'\u2588'
    encoded_unicode1 = unicode_text1.encode("utf8")
    unicode_text2 = u'\u2593'
    encoded_unicode2 = unicode_text2.encode("utf8")
    unicode_text3 = u'\u2592'
    encoded_unicode3 = unicode_text3.encode("utf8")
    unicode_text4 = u'\u2591'
    encoded_unicode4 = unicode_text4.encode("utf8")
    b_file = open("final ascii.txt", "wb")
    pp = 1
    for i in range(1, len(str(contents))+1):
        if pp % 501 != 0 or pp == 0:
            if contents[i-1] == "@":         
                b_file.write(" "+ encoded_unicode1)
                pp += 1
            if contents[i-1] == "#":
                b_file.write(" "+ encoded_unicode2)
                pp += 1
            if contents[i-1] == "S":
                b_file.write(" "+ encoded_unicode3)
                pp += 1
            if contents[i-1] == "%":
                b_file.write(" "+ encoded_unicode4)
                pp += 1
            if contents[i-1] == "?":
                b_file.write(" "+ b'S')
                pp += 1
            if contents[i-1] == "*":
                b_file.write(" "+ b'=')
                pp += 1
            if contents[i-1] == "+":
                b_file.write(" "+ b'+')
                pp += 1
            if contents[i-1] == ";":
                b_file.write(" "+ b'|')
                pp += 1
            if contents[i-1] == ":":
                b_file.write(" "+ b':')
                pp += 1
            if contents[i-1] == ",":
                b_file.write(" "+ b'.')
                pp += 1
            if contents[i-1] == ".":
                b_file.write(" "+ b' ')
                pp += 1
                
        if pp % 501 == 0 and pp != 0:
            if contents[i-1] == "@":         
                b_file.write(" "+ encoded_unicode1)
                pp += 1
            if contents[i-1] == "#":
                b_file.write(" "+ encoded_unicode2)
                pp += 1
            if contents[i-1] == "S":
                b_file.write(" "+ encoded_unicode3)
                pp += 1
            if contents[i-1] == "%":
                b_file.write(" "+ encoded_unicode4)
                pp += 1
            if contents[i-1] == "?":
                b_file.write(" "+ b'S')
                pp += 1
            if contents[i-1] == "*":
                b_file.write(" "+ b'=')
                pp += 1
            if contents[i-1] == "+":
                b_file.write(" "+ b'+')
                pp += 1
            if contents[i-1] == ";":
                b_file.write(" "+ b'|')
                pp += 1
            if contents[i-1] == ":":
                b_file.write(" "+ b':')
                pp += 1
            if contents[i-1] == ",":
                b_file.write(" "+ b'.')
                pp += 1
            if contents[i-1] == ".":
                b_file.write(" "+ b' ')
                pp += 1
            b_file.write(b'\n')

            
##    a_file = open("out.txt", "wb")
##    a_file.write(encoded_unicode1)
##    a_file.write(encoded_unicode1)
##    a_file.write(encoded_unicode1)

main()






    
