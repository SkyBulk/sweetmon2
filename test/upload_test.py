import requests

#header = {"apikey":"fbfe6f239502196947e98db2bce0c74c02e93216b2f2cbc558d267d1bdfce04a"}
header = {"apikey":"87723518ea2d8c66eb090fc711972e9dd998b8a491abf26d46be739395754780"}

post = {"title":"yks_", "crashlog":"test"}
files = {'file': "asdasd"}

r = requests.post("http://localhost:8000/api/v1/crash/upload", files=files, data=post, headers=header)
print(r.text)


r = requests.get("http://localhost:8000/api/v1/fuzzer/ping", headers=header)
print(r.text)

r = requests.get("http://localhost:8000/api/v1/storage/list", headers=header)
print(r.text)
