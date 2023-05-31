import openai
import os

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': 'Nói với tôi về việt nam !'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])