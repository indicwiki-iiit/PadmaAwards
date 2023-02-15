# Generate_XML 

This directory contains the final minimal set of files to generate XML 

INPUT(Awards.j2,PadmaAwards.csv,col_names_tel_editted.xlsx) -> genXML_Render.ipynb -> OUTPUT(Awards_<from>-<to>.xml)

## To Generate XML file
RUN by opening the terminal in this folder

```
python.exe genXML.py
```


## Files

* Jupyter Notebook - genXML_Render.ipynb
    - To generate XML 
    - a version on Python source is exported as genXML.py for convience
  
the .xml files are the final output files 
- Awards_0-49.xml => xml for first 50 (i.e, 0,1,2,... 49 ) 
- Awards.xml => xml for entire dataset of 4420 entries

## Folders
* dataset 
    - the final dataset in 3 formats -> excel,csv,pickle 
    - *** Note : Don't use excel since it shown a lot of data loss , prefer csv or load pickle into python. 

*  Template
    - Awards.j2 => jinja Template for generating xml
