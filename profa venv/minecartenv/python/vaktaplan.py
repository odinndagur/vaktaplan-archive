import numpy as np
import pandas as pd
import minecart

file = "../input/11okt10nov.pdf"
# file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'


colors = set()
with open(file,"rb") as doc:
    document = minecart.Document(doc)
    print(document)
    page = document.get_page(0)
    for shape in page.shapes:
        if shape.fill:
            colors.add(shape.fill.color.as_rgb())
for color in colors: 
    print(color)