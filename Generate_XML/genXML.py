import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("[+] INSTALLING REQUIRED PACKAGES")
subprocess.call('python.exe -m pip install --upgrade pip')
pkgs = ['pandas','numpy','tqdm','jinja2','openpyxl']
for pkg in pkgs:
    install(pkg)

import string
from hashlib import sha1
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pandas as pd
from tqdm import tqdm

Fail = True
awards = pd.read_pickle('dataset/PadmaAwards.pickle')
awards.sort_index(inplace=True)
padma_awards = awards.copy()
padma_awards.reset_index(inplace=True)
try:
    print(f'\n\n\nThe Awards dataset has {awards.shape[0]} rows \nFrom these range 0 to {awards.shape[0]} select From and to\nNOTE : To generate Total dataset enter "0" for both From and to\n\n')
    # From_n = 0
    From_n = int(input('Enter From (Where the xml should start, 0 if all) : '))
    To_n = int(input('Enter To (Where the xml should end, 0 if all) : '))
    if From_n == To_n and From_n == 0 and To_n == 0:
        From_n = None
        To_n = None
        print('\n\n[+] RESULT in Awards.xml FILE \n\n')
    elif To_n <= From_n or From_n > awards.shape[0] or To_n > awards.shape[0]  :
        print('[-] Not in Correct RANGE')
        raise Exception
    else:
        print(f'\n\n[+] RESULT in Awards_{From_n}-{To_n}.xml FILE \n\n')

except:
    Fail = False
    print('\n\n[-] Failed\t PLEASE RUN AGAIN \n\n')

def add_(text):
    return "_".join(text.split(' '))

awards_colName = pd.read_excel('dataset/col_names_tel_editted.xlsx')
awards_colName['colName'] = awards_colName['colName'].apply(add_,)
colName_tel = dict(zip(awards_colName['colName'],awards_colName['colNameTelugu']))



## Change below siteinfo if different website is picked ##
tewiki = '''<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="te">
  <siteinfo>
    <sitename>tewiki</sitename>
    <dbname>indicwiki</dbname>
    <base>https://tewiki.iiit.ac.in/index.php?title=%E0%B0%AE%E0%B1%8A%E0%B0%A6%E0%B0%9F%E0%B0%BF_%E0%B0%AA%E0%B1%87%E0%B0%9C%E0%B1%80</base>
    <generator>MediaWiki 1.34.0</generator>
    <case>first-letter</case>
    <namespaces>
      <namespace key="-2" case="first-letter">మీడియా</namespace>
      <namespace key="-1" case="first-letter">ప్రత్యేక</namespace>
      <namespace key="0" case="first-letter" />
      <namespace key="1" case="first-letter">చర్చ</namespace>
      <namespace key="2" case="first-letter">వాడుకరి</namespace>
      <namespace key="3" case="first-letter">వాడుకరి చర్చ</namespace>
      <namespace key="4" case="first-letter">Project</namespace>
      <namespace key="5" case="first-letter">Project చర్చ</namespace>
      <namespace key="6" case="first-letter">దస్త్రం</namespace>
      <namespace key="7" case="first-letter">దస్త్రంపై చర్చ</namespace>
      <namespace key="8" case="first-letter">మీడియావికీ</namespace>
      <namespace key="9" case="first-letter">మీడియావికీ చర్చ</namespace>
      <namespace key="10" case="first-letter">మూస</namespace>
      <namespace key="11" case="first-letter">మూస చర్చ</namespace>
      <namespace key="12" case="first-letter">సహాయం</namespace>
      <namespace key="13" case="first-letter">సహాయం చర్చ</namespace>
      <namespace key="14" case="first-letter">వర్గం</namespace>
      <namespace key="15" case="first-letter">వర్గం చర్చ</namespace>
      <namespace key="106" case="first-letter">Form</namespace>
      <namespace key="107" case="first-letter">Form talk</namespace>
      <namespace key="120" case="first-letter">Item</namespace>
      <namespace key="121" case="first-letter">Item talk</namespace>
      <namespace key="122" case="first-letter">Property</namespace>
      <namespace key="123" case="first-letter">Property talk</namespace>
      <namespace key="482" case="first-letter">Config</namespace>
      <namespace key="483" case="first-letter">Config talk</namespace>
      <namespace key="710" case="first-letter">TimedText</namespace>
      <namespace key="711" case="first-letter">TimedText talk</namespace>
      <namespace key="828" case="first-letter">మాడ్యూల్</namespace>
      <namespace key="829" case="first-letter">మాడ్యూల్ చర్చ</namespace>
      <namespace key="2300" case="first-letter">Gadget</namespace>
      <namespace key="2301" case="first-letter">Gadget talk</namespace>
      <namespace key="2302" case="case-sensitive">Gadget definition</namespace>
      <namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
      <namespace key="2600" case="first-letter">Topic</namespace>
      <namespace key="3022" case="first-letter">Tewiki</namespace>
      <namespace key="3023" case="first-letter">Tewiki talk</namespace>
    </namespaces>
  </siteinfo>'''

