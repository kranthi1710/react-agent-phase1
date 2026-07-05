from rich.panel import Panel
from core.console import console
from llm import llm
console.print(Panel.fit('ReAct Agent From Scratch'))
while True:
 q=input('You> ')
 if q.lower() in ['exit','quit']: break
 console.print(Panel(llm.chat(q),title='Assistant'))
