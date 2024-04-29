# Agent class is for creating an agent object with the following attributes:
#
# llm_model: str
# system_prompt: str
# user_prompt: str
#
# The class has an __init__ method that initializes the agent object with the given attributes.
#
# Example:
# agent = Agent(llm_model="model", system_prompt="prompt", user_prompt="prompt")
class Agent:
    def __init__(self, llm_model:str = None, system_prompt:str = None, user_prompt:str = None):
        self.model = llm_model
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt

class Tool:
    def __init__(self, name:str = None, description:str = None):
        self.name = name
        self.description = description
        