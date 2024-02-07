from fastapi import FastAPI
from CreateBingoFromImage import createBingoTable

app = FastAPI()

@app.get("/bingo")
def index(image_src: str):
  return createBingoTable(image_src)
