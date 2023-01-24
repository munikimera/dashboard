from flask import Flask,render_template,url_for,redirect,request
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.18;DATABASE=LOYALPAC_v7;UID=business;PWD=Sy$temB+;TrustServerCertificate=true')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT PAYROLLINFO.PRI_RES_D,COUNT(PAYROLLINFO.PRI_KEY), year(PAYROLLINFO.PRI_RES_D) AS yee,MONTH(PAYROLLINFO.PRI_RES_D) AS months FROM PAYROLLINFO WHERE PAYROLLINFO.PRI_STATUS = 2 and PAYROLLINFO.PRI_HIRE_TY = 1  GROUP BY PAYROLLINFO.PRI_RES_D  ORDER BY PAYROLLINFO.PRI_RES_D DESC")
    result = cursor.fetchall()
    print(result)
    

    jan = [number for number in result if number[3] == 1]
    totaljan = 0
    for i in jan:
        totaljan += i[1]
    print(totaljan)

    feb = [number for number in result if number[3] == 2]
    totalfeb = 0
    for i in feb:
        totalfeb += i[1]
    print(totalfeb)

    mar = [number for number in result if number[3] == 3]
    totalmar = 0
    for i in mar:
        totalmar += i[1]
    print(totalmar)

    apr = [number for number in result if number[3] == 4]
    totalapr = 0
    for i in apr:
        totalapr += i[1]
    print(totalapr)

    may = [number for number in result if number[3] == 5]
    totalmay = 0
    for i in may:
        totalmay += i[1]
    print(totalmay)

    jun = [number for number in result if number[3] == 6]
    totaljun = 0
    for i in jun:
        totaljun += i[1]
    print(totaljun)

    jul = [number for number in result if number[3] == 7]
    totaljul = 0
    for i in jul:
        totaljul += i[1]
    print(totaljul)

    aug = [number for number in result if number[3] == 8]
    totalaug = 0
    for i in aug:
        totalaug += i[1]
    print(totalaug)

    sept = [number for number in result if number[3] == 9]
    totalsept = 0
    for i in sept:
        totalsept += i[1]
    print(totalsept)

    oct = [number for number in result if number[3] == 10]
    totaloct = 0
    for i in oct:
        totaloct += i[1]
    print(totaloct)

    nov = [number for number in result if number[3] == 11]
    totalnov = 0
    for i in nov:
        totalnov += i[1]
    print(totalnov)

    dec = [number for number in result if number[3] == 12]
    totaldec = 0
    for i in dec:
        totaldec += i[1]
    print(totaldec)
    x =['jan', 'feb', 'mar', 'apr', 'may','jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    y =[]
    y.append(totaljan)
    y.append(totalfeb)
    y.append(totalmar)
    y.append(totalapr)
    y.append(totalmay)
    y.append(totaljun)
    y.append(totaljul)
    y.append(totalaug)
    y.append(totalsept)
    y.append(totaloct)
    y.append(totalnov)
    y.append(totaldec)
    print(len(y))
    print(len(x))
    c = sorted(y)
    print(c)

    df = pd.DataFrame({'Category': x,
                   'Values': y,
                   'Color': ['darkred', 'maroon', 'brown', 'firebrick', 'indianred','red', 'r', 'lightcoral', 'rosybrown', 'salmon', 'tomato', 'orangered']})
                   
    df = df.sort_values(by='Values', ascending=False)

    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Values'], color=df['Color'],
        width = 0.4)
    ax.set_yticks(y)
    for i, txt in enumerate(y):
        ax.text(x[i], y[i], txt)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    # plt.show()
    return render_template('index.html',plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)