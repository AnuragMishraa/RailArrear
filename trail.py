import csv
from fpdf import FPDF

datacsv=open("C:\Users\Anurag Mishra\Downloads\DATA1.csv")
data=csv.reader(datacsv)
pfno=input("Enter your PF NUMBER:")
for row in data:
    if row[1]==pfno:
        a=row
        break
        
header="NAME: "+str(a[2])+" | Designation: "+str(a[3])+" | Employee No.: "+str(a[1])+" | Bill Unit No.: "+str(a[0])

desg=a[3]
datacsv.close()

    

ratecsv=open("C:\Users\Anurag Mishra\Downloads\RATE.csv")
rate=csv.reader(ratecsv)
for i in rate:
    if i[0]==desg:
        b=i
        break

    
#report=open("C:\Users\ASHISH\Desktop\REPORT.csv",'w')
#writer=csv.writer(report)
#writer.writerow(header)
#writer.writerow(["F.Y.2017-2018"])
#writer.writerow(["Sl No.","MONTH","KM","KMA as per old rate","Exmption u/s 10(14)","Taxable Income","KMA as per new rate","Exption u/s 10(14)","Taxable Income","Arrear of KMA","Exption u/s 10(14)","Taxable Income"])
#writer.writerow(['a','b','c','d','e','f(d-e)','g','h','i(g-h)','j(g-d)','k(h-e)','l(i-f)'])

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",'BU',8)

pdf.cell(190,10,txt=header,ln=0.5,align='C')
pdf.cell(190,10,txt="F.Y.2017-2018",ln=0.5,align='C')

epw = pdf.w - 2*pdf.l_margin
pdf.set_font("Arial",'',8)
th = pdf.font_size
pdf.ln(0.5)



L1=["Sl","MONTH","KM","KMA as per","Exmption","Taxable","KMA as per","Exption","Taxable","Arrear of","Exption","Taxable"]
L2=["No.","","","old rate","u/s 10(14)","Income","new rate","u/s 10(14)","Income","KMA","u/s10(14)","Income"]
L3=['a','b','c','d','e','f(d-e)','g','h','i(g-h)','j(g-d)','k(h-e)','l(i-f)']


pdf.set_font("Arial",'B',8)
for i in L1:
    if i==L1[0]:
        pdf.cell(7,4*th,str(i),border=1,align='C')
        
    else:
        pdf.cell(16,4*th,str(i),border=1,align='C')
    

pdf.ln(2*th)

for i in L2:
    if i==L2[0]:
        pdf.cell(7,2*th,str(i),border=0,align='C')
        
    else:
        pdf.cell(16,2*th,str(i),border=0,align='C')
    
pdf.ln(2*th)

for i in L3:
    if i==L3[0]:
        pdf.cell(7,2*th,str(i),border=1,align='C')
    else:
        pdf.cell(16,2*th,str(i),border=1,align='C')
    
pdf.ln(2*th)

pdf.set_font("Arial",'',8)

datacsv=open("C:\Users\Anurag Mishra\Downloads\DATA1.csv")
data=csv.reader(datacsv)

count=0

totalj=0.0
totalk=0.0
totall=0.0


for row in data:
    if row[1]==pfno:
        month=row[4]
        c=(round(int(row[6])/float(b[3])))
        c=float(c)
        d=c*float(b[2])
        if d*0.7>=10000:
            e=10000
        else:
            e=round(d*0.7)
        f=d-e
        g=c*float(b[1])
        if g>=14300:
            h=10000
        else:
            h=round(g*0.7)
        i=g-h
        j=row[6]
        totalj=float(totalj)+float(j)
        k=h-e
        totalk=float(totalk)+float(k)
        l=i-f
        totall=float(totall)+float(l)
        count+=1
        main=[str(count),str(month),str(int(round(c))),str(int(round(d))),str(int(round(e))),str(int(round(f))),str(int(round(g))),str(int(round(h))),str(int(round(i))),str(int(j)),str(int(k)),str(int(round(l)))]

        for i in main:
            if i==main[0]:
                pdf.cell(7,2*th,str(i),border=1,align='C')
            else:
                pdf.cell(16,2*th,str(i),border=1,align='C')
        pdf.ln(2*th)
    
        if month=="201803":
            totalj1=totalj
            totalk1=totalk
            totall1=totall
            pdf.set_font("Arial",'BU',8)
            pdf.cell(190,6,txt="TOTAL:"+"          "+str(int(round(totalj1)))+"          "+str(int(round(totalk1)))+"            "+str(int(round(totall1)))+"            ",ln=0.5,align='R')
            
            pdf.cell(190,10,txt="F.Y.2018-2019",ln=0.5,align='C')
            pdf.set_font("Arial",'',8)
            
            totalj=0.0
            totalk=0.0
            totall=0.0
        if month=="201903":
            totalj2=totalj
            totalk2=totalk
            totall2=totall
            pdf.set_font("Arial",'BU',8)
            pdf.cell(190,6,txt="TOTAL:"+"      "+str(int(round(totalj2)))+"          "+str(int(round(totalk2)))+"           "+str(int(round(totall2)))+"             ",ln=0.5,align='R')
        
            pdf.cell(190,10,txt="F.Y.2019-2020",ln=0.5,align='C')
            pdf.set_font("Arial",'',8)
            
            totalj=0.0
            totalk=0.0
            totall=0.0
        
