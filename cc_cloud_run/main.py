from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google.cloud import firestore
from typing import Annotated
import datetime

app = FastAPI()

# mount static files
app.mount("/static", StaticFiles(directory="/app/static"), name="static")
templates = Jinja2Templates(directory="/app/template")

# init firestore client
db = firestore.Client()
votes_collection = db.collection("votes")

@app.get("/")
async def read_root(request: Request):
    # stream all votes; count tabs / spaces votes, and get recent votes
    tabs_counter = 0
    spaces_counter = 0
    recent_votes = []
    try:
        votes = votes_collection.stream()

        for v in votes:
            vote = v.to_dict()
            recent_votes.append(vote)
            if vote.get("team") == "TABS":
                tabs_counter += 1
            elif vote.get("team") == "SPACES":
                spaces_counter += 1

        ##sort by most recent 
        recent_votes.sort(key=lambda x: x["time_cast"], reverse=True)

        return templates.TemplateResponse("index.html", {
        "request": request,
        "tabs_count": tabs_counter,
        "spaces_count": spaces_counter,
        "recent_votes": recent_votes
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/")
async def create_vote(team: Annotated[str, Form()]):
    if team not in ["TABS", "SPACES"]:
        raise HTTPException(status_code=400, detail="Invalid vote")
    
    try:
        vote = {
            "team": team,
            "time_cast": datetime.datetime.utcnow().isoformat()
        }
        votes_collection.add(vote)
        # create a new vote document in firestore
        return {"detail": "Created a new vote!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    # ====================================
    # ++++ START CODE HERE ++++
    # ====================================

    # ====================================
    # ++++ STOP CODE ++++
    # ====================================
