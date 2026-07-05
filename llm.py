from pathlib import Path
import ollama
from config import settings
SYSTEM_PROMPT=Path('prompts/system_prompt.txt').read_text()
class LocalLLM:
    def chat(self,msg):
        r=ollama.chat(model=settings.MODEL,messages=[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':msg}])
        return r['message']['content']
llm=LocalLLM()
