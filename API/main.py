from fastapi import FastAPI
import uvicorn
from data import DataAccess as da

app = FastAPI(redoc_url=None)

@app.get("/")
async def index():
    return {"Hello" : "world!"}

@app.get("/req_1")
async def requete_1():
    da.connexion()
    resultat = da.requete_1()
    da.deconnexion()
    return resultat

@app.get("/req_2")
async def requete_2():
    da.connexion()
    resultat = da.requete_2()
    da.deconnexion()
    return resultat

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)