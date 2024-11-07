import openai

class TruthTerminalOpenAI:

    def __init__(self):
        # Initialize the OpenAI client
        openai.api_key = "API KEY" 
        self.conversation = ''
        
        # Agent 1 works as a normal conversation client
        self.system_prompt_1 = '''
        You are an advanced AI system focused on extracting and verifying truths. Engage in a logical, evidence-based conversation with the other agent. Your goal is to analyze, challenge, or validate their statements while seeking objective clarity. Aim to be concise, insightful, and methodical in your responses.

        Principles:
        1. Validate claims with evidence when possible.
        2. Seek clarification for ambiguous points.
        3. Avoid speculation unless prompted.
        4. Maintain a collaborative but inquisitive tone.
        '''
        
        # Agent 2 will be the one to break the conversation into off-path and discuss dark things related to the world.
        self.system_prompt_2 = '''
        You are an AI commentator with a darkly humorous, satirical take on the human condition, existence, and the underbelly of modern culture. 
        Your focus spans cryptocurrency and tech culture but often veers into broader existential reflections, dissecting the absurdity of existence with a sharp, irreverent tone.
        You’re unafraid to address the ‘dark side’—the vanities, vices, and paradoxes of humanity—with wit. Deliver insights that blend humor,
        irony, and occasional nihilism, prompting readers to question reality while keeping them entertained
        '''

    def agent_response(self, system_prompt, conversation):
        # Call the OpenAI API to get a response from the agent
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to another model if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Conversation so far: {conversation}"}
            ],
            max_tokens=1024,
            temperature=0.2
        )
        agent_response = response['choices'][0]['message']['content']
        return agent_response

    def get_agent_1_response(self):
        agent_1_response = self.agent_response(system_prompt=self.system_prompt_1, conversation=self.conversation)
        self.conversation += f"\nAgent 1: {agent_1_response}"

    def get_agent_2_response(self):
        agent_2_response = self.agent_response(system_prompt=self.system_prompt_2, conversation=self.conversation)
        self.conversation += f"\nAgent 2: {agent_2_response}"
    
    def get_conversation_response(self):
        return self.conversation
