# -*- coding: utf-8 -*-
"""
Created on Sat May 16 03:31:19 2015

@author: JZA
"""
#--------- To set up an enviornment before running this script
# 1. Install python-nvd3 : python3.4 -m pip install python-nvd3
# 2. Download node from the link (http://nodejs.org/)
# 3. Install npm and bower: sudo npm install -g bower
# 4. Install in the same directory where you will used python-nvd3
# 5. Install d3#3.3.8: bower install d3#3.3.8
# 6. Install nvd3#.1.12-beta: bower install nvd3#1.1.12-beta
#------------------------------------------------------------------------------------
 
from nvd3 import pieChart
from nvd3 import multiBarChart
import time
import datetime
 
output_file = open('Visual.html', 'w')      # Write html output file
 
#----------------------- Stacked Bar Chart of First MultiBarChart - Keywords in Job Title
 
# Title of Chart
type = "Hottest Key Words in Job Title"
# Use Multibar Chart to display in our HTML - Height, Width, Stacked, Formating X axis into date
chart = multiBarChart(name=type, height=400, width=1100, stacked= True, x_is_date=True, x_axis_format="%d-%b-%Y")
# Header insert in our HTML
chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
# Date - X axis
xdata= [1416027600001, 1416227600001, 1416427600001, 1416627600001, 1416727600001]
# Data - Y axis - Values
ydata1 = [0.19763513513513514, 0.1625, 0.1704225352112676, 0.20998719590268886, 0.16584158415841585]
# Transfer to [0, 100] percentage
ydata1 = [ydata1[i]*100 for i in range(5)]
ydata2 = [0.13429054054054054, 0.1375, 0.1323943661971831, 0.18053777208706787, 0.15594059405940594]
ydata2 = [ydata2[i]*100 for i in range(5)]
ydata3 = [0.11570945945945946, 0.1125, 0.11408450704225352, 0.10627400768245839, 0.1419141914191419]
ydata3 = [ydata3[i]*100 for i in range(5)]
ydata4 = [0.10557432432432433, 0.10000001, 0.09859154929577464, 0.09603072983354674, 0.12458745874587458]
ydata4 = [ ydata4[i]*100 for i in range(5) ]
ydata5 = [0.10050675675675676, 0.0875, 0.08873239436619719, 0.07810499359795134, 0.09735973597359736]
ydata5 = [ydata5[i]*100 for i in range(5)]
ydata6 = [0.0785472972972973, 0.0875, 0.08732394366197183, 0.07554417413572344, 0.07508250825082509]
ydata6 = [ydata6[i]*100 for i in range(5)]
ydata7 = [0.07263513513513513, 0.0875, 0.08450704225352113, 0.07042253521126761, 0.07260726072607261]
ydata7 = [ydata7[i]*100 for i in range(5)]
ydata8 = [0.07179054054054054, 0.075, 0.08028169014084507, 0.06914212548015365, 0.0594059405940594]
ydata8 = [ydata8[i]*100 for i in range(5)]
ydata9 = [0.06672297297297297, 0.075, 0.07464788732394366, 0.058898847631242, 0.05858085808580858]
ydata9 = [ydata9[i]*100 for i in range(5)]
ydata10 = [0.056587837837837836, 0.075, 0.06901408450704226, 0.05505761843790013, 0.04867986798679868]
ydata10 = [ydata10[i]*100 for i in range(5)]
 
