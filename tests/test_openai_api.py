import openai
from openai import OpenAI
print("openai package version = ", openai.__version__)

client = OpenAI(base_url='https://api.closeai-asia.com/v1')

models = [
    'gpt-3.5-turbo-1106',
    'gpt-3.5-turbo-0613',
    'gpt-4',
    'gpt-4-1106-preview'
]
for model in models:
    response = client.chat.completions.create(
        messages=[{'role': 'user', 'content': 'hello!'}],
        model='gpt-3.5-turbo-1106'
    )
    assert response.choices[0].finish_reason == 'stop', \
        f'Assertion Failed. OpenAI response:\n{response}'
    print(f'Test Passed: {model}')
