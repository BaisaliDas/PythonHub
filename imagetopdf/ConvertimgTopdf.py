import img2pdf

pdfdata=img2pdf.convert(["kolkata.jpg","coffee.jpg"])
file=open("myreport_1.pdf","wb")
file.write(pdfdata)
file.close()
print("Coverted")

