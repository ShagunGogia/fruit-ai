from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class FAQ(BaseModel):
    id: int
    question: str
    answer: str

faqs_db = [
    FAQ(id=1, question="What is Apple?", answer="Apple is a fruit."),
    FAQ(id=2, question="What is Banana?", answer="Banana is a fruit."),
]

@app.get("/faqs", response_model=List[FAQ])
async def get_faqs():
    return faqs_db

@app.get("/faqs/{faq_id}", response_model=FAQ)
async def get_faq(faq_id: int):
    faq = next((faq for faq in faqs_db if faq.id == faq_id), None)
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq

@app.post("/faqs", response_model=FAQ)
async def create_faq(faq: FAQ):
    faqs_db.append(faq)
    return faq

@app.put("/faqs/{faq_id}", response_model=FAQ)
async def update_faq(faq_id: int, updated_faq: FAQ):
    for index, faq in enumerate(faqs_db):
        if faq.id == faq_id:
            faqs_db[index] = updated_faq
            return updated_faq
    raise HTTPException(status_code=404, detail="FAQ not found")

@app.delete("/faqs/{faq_id}")
async def delete_faq(faq_id: int):
    faq = next((faq for faq in faqs_db if faq.id == faq_id), None)
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    faqs_db.remove(faq)
    return {"message": "FAQ deleted"}
