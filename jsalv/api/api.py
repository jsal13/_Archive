import random
from fastapi import FastAPI

api = FastAPI()

# Open external files to get data.
with open("./data/word_list.txt", "r") as f_words:
    WORD_LIST = list(word.strip() for word in f_words.readlines())


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.get("/word-list")
async def word_list():
    num_words = random.randint(2, 4)
    words = " ".join(random.sample(WORD_LIST, k=num_words))
    return words
