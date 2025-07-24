from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from http import HTTPStatus

app = FastAPI()

players = []

class Player(BaseModel):
    number: int
    name: str

@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return "<html><body><h1>Hello</h1></body></html>"

@app.get("/welcome")
async def welcome(name: str):
    return {"message": f"Welcome {name}"}

@app.post("/players", status_code=HTTPStatus.CREATED)
async def add_players(new_players: List[Player]):
    players.extend(new_players)
    return players

@app.get("/players")
async def get_players():
    return players

@app.put("/players")
async def update_or_add_player(player: Player):
    for i, existing_player in enumerate(players):
        if existing_player.number == player.number:
            players[i] = player
            return players
    players.append(player)
    return players

@app.get("/players-authorized")
async def get_players_authorized(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Authorization header missing"
        )
    if authorization != "bon courage":
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Invalid authorization credentials"
        )
    return players