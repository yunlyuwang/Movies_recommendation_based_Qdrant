from fastapi import FastAPI

# That is the file where NeuralSearcher is stored
from NeuralSearcher import NeuralSearcher

app = FastAPI()

neural_searcher = NeuralSearcher(collection_name='movies')

@app.get("/api/movies")
def movies_recomm(q: str):
    return {
        "result": neural_searcher.search(text=q)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)