# 700000 - 715000 => bird's articles

page_id = 1000000

user_id ="18852"
username ="Yallamahanth"

# Funtions to write page to file object
def sha36(page_id):
	page_id = str(page_id).encode('utf-8')
	sha16 =sha1(page_id).hexdigest()
	sha10 =int(sha16, 16)

	chars =[]
	alphabets = string.digits +string.ascii_lowercase
	while sha10>0:
		sha10, r = divmod(sha10, 36)
		chars.append(alphabets[r])
	
	return ''.join(reversed(chars))

# Function to replace possible Entity references
def clean(text):
	text = text.replace('&',"&amp;")
	text = text.replace('<',"&lt;")
	text = text.replace('>',"&gt;")
	text = text.replace('"',"&quot;")
	text = text.replace("'","&apos;")

	return text

def clean_format(text):
	text = text.replace('..',".")
	text = text.replace(',.',".")
	text = text.replace('.,',".")
	text = text.replace(' . ',". ")
	text = text.replace(' , ',", ")
	text = text.replace(' . ',". ")
	text = text.replace(' , ',", ")
	text = text.replace('  '," ")

	return text

# Function to generate XML content that uses title and rendered awards from render.py
def writePage(title, wikiText, fobj):
	global user_id, username, page_id

	pglen = len(wikiText)
	time =datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")
	
	curPage ='''\n\n
	<page>
		<title>''' +clean(title) +'''</title>
		<ns>0</ns>
		<id>''' +str(page_id) +'''</id>
		<revision>
			<id>''' +str(page_id) +'''</id>
			<timestamp>'''+time+'''</timestamp>
			<contributor>
				<username>''' +username +'''</username>
				<id>''' +str(user_id) +'''</id>
			</contributor>
			<comment>xmlpage created</comment>
			<model>wikitext</model>
			<format>text/x-wiki</format>
			<text xml:space="preserve" bytes="''' +str(pglen) +'''">
			\n''' + clean_format(clean(wikiText)) +'''
			</text>
			<sha1>''' +sha36(page_id) +'''</sha1>
		</revision>
	</page>
	\n\n'''

	fobj.write(curPage)
	page_id += 1
	return

def getData(data,A):
    row_dict = {'Recipients':A,'colName_tel':colName_tel}
    award_dict = dict(data.loc[A])
    for k,v in zip(award_dict,award_dict.values()):
        if pd.isna(v) :
            row_dict["_".join(k.split(' '))] = 'NaN'
        else:
            row_dict["_".join(k.split(' '))] = str(v).strip()
    numericals = ['Padma_Shri_Year','Padma_Bhushan_Year','Padma_Vibhushan_Year','Page_Id']
    new_dic = {}
    flag = 0
    remove_list = ['Summary_Telugu','further_reading_Telugu']
    for k,v in row_dict.items():
        if k == 'Summary':
            flag = 1
        if flag and 'Telugu' in k and k not in remove_list:
            new_dic[k] = v
    row_dict['body'] = new_dic
    for c_n in numericals:
        if row_dict[c_n] != 'NaN':
            try:
                row_dict[c_n] = str(int(float(row_dict[c_n])))
            except:
                continue
    ref_dic = {}
    row_dict['ref_dict'] = ref_dic
    if row_dict['Ref'] != 'NaN':
        refs =  row_dict['Ref'].split(';')
        for ref in refs:
            try:
                ref_dic[ref] = ref.split('//')[1].split('/')[0]
            except Exception:
                pass
        row_dict['ref_dict'] = ref_dic
    return row_dict

file_loader = FileSystemLoader('./Template/')
env = Environment(loader=file_loader)
env.globals.update(zip=zip)
env.globals.update(len=len)
env.add_extension('jinja2.ext.do')
template = env.get_template('Awards.j2')

if Fail:
    if not From_n:
        From_n = 0
    if not To_n:
        To_n = awards.shape[0]
    if From_n!= 0 or To_n != awards.shape[0] :
        To_n += 1
        fobj = open('Awards_'+str(From_n)+'-'+str(To_n-1)+'.xml', 'w', encoding="utf-8")
        fobj.write(tewiki+'\n')
    else:
        fobj = open('Awards.xml', 'w', encoding="utf-8")
        fobj.write(tewiki+'\n')

    # for i in tqdm(range(padma_awards.shape[0])):
    # for i in tqdm(range(5)):
    for i in tqdm(range(From_n,To_n)):
        title2 = padma_awards['Recipients Telugu'][i]
        title = padma_awards['Recipients'][i]
        text = template.render(getData(awards,title)) 

        writePage(title2, text, fobj)

    fobj.write('</mediawiki>')
    fobj.close()
    # To_n -= 1