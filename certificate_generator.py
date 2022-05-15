from PIL import ImageFont, ImageDraw, Image, ImageEnhance


def writeName(certificate_path, coordinates, name_path,target_folder,font_path = None):
    f = open(name_path,"r")
    names_list = f.read().split("\n")
    for name_to_print in names_list:
        image = Image.open(certificate_path)
        # image = ImageEnhance.Sharpness(image)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("BOOKOS.TTF", 35)
        draw.text((int(coordinates[0]), int(coordinates[1]-35)), name_to_print, font=font, fill='black')
        image.save(target_folder+"/"+name_to_print+".png")
