from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, StrictStr
from typing import List, Optional, Union
import uvicorn
import nest_asyncio
import data_get as dg

############################################################################################################################################
app = FastAPI()

subapi = FastAPI(title="SPAM or HAM classifier", description="Classification of a paragraph into SPAM or HAM..")
############################################################################################################################################

@app.get("/status", status_code=200)
def read_status():
    log_info("API connected successfully.")
    return {"status": "API connected successfully"}


@subapi.get("/sub")
def read_sub(request: Request):
    return{
        "root_path": request.scope['root_path'],
        "raw_path": request.scope['raw_path'],
        "path": request.scope['path'],
        "app_url_for": app.url_path_for("read_sub"),
        "subapp_url_for": subapi.url_path_for("read_sub"),
    }

############################################################################################################################################

class values(BaseModel):
    input_text: Optional[StrictStr] = None
        
############################################################################################################################################
        
nest_asyncio.apply()

############################################################################################################################################

from typing import List
from fastapi import HTTPException

############################################################################################################################################
@subapi.post("/spam_classifier_")
async def smartapi_request(item: values):
    try:
        response = item.__dict__
        input_text = item.input_text
    

 
        try:
            input_text = eval(input_text)
            print(input_text)
            if not isinstance(input_text, list):
                raise ValueError("Invalid input format. Must be a string representation of a list.")
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid input format. Must be a string representation of a list.")


        result = dg.func_for_api(input_text)

        try:
            return result
        except Exception as e:
            return {"error": str(e)}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid request payload.")
############################################################################################################################################        
        
app.mount("/spam_classifier", subapi)

############################################################################################################################################
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, workers=1)

