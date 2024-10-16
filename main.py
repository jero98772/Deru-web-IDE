from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import subprocess
import os
from deru.deru import REP
app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/execute")
async def execute_code(request: CodeRequest):
    try:
        """
        with open("deruuk/temp.dru", "w") as f:
            f.write(request.code)
        
        result = subprocess.run(
            ["python", "deruuk/deruuk.py","deruuk/temp.dru"],
            capture_output=True,
            text=True,
            check=True
        )
        """
        out=""
        code=request.code.split("\n")
        for i in code:
            print(i)
            out+=REP(i)+"\n"
        return {"output":out , "error":""}#{"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Execution Error: {e.stderr}")
