from fastapi import FastAPI
from setting import setting

app = FastAPI()

@app.get("/value/{variable}")
def read_variable(variable: str):
    value = setting.get_attribute(variable)
    return {variable: value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
