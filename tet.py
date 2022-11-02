import requests
import zipfile
import io

r = requests.get('https://api.github.com/repos/todolodo/cod-python-api/releases/latest')
j = r.json()
print(j['zipball_url'] if 'zipball_url' in j else None)

r = requests.get('https://api.github.com/repos/TodoLodo/cod-python-api/zipball/v2.0.1')

#print(r.content)

z = zipfile.ZipFile(io.BytesIO(r.content))

for f in z.infolist():
    print(f)

print(z.namelist())

