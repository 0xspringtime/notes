- prompt: aka context, is the text provided to a model before it begins generating output

- hidden prompt: portions of the prompt that are never intended to be seen by the user

- token: atomic unit of consumption for a language model; roughly 750 words per 1,000 tokens

- stateless: property in general of LLMs; won’t remember anything about previous requests

- context window: total size of prompt, GPT-3, it is 4,096 tokens. For GPT-4, it is 8,192 tokens or 32,768 tokens depending on which variant

- OpenAI token limit includes both input and output length

- jailbreak: typically hidden prompts will tell the bot to behave with a certain persona and focus on specific tasks or avoid certain words

- It is crucial to assume that any data exposed to the language model will eventually be visible to the user, including embedded data in hidden prompts.

- Give a Bot a Fish: scenario in which you can explicitly give the bot, in the hidden context, all of the information it needs to do whatever task is requested of it

- Sementic Search: oriented around document embedding

- Teach a Bot to Fish: you want the bot to have the capability to perform actions on the user’s behalf, like adding a memo to a receipt or plotting a chart

- Command Grammars: give the bot a list of commands for our system to interpret, along with descriptions and examples for the commands, and then have it produce programs composed of those commands

- few-shot learners: can learn a new task by being provided just a few examples

-  ReAct: variant of command grammars with fully autonomous interactive execution of actions and retrieval of data

- Chain of Thought: asking bot to think step-by-step

- Fine Tuning: process of taking an already trained model and then giving it thousands (or more) of example input:output pairs

