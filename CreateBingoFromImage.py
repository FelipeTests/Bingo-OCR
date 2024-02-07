import easyocr
import requests 
import ssl 

requests.packages.urllib3.disable_warnings() 

try:
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass 
else: 
    ssl._create_default_https_context = _create_unverified_https_context

reader = easyocr.Reader(['en'])

def createBingoTable(image_src: str):
  result = reader.readtext(image_src, detail = 0)

  list = []

  for i in result:
    try:
      splitNumber = i.split("/")

      for index, splitNumElement in enumerate(splitNumber):
        if len(splitNumElement) == 5:
          del splitNumber[index]
          element1 = "" + splitNumElement[0] + splitNumElement[1]
          element2 = "" + splitNumElement[3] + splitNumElement[4]
          splitNumber.insert(index, element1)
          splitNumber.insert(index + 1, element2)

      print(splitNumber)
      for j in splitNumber:
        number = int(j)
        if number == 0:
          continue
        list.append(number)
    except:
      ""

  if len(list) == 25:
    del list[12]

  print(list)

  B = list[0:5]
  I = list[5:10]
  N = list[10:14]
  G = list[14:19]
  O = list[19:24]

  bingoTable = []
  bingoTable.append(B)
  bingoTable.append(I)
  bingoTable.append(N)
  bingoTable.append(G)
  bingoTable.append(O)

  return bingoTable