totalj3=totalj1+totalj2+totalj
totalk3=totalk+totalk2+totalk1
totall3=totall+totall1+totall2

pdf.set_font("Arial",'BU',8)
pdf.cell(190,6,txt="TOTAL:"+"        "+str(int(round(totalj)))+"            "+str(int(round(totalk)))+"            "+str(int(round(totall)))+"              ",ln=1,align='R')

pdf.set_font("Arial",'B',8)
#pdf.set_font("Arial",'',8)

pdf.ln(2*th)


#last=["F.Y.","ARREARS KMA PAID","EXCEMPTION","TAXABLE ARREARS"],["2017-2018",int(round(totalj1)),int(round(totalk1)),int(round(totall1))],["2018-2019",int(round(totalj2)),int(round(totalk2)),int(round(totall2))],["2019-2020",int(round(totalj)),int(round(totalk)),int(round(totall))],["GRAND TOTAL",int(round(totalj3)),int(round(totalk3)),int(round(totall3))]

last1=["F.Y.","ARREARS KMA PAID","EXCEMPTION","TAXABLE ARREARS"]
last2=["2017-2018",int(round(totalj1)),int(round(totalk1)),int(round(totall1))]
last3=["2018-2019",int(round(totalj2)),int(round(totalk2)),int(round(totall2))]
last4=["2019-2020",int(round(totalj)),int(round(totalk)),int(round(totall))]
last5=["GRAND TOTAL",int(round(totalj3)),int(round(totalk3)),int(round(totall3))]



for i in last1:
    pdf.set_font("Arial",'B',8)
    if i==last1[0]:
        pdf.cell(epw/5,2*th,txt=str(i),border=1,align='C')
    else:
        pdf.cell(epw/4,2*th,txt=str(i),border=1,align='C')
pdf.ln(2*th)

for i in last2:
    pdf.set_font("Arial",'',8)
    if i==last2[0]:
        pdf.cell(epw/5,2*th,txt=str(i),border=1,align='C')
    else:
        pdf.cell(epw/4,2*th,txt=str(i),border=1,align='C')
pdf.ln(2*th)

for i in last3:
    pdf.set_font("Arial",'',8)
    if i==last3[0]:
        pdf.cell(epw/5,2*th,txt=str(i),border=1,align='C')
    else:
        pdf.cell(epw/4,2*th,txt=str(i),border=1,align='C')
pdf.ln(2*th)

for i in last4:
    pdf.set_font("Arial",'',8)
    if i==last4[0]:
        pdf.cell(epw/5,2*th,txt=str(i),border=1,align='C')
    else:
        pdf.cell(epw/4,2*th,txt=str(i),border=1,align='C')
pdf.ln(2*th)

for i in last5:
    pdf.set_font("Arial",'BU',8)
    if i==last5[0]:
        pdf.cell(epw/5,2*th,txt=str(i),border=0,align='C')
    else:
        pdf.cell(epw/4,2*th,txt=str(i),border=0,align='C')
pdf.ln(2*th)



pdf.output(str(a[2])+".pdf")


print("YOUR REPORT HAS BEEN GENERATED SUCESSFULLY, GO CHECK!!")
print("THANKYOU FOR USING MY PROGRAM!!")
print("DEVELOPED BY SERMC.")


