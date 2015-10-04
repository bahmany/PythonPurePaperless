#!d:/Python27/python.exe -u
# -*- coding: UTF-8 -*-



import cStringIO
import xhtml2pdf.pisa as pisa
import os

# Shortcut for dumping all logs on screen
pisa.showLogging()

def HTML2PDF(data, filename, open=False):

    """
    Simple test showing how to create a PDF file from
    PML Source String. Also shows errors and tries to start
    the resulting PDF
    """

    pdf = pisa.CreatePDF(
        cStringIO.StringIO(data),
        file(filename, "wb"),encoding= 'utf-8')

    if open and (not pdf.err):
        os.startfile(str(filename))

    return not pdf.err

if __name__=="__main__":
    HTMLTEST = """
    <html>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
    <body>
    <p>Hello <strong style="color: #f00;">World</strong>
    <hr>
    <table border="1" style="background: #eee; padding: 0.5em;">
        <tr>
            <td>Amount</td>
            <td>سلام سلام</td>
            <td>Total</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Good weather</td>
            <td>0 EUR</td>
        </tr>
        <tr style="font-weight: bold">
            <td colspan="2" align="right">Sum</td>
            <td>0 EUR</td>
        </tr>
    </table>
    </body></html>
    """

    HTML2PDF(HTMLTEST, "test.pdf", open=True)