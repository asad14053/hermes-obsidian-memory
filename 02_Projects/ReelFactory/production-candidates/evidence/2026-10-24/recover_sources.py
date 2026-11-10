import urllib.request, json
from pathlib import Path
from bs4 import BeautifulSoup
from pypdf import PdfReader
B=Path(__file__).parent
urls={
 'tbs':'https://www.tbsnews.net/bangladesh/govt-scraps-9-adp-projects-merges-32-tighten-fiscal-belt-1578911',
 'daily-sun':'https://www.daily-sun.com/front-page/904733',
 'worldbank':'https://documents.worldbank.org/curated/en/099021826030012463/pdf/P179009-3fada7ea-cfda-487d-8940-65f428488fa6.pdf'}
for name,url in urls.items():
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:
   data=r.read(); final=r.url
  if name=='worldbank':
   assert data.startswith(b'%PDF')
   p=B/'worldbank.pdf';p.write_bytes(data)
   reader=PdfReader(p)
   text='\n\n'.join(f'## Page {i}\n'+p.extract_text(extraction_mode='layout') for i,p in enumerate(reader.pages,1))
   (B/'worldbank.txt').write_text(text)
   print(name,final,'pages',len(reader.pages));print(text[:14000])
  else:
   (B/(name+'.html')).write_bytes(data)
   soup=BeautifulSoup(data,'html.parser')
   meta=[dict(t.attrs) for t in soup.find_all('meta') if any(k in str(t) for k in ['published','modified','date'])]
   for t in soup(['script','style','nav','footer','header']): t.decompose()
   text=soup.get_text('\n',strip=True)
   (B/(name+'-full.txt')).write_text(text)
   print(name,final,'metadata',json.dumps(meta),'length',len(text))
   for line in text.splitlines():
    if any(k in line for k in ['Oct','2026','Updated','Published']):print(line[:300])
 except Exception as e:print(name,type(e).__name__,str(e))
