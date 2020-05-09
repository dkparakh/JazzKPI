#!/usr/bin/python
from dkplib import *

url_xml_2DB_main("D:/WebSite/JazzKPI/reportinputs.xml")
print("Content-type: text/html\n")
print("""
<html>
<body style="margin:5px 0px 0px 5px">
    <div style="font-size:18pt; font-family:verdana; font-weight:bold; text-align:center">
        Jazz KPI 
    </div>
    <hr style="border:solid 1px #000080;margin:5px 5px 0px 5px" />
    <div style="font-size:10pt; font-family:verdana; font-weight:bold;margin:5px 0px 0px 50px">
        <br>
            <a href="http://localhost/JazzKPI/HOD.html">HOD KPI</a>
        <br>
        <br>
            <a href="http://localhost/">SI Line KPI</a>
        <br>
        <br>
            <a href="http://localhost/">UI Line KPI</a>
        <br>
        <br>
            <a href="http://localhost/">QC Line KPI</a>
        <br>
        <br>
            <a href="http://localhost/">RM KPI</a>
        <br>
        <br>
    </div>
</body>
</html>
""")
