import json
with open('report.txt') as f:
    data = json.load(f)
print(data)

from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100,750,"Welcome to Reportlab!")
c.save()
