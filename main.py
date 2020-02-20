from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
	
 
class ConjuntoDeProcessos(BaseModel):
    # campos a serem recebidos
    npus: list
    # adicione aqui novos campos a serem recebidos


@app.post("/dados_de_processos/")
def dados_de_processos(conjunto: ConjuntoDeProcessos = Body(
        ...,
        example={
            "npus": [ "0001647-60.2019.8.17.8232",
                      "0819166-41.2019.8.15.2001",
                      "0000000-00.2013.8.15.2001",
                      "0000000-00.2013.8.15.2001",
                      "0000000-00.2013.8.15.2001",
                      "0000000-00.2013.8.15.2001",
                      "0000000-00.2013.8.15.2001",
                      "0000000-03.2010.8.15.0601",
                      "0000000-03.2014.5.23.0026",
                      "0000000-03.2014.5.23.0026" ]
        },
    )):
    
    return {"processos":conjunto}
