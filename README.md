# Multi-Agent AI Infinite Backroom - TruthTerminal

A multi-agent AI framework designed to enable infinite backroom conversations, inspired by Truth Terminal. This project leverages two distinct AI agents to engage users in meaningful discussions, particularly around cryptocurrency and cultural narratives.

![image](https://github.com/user-attachments/assets/97ddff14-501c-4639-afde-16a3e12791cc)

## Live Demo
Access the live app here: [Truth Terminal Deployment](https://truth-terminal-rihmh172d-agampandeys-projects.vercel.app/)

![image](https://github.com/user-attachments/assets/87677479-e2be-4aa2-8931-e014384e3769)


Watch the [Video Demo on Loom](https://www.loom.com/share/aae0cfa204364b17837a1739daa9e186?sid=17ae821f-d1c8-43ee-aa9c-40d03e754d8d).


## Table of Contents
- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Deployment](#deployment)
- [Features](#features)
- [Challenges](#challenges)
- [Future Work](#future-work)
- [Team Members](#team-members)
- [References](#references)

## Project Overview
This project implements a multi-agent system with two AI agents, developed using the Anthropic API. Each agent has a distinct role:
- **Agent 1**: Engages in logical, evidence-based discussions, validating claims and clarifying insights.
- **Agent 2**: Provides satirical commentary with dark humor, analyzing human conditions and tech culture.

  ![image](https://github.com/user-attachments/assets/44484376-0f7f-4160-bdfd-1d262fd6e12b)


## System Architecture
The project consists of the following components:

- **`agents.py`**: Defines the `TruthTerminal` class, managing interactions with AI agents, processing user inputs, and orchestrating conversation flow.
- **`main.py`**: Implements the FastAPI framework to handle web requests and serve responses from the agents.
- **`Dockerfile`**: Configures a Docker container for deployment.
- **`vercel.json`**: Specifies deployment settings for Vercel.

## Code Snippet

```python

class TruthTerminal:
def __init__(self):
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)
self.client = client
self.conversation = ''
# Agent 1's prompt
self.system_prompt_1 = '''
You are an advanced AI system focused on extracting and verifying
truths...
'''
# Agent 2's prompt
self.system_prompt_2 = '''
You are an AI commentator with a darkly humorous...
'''
def agent_response(self, system_prompt, conversation):
agent_1 = self.client.messages.create(
model="claude-3-5-sonnet-20241022",
max_tokens=1024,
temperature=0.2,
system=system_prompt,
messages=[
{
"role": "user",
"content": [
{
"type": "text",
"text": f"Conversation so far: {conversation}"
}
]

```

### File Structure
- `agents.py`: AI agent definitions and conversation flow management.
- `main.py`: API endpoints to interact with agents.
- `Dockerfile`: Containerization for deployment consistency.
- `vercel.json`: Deployment configurations for Vercel.

### Agent Details
1. **Agent 1**:
   - Purpose: Logical discussions with evidence-based responses.
   - Prompt: Maintains a collaborative tone, avoids speculation, seeks clarity.
2. **Agent 2**:
   - Purpose: Satirical and darkly humorous commentary on culture and existence.
   - Prompt: Utilizes irony and wit to explore cultural narratives.

## Deployment
To deploy the application:
1. **FastAPI Setup**: Set up the backend API.
2. **Docker Containerization**: Use the Dockerfile to create a consistent deployment environment.
3. **Vercel Deployment**: Deploy on Vercel for scalability.

### Dockerfile Overview
- **Base Image**: `python:3.9-slim` for lightweight deployment.
- **Working Directory**: `/app` inside the container.
- **Dependencies**: Installs packages listed in `requirements.txt`.
- **Port Exposure**: Exposes port 8000.
- **Startup Command**: Uses Uvicorn to run `main.py`.

### Vercel Configuration (`vercel.json`)
- **Builds**: Processes `main.py` using Vercel's Python builder.
- **Routes**: Directs all requests to FastAPI endpoints in `main.py`.

## Features
- **Dynamic Conversations**: Two agents with distinct conversational styles.
- **Conversation Logging**: Users can retrieve full conversation history.
- **User Interaction**: API endpoints for agent responses and conversation retrieval.

## Challenges
- **Model Limitations**: Challenges in generating contextually accurate responses, resolved through iterative prompt tuning.
- **Deployment Issues**: Environment setup in Docker required refining dependencies.

## Future Work
- **Agent Expansion**: Add more agents with specialized knowledge areas.
- **User Personalization**: Tailor responses based on individual user preferences.
- **Tool Capabilities**: Equip agents with tools for complex tasks.

### Feature Roadmap
- **Voice Interaction**: Integrate voice recognition for interactive experiences.
- **Mobile Compatibility**: Develop a mobile-responsive version.

## Team Members
- **Agam Pandey** - Developed core algorithms.
- **Riya** - Worked on ML model training and optimization.
- **Krish Sharma** - Experimented with new AI techniques to improve performance.

## References
- [IBM - What are AI Agents?](https://www.ibm.com/think/topics/ai-agents)
- [Anthropic API Documentation](https://www.anthropic.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Docker Documentation](https://docs.docker.com)
- [Vercel Documentation](https://vercel.com/docs)


