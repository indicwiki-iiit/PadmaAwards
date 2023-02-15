# padmaAwards
indicWiki Project 


## src - Working directory 

This is the primary directory while working on data 

#### Files

* Scraping 
    - Jupyter Notebooks with Prefix as Scrape_<Version_Number>_<description>.ipynb

* Cleaning - Analysing
    - Jupyter Notebooks with Prefix as Clean_<Version_Number>_<description>.ipynb
  
* Jinja Templating
    - Jupyter Notebooks with Prefix as Jinja_<Version_Number>_<description>.ipynb
  
* XML Generation
    - Jupyter Notebooks with Prefix as XMLGen_<Version_Number>_<description>.ipynb

the .xml files are the final output files 
- Awards_0-4.xml => xml for first 5 (i.e, 0,1,2,3,4 ) 
- Awards.xml => xml for entire dataset of 4420 entries


#### Folders


* renders
    - collection data in versions using online resources or personal computers with versions and prefixes accordingly

* output
    - Backed up files while manual cleaning
 
* renders
    - final dataset after all cleaning 
    - the latest version (v6) is the most reliable dataset after going through prev versions and thus those many cleanings

* Template 
    - jinja Templates for generating xml

  
## Generate_XML - Result of Project on Domain 

This directory contains the final minimal set of files to generate XML 

INPUT(Awards.j2,PadmaAwards.csv,col_names_tel_editted.xlsx) -> genXML_Render.ipynb -> OUTPUT(Awards_<from>-<to>.xml)

#### Files


* Jupyter Notebook - genXML_Render.ipynb
    - To generate XML 
    - a version on Python source is exported as genXML.py for convience 

the .xml files are the final output files 
- Awards_0-49.xml => xml for first 50 (i.e, 0,1,2,... 49 ) 
- Awards.xml => xml for entire dataset of 4420 entries

#### Folders
* dataset 
    - the final dataset in 3 formats -> excel,csv,pickle 
    - *** Note : Don't use excel since it shown a lot of data loss , prefer csv or load pickle into python. 

*  Template
    - Awards.j2 => jinja Template for generating xml