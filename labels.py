import svgwrite
from svgwrite.text import TSpan
import csv

rows = 10
columns = 3
labelsize = { 'x': 2.5935, 'y': 1.0 }
leftMargin = 0.21975
rightMargin = 0.21975
topMargin = 0.5
bottomMargin = 0.5
horSpacing = 0.14
vertSpacing = 0.0

fontSize = 12
yTxtSpacing = fontSize

addresses = []

with open('Baby Shower Guest List.csv', 'r') as csvFile:
	addressList = csv.reader(csvFile,delimiter=",", quotechar='"')
	for address in addressList:
		addresses.append(address[:3])
		
print addresses

dwg = svgwrite.Drawing("labels.svg", ('8.5in','11in'), profile='tiny')
addressIndex = 0
for xRow in range(rows):
	for yCol in range(columns):
		xPos = leftMargin + (labelsize['x'] / 2 * (yCol + 1)) + (horSpacing * yCol)
		yPos = topMargin + (labelsize['y'] / 2 * (xRow + 1)) + (vertSpacing * xRow)
		txt = dwg.text(addresses[addressIndex][0], insert=(str(xPos) + 'in', str(yPos) + 'in'),fill='black', text_anchor="middle", font_size=fontSize)
		for i in range(2):
			txt.add(TSpan(addresses[addressIndex][i + 1],x=[str(xPos) + 'in'],dy=[yTxtSpacing]))
		txt.update({'text_anchor':"middle", 'x':str(xPos) + 'in', 'y':str(yPos) + 'in'})
		dwg.add(txt)
		addressIndex += 1
		print xPos, yPos
		
		
dwg.save()
