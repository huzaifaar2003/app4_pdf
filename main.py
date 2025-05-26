import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation='P', unit= "mm", format = "A4")
df = pd.read_csv("topics.csv")
topics = []
pages = []

for index, row in df.iterrows():
    pages.append(row["Pages"])
    topics.append(row["Topic"])

    for i in range (0,row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="b", size=24)
        pdf.cell(w=0, h=24, txt=row["Topic"], ln=1, border=0, align="L")
        pdf.line(10, 34, 200, 34)#(x1,y1,x2,y2) starting x,y then ending x,y

pdf.output("output.pdf") #this would be the name of the output pdf.

