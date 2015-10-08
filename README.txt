#######################################################
Objectives of our project
######################################################

Job searching is a painful process for every graduate. 
For one, there is a vast pool of career information. 
Also, as a freshman in a job market, graduates run around like headless chickens. 
In this regard, a career information aggregator, which can show them a big picture of the job market, is of crucial importance. 
In a rapidly changing job market, it is beneficial to have daily and even real-time information with regard to job openings. 
Our project is to serve this need by writing several python scripts to extract most recent job information from CareerBuilder.com, 
and automatically generate a general overview or trend report for job searchers.


#######################################################
The structure of code
#######################################################

There are three parts of code in our project. They are datacollection, analysis and visualization parts.

In our datacollection part, scripts are used to download and collect data from webside, i.e. careerbuilder.com
The 'extractiondata.py' file is used to download xml format files from webside and store them in the data directory.
The 'datac.py' file is used to parsing every html file that is found in the xml files and collect data using for analysis.

In our analysis part, scripts are used to analysis data we collect.
The 'xmlwords.py' is a file that contains one class that we develop to analysis the data.
The 'main.py' is a file that used to generate analysis outcomes using the class in 'xmlwords.py'

In our visualization part, the script is used to generate interactive charts and graphs that visualize the result of our analysis.


#########################################################
How to run this project
########################################################
The modules need to be install: BeautifulSoup, node, nvd3.
the command line statements are listed below:
#install node and nvd3.
$ python3.4 -m pip install python-nvd3
$ download node from the link (http://nodejs.org/)
$ sudo npm install -g bower
$ install in the same directory where you will used python-nvd3
$ bower install d3#3.3.8
$ bower install nvd3#1.1.12-beta

#install beautifulsoup module
$ pip install beautifulsoup4
$ 2to3-3.2 -w bs4

After installing these required modules, the first step is to run the datac.py and extractdata.py files in datacollection directory.
Doing so will download data and naming automatically according to the time.
The second step is to run main.py in analysis directory.
Doing so will generate outcomes of analysing the data.
The third step is to run finalpart3.py in visualization directory.
Doing so will generate graphs and charts and combine them in a single html file that can be found in the root directory of our project.
