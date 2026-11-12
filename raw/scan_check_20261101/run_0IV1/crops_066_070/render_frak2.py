from PIL import Image, ImageDraw, ImageFont
ft = ImageFont.truetype(r"C:\Windows\Fonts\cambria.ttc", 300, index=1)
im = Image.new("L", (1500, 420), 255)
d = ImageDraw.Draw(im)
d.text((20, 20), "\U0001D50E", font=ft, fill=0)
d.text((420, 20), "\u211C", font=ft, fill=0)
g = Image.open("p66_frakR_zoom.png").convert("L").resize((400,350))
im.paste(g, (850, 30))
im.save("frak_compare.png")