# Inserting tooltips/ buttons
extra_serie = {"tooltip": {"y_start": "", "y_end": " percent"}}
chart.add_serie(name="Rank1",y=ydata1, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank2", y=ydata2, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank3", y=ydata3, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank4", y=ydata4, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank5", y=ydata5, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank6", y=ydata6, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank7", y=ydata7, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank8", y=ydata8, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank9", y=ydata9, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank10", y=ydata10, x=xdata, extra=extra_serie)
 
# Building HTML content only
chart.buildcontent()
# Building Charts in HTML
chart.buildhtml()
# Wrting the output file and Save it as a HTML file
output_file.write(chart.htmlcontent)
 
 
 
 
#---------------------- Stacked Bar Chart of Second MultiBar Chart  - Keywords in Job Title and Description
 
type = "Key Words in Job Title and Description"
 
chart = multiBarChart(name=type, height=400, width=1100, stacked= True, x_is_date=True, x_axis_format="%d-%b-%Y")
chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
output_file.write("<p>Title key word rank: <br> 1st: ['service', 'manage', 'manage', 'manage', 'demonstrate'],<br> 2nd: ['manage', 'sale', 'sale', 'sale', 'sale'] , <br>3rd: ['entry', 'part', 'account', 'nurse', 'product'], <br> 4th: ['custom', 'assist', 'nurse', 'assist', 'costco'], <br> 5th: ['sale', 'technician', 'service', 'retail', 'manage'], <br> 6th: ['member', 'engineer', 'engineer', 'engineer', 'retail'], <br> 7th: ['food', 'nurse', 'represent', 'analyst', 'consult'],<br> 8th: ['crew', 'time', 'specialist', 'account', 'entry'],<br> 9th: ['nurse', 'specialist', 'assist', 'driver', 'account'],<br> 10th: ['assist', 'automotatic', 'analyst', 'specialist', 'market'] </p>")
output_file.write("<p>From the above graph, we can see that the hottest jobs are: manager, salesman, assistant, nurse, engineer and analyst.</p>")
 
# Date - X axis
xdata= [1416027600001, 1416227600001, 1416427600001, 1416627600001, 1416727600001]
# Data - Y axis - Values
ydata1 = [0.17189962419687235, 0.17094017094017094, 0.13928293063133282, 0.1611441307578009, 0.14891686514687535]
# Transfer to [0, 100] percentage
ydata1 = [ydata1[i]*100 for i in range(5)]
ydata2 = [0.14480543096132864, 0.13597513597513597, 0.12182385035074045, 0.11136701337295692, 0.14704548032210502]
ydata2 = [ydata2[i]*100 for i in range(5)]
ydata3 = [0.11334707237240878, 0.108003108003108, 0.11402961808261886, 0.10586924219910847, 0.11937166836792559]
ydata3 = [ydata3[i]*100 for i in range(5)]
ydata4 = [0.10092132379682386, 0.09557109557109557, 0.09688230709275136, 0.10081723625557207, 0.10905069751616196]
ydata4 = [ydata4[i]*100 for i in range(5)]
ydata5 = [0.09219299309007152, 0.08780108780108781, 0.09586905689789556, 0.09301634472511144, 0.10116819779970511]
ydata5 = [ydata5[i]*100 for i in range(5)]
ydata6 = [0.07940356406837193, 0.08313908313908314, 0.09150428682774747, 0.0913075780089153, 0.07927866621299762]
ydata6 = [ydata6[i]*100 for i in range(5)]
ydata7 = [0.07819129591465632, 0.08158508158508158, 0.08862042088854248, 0.08789004457652302, 0.07786095043665646]
ydata7 = [ydata7[i]*100 for i in range(5)]
ydata8 = [0.07503939871499575, 0.08003108003108003, 0.08604832424006235, 0.0838038632986627, 0.07735057275717364]
ydata8 = [ydata8[i]*100 for i in range(5)]
ydata9 = [0.07352406352285125, 0.07925407925407925, 0.08316445830085736, 0.08306092124814264, 0.07394805489395485]
ydata9 = [ydata9[i]*100 for i in range(5)]
ydata10 = [0.07067523336161959, 0.0777000777000777, 0.08277474668745129, 0.08172362555720654, 0.06600884654644437]
ydata10 = [ydata10[i]*100 for i in range(5)]
 
# Inserting tooltips/ buttons
extra_serie = {"tooltip": {"y_start": "", "y_end": " percent"}}
chart.add_serie(name="Rank1",y=ydata1, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank2", y=ydata2, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank3", y=ydata3, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank4", y=ydata4, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank5", y=ydata5, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank6", y=ydata6, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank7", y=ydata7, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank8", y=ydata8, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank9", y=ydata9, x=xdata, extra=extra_serie)
chart.add_serie(name="Rank10", y=ydata10, x=xdata, extra=extra_serie)
 
 
chart.buildcontent() # Build HTML content only
output_file.write(chart.htmlcontent)
 
output_file.write("<p>All key word rank: <br>1st: ['service', 'manage', 'manage', 'manage', 'sale'], <br> 2nd: ['custom', 'work', 'work', 'work', 'custom'],<br>3rd: ['manage', 'service', 'service', 'service', 'product'], <br>4th: ['work', 'detail', 'custom', 'provide', 'service'], <br>5th: ['experiment', 'provide', 'experiment', 'response', 'work'],<br>6th: ['time', 'custom', 'require', 'custom', 'time'],<br>7th: ['sale', 'include', 'detail', 'sale', 'companies'],<br>8th: ['provid', 'require', 'provide', 'detail', 'manage'],<br>9th: ['require', 'companies', 'develop', 'develop', 'experiment'],<br>10th: ['detail', 'develop', 'response', 'experiment', 'detail']</p>")
output_file.write("<p>Interestingly the hightest appeared key words from Job titles and Job descriptions are slightly different, we can see that the hottest job key words are: management, work, customer, service, sales, experienced, provider.</p>")
 
 
# ----------------------------Title_11/15 Pie Chart
 
output_file.write('<h3>Closer look at Top 10 Key Words in Job Title</h3>')
output_file.write("<p>Following pie charts provides a closer look at Top 10 Key Words in Job Title</p>")
 
type = "Hottest Key Words in Job Title for 11/15"
chart = pieChart(name=type, color_category='category20c', height=350, width=1000)
#chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
#chart.add_chart_extras("\n\n<p>" + 'Here is the description.' + "<p>\n\n")
#chart.header_css = <link rel="stylesheet" href="styles.css">
extra_serie = {"tooltip": {"y_start": "", "y_end": " %"}}
xdata = ['service', 'manage', 'entry', 'custom', 'sale', 'member', 'food', 'crew', 'nurse', 'assist']
ydata = [0.19763513513513514, 0.13429054054054054, 0.11570945945945946, 0.10557432432432433, 0.10050675675675676, 0.0785472972972973, 0.07263513513513513, 0.07179054054054054, 0.06672297297297297, 0.056587837837837836]
ydata = [ydata[i]*100 for i in range(9)]
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
 
 
chart.buildcontent() # Build HTML content only
output_file.write(chart.htmlcontent)
 
#----------------------------- Title_11/17 Pie Chart
type = "Hottest Key Words in Job Title for 11/17"
chart = pieChart(name=type, color_category='category20c', height=350, width=1000)
#chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
extra_serie = {"tooltip": {"y_start": "", "y_end": " %"}}
xdata = ['manage', 'sale', 'part', 'assist', 'nurse', 'technician', 'engineer', 'specialist', 'time', 'automotatic']
ydata =[0.1625, 0.1375, 0.1125, 0.1, 0.0875, 0.0875, 0.0875, 0.075, 0.075, 0.075]
ydata = [ydata[i]*100 for i in range(9)]
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
 
 
chart.buildcontent() # Build HTML content only
output_file.write(chart.htmlcontent)
 
#----------------------------- Title_11/19 Pie Chart
type = "Hottest Key Words in Job Title for 11/19"
chart = pieChart(name=type, color_category='category20c', height=350, width=1000)
#chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
extra_serie = {"tooltip": {"y_start": "", "y_end": " %"}}
xdata = ['manage', 'sale', 'account', 'nurse', 'service', 'engineer', 'represent', 'specialist', 'assist', 'analyst']
ydata = [0.1704225352112676, 0.1323943661971831, 0.11408450704225352, 0.09859154929577464, 0.08873239436619719, 0.08732394366197183, 0.08450704225352113, 0.08028169014084507, 0.07464788732394366, 0.06901408450704226]
ydata = [ydata[i]*100 for i in range(9)]
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
#chart.margin({top: 30, right: 60, bottom: 20, left: 100});
 
chart.buildcontent() # Build HTML content only
output_file.write(chart.htmlcontent)
 
#----------------------------- Title_11/21 Pie Chart
type = "Top 10 Key Words in Job Title for 11/21"
chart = pieChart(name=type, color_category='category20c', height=350, width=1000)
#chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
extra_serie = {"tooltip": {"y_start": "", "y_end": " %"}}
xdata = ['manage', 'sale', 'nurse', 'assist', 'retail', 'engineer', 'analyst', 'account', 'driver', 'specialist']
ydata = [0.20998719590268886, 0.18053777208706787, 0.10627400768245839, 0.09603072983354674, 0.07810499359795134, 0.07554417413572344, 0.07042253521126761, 0.06914212548015365, 0.058898847631242, 0.05505761843790013]
ydata = [ydata[i]*100 for i in range(9)]
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
#chart.margin({top: 30, right: 60, bottom: 20, left: 100});
 
chart.buildcontent() # Build HTML content only
output_file.write(chart.htmlcontent)
 
#----------------------------- Title_11/23 Pie Chart
type = "Top 10 Key Words in Job Title for 11/23"
chart = pieChart(name=type, color_category='category20c', height=350, width=1000)
#chart.set_containerheader("\n\n<h3>" + type + "</h3>\n\n")
extra_serie = {"tooltip": {"y_start": "", "y_end": " %"}}
xdata = ['demonstrate', 'sale', 'product', 'costco', 'manage', 'retail', 'consult', 'entry', 'account', 'market']
ydata = [0.16584158415841585, 0.15594059405940594, 0.1419141914191419, 0.12458745874587458, 0.09735973597359736, 0.07508250825082509, 0.07260726072607261, 0.0594059405940594, 0.05858085808580858, 0.04867986798679868]
ydata = [ydata[i]*100 for i in range(9)]
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
#chart.margin({top: 30, right: 60, bottom: 20, left: 100});
 
 
chart.buildcontainer() # generate HTML div
chart.buildcontent()
 
output_file.write(chart.htmlcontent)
#print(chart.htmlcontent)
# close Html file
output_file.close()