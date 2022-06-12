
# basic fastapi application

from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") # this is an endpoint -> is user come to this endpoint, this function return {message: ...}
def home():
    return {"message": "hello world from app.py"}

@app.get("/test") # this is an endpoint
def test(): # if user come to /test -> message will be returned
    return {"message": "test"}

@app.get("/test/hello")
def test():
    return {"message": "test/hello"}

@app.get('/2206121718_01/hello')
def time_2206121718_01():
    return {'12 June 1718HRs': 'helloing at 12 Jun 5.18pm'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
