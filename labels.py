import svgwrite
from svgwrite.text import TextArea
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

addresses = []

with open('Baby Shower Guest List.csv', 'r') as csvFile:
	addressList = csv.reader(csvFile,delimiter=",", quotechar='"')
	for address in addressList:
		addresses.append("\n".join(address[:3]))
		
print addresses

dwg = svgwrite.Drawing("labels.svg", ('8.5in','11in'), profile='tiny')
addressIndex = 0
for xRow in range(rows):
	for yCol in range(columns):
		xPos = leftMargin + (labelsize['x'] / 2 * (yCol + 1)) + (horSpacing * yCol)
		yPos = topMargin + (labelsize['y'] / 2 * (xRow + 1)) + (vertSpacing * xRow)
		txtArea = TextArea(addresses[addressIndex],insert=(str(xPos) + 'in', str(yPos) + 'in'), fill='black', text_anchor="middle", profile="tiny")
		dwg.add(txtArea)
		addressIndex += 1
		print xPos, yPos
		
		
dwg.save()
