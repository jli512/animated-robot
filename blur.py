from PIL import Image, ImageFilter

before = Image.open("jiahao.jpg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")