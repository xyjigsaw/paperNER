# Name: paperNERapi
# Author: Reacubeth
# Time: 2020/6/5 15:35
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from predictNER import ModelPredict
from paper2XML import PaperXML

import time
import warnings

warnings.filterwarnings("ignore")

app = FastAPI()

model = ModelPredict('save')


@app.get("/paperNER/")
async def paper2kg(paperID: str):
    start = time.time()
    paper = PaperXML(paperID)
    NER = model.predict(paper.section_text, clear=True)
    return {"message": "success", "time": time.time() - start, "paperID": paperID, "data": NER['texts']}


class PostItem4Paper2Kg(BaseModel):
    paperID: str = None


@app.post('/post_paperNER')
async def post_paper2kg(request: PostItem4Paper2Kg):
    start = time.time()
    paper = PaperXML(request.paperID)
    NER = model.predict(paper.section_text, clear=True)
    return {"message": "success", "time": time.time() - start, "paperID": request.paperID, "data": NER['texts']}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000, workers=1)

# uvicorn paperNERapi:app --reload --port 7000 --host 127.0.0.1
