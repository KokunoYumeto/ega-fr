from PIL import Image, ImageDraw, ImageFont
import sys
fonts = [r"C:\Windows\Fonts\cambria.ttc", r"C:\Windows\Fonts\seguisym.ttf", r"C:\Windows\Fonts\STIXTwoMath-Regular.otf"]
chars = "\U0001D50E \u211C \U0001D50D \U0001D50F \U0001D510"
im = Image.new("L", (1400, 150*len(fonts)), 255)
d = ImageDraw.Draw(im)
for i, f in enumerate(fonts):
    try:
        ft = ImageFont.truetype(f, 110, index=1) if f.endswith('.ttc') else ImageFont.truetype(f, 110)
        d.text((10, 10+150*i), "K R J L M: " + chars, font=ft, fill=0)
    except Exception as e:
        d.text((10, 10+150*i), str(e), fill=0)
im.save("frak_ref.png")
