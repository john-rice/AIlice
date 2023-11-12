from utils.AFileUtils import LoadTXTFile
from prompts.ARegex import GenerateRE4FunctionCalling

class APromptSystem():
    PROMPT_NAME = "search-engine"

    def __init__(self, processor, storage, collection, conversations, formatter, outputCB = None):
        self.processor = processor
        self.conversations = conversations
        self.formatter = formatter
        self.outputCB = outputCB
        self.prompt0 = LoadTXTFile("prompts/prompt_system.txt")
        self.PATTERNS = {"QUERY": [{"re": GenerateRE4FunctionCalling("QUERY<!|request: str|!> -> str", faultTolerance = True), "isEntry": True}],
                         "ARXIV": [{"re": GenerateRE4FunctionCalling("ARXIV<!|keywords: str|!> -> str", faultTolerance = True), "isEntry": True}],
                         "GOOGLE": [{"re": GenerateRE4FunctionCalling("GOOGLE<!|keywords: str|!> -> str", faultTolerance = True), "isEntry": True}],
                         "SCROLLDOWNGOOGLE": [{"re": GenerateRE4FunctionCalling("SCROLLDOWNGOOGLE<!||!> -> str", faultTolerance = True), "isEntry": True}],
                         "DUCKDUCKGO": [{"re": GenerateRE4FunctionCalling("DUCKDUCKGO<!|keywords: str|!> -> str", faultTolerance = True), "isEntry": True}],
                         "SCROLLDOWNDUCKDUCKGO": [{"re": GenerateRE4FunctionCalling("SCROLLDOWNDUCKDUCKGO<!||!> -> str", faultTolerance = True), "isEntry": True}],
                         "BROWSE": [{"re": GenerateRE4FunctionCalling("BROWSE<!|url: str|!> -> str", faultTolerance = True), "isEntry": True}],
                         "SCROLLDOWN": [{"re": GenerateRE4FunctionCalling("SCROLLDOWN<!||!> -> str"), "isEntry": True}]}
        self.ACTIONS= {}
        return
    
    def Reset(self):
        return
    
    def GetPatterns(self):
        return self.PATTERNS
    
    def GetActions(self):
        return self.ACTIONS
    
    def BuildPrompt(self):
        prompt = f"""
{self.prompt0}

End of general instructions.

"""
        #prompt += "Conversations:"
        return self.formatter(prompt0 = prompt, conversations = self.conversations.GetConversations(frm = -4))