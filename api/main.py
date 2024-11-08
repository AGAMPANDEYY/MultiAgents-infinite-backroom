from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .agents import TruthTerminal
from .openai_agents import TruthTerminalOpenAI

app = FastAPI()
truth_terminal = TruthTerminal()
#truth_terminal = TruthTerminalOpenAI()

# Define the path for the static directory using an absolute path
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    file_path = static_dir / "index.html"
    print(f"Serving index file from: {file_path}")  # Debugging line
    with open(file_path) as file:
        return HTMLResponse(file.read())


@app.get("/agent1")
async def get_agent_response():

    """ Get response from Agent 1"""
    response=truth_terminal.get_agent_1_response()
    print(f"Agent 1 response:{response}")
    return {"response": response}

@app.get("/agent2")
async def get_agent_2_response():

    """ Get response from Agent 2"""
    response=truth_terminal.get_agent_2_response()
    print(f"Agent 2 response:{response}")
    return {"response": response}

@app.get("/conversation")
async def get_conversation_response():
    """ Get conversation history"""
    conversation=truth_terminal.get_conversation_response()
    print(f"Conversation retrieved: {conversation}")
    return {"conversation": conversation}


@app.get("/welcome")
async def welcome_screen():
    return "Welcome to Truth Terminal"