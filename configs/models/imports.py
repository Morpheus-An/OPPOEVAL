from opencompass.models import HuggingFaceCausalLM, HuggingFace, HuggingFaceChatGLM3
from opencompass.models import OpenAI
import os.path as osp
import torch

# the base folder of local huggingface models
model_base = './models'

# use proxy for OpenAI api
openai_api_base='https://api.closeai-asia.com/v1/chat/completions'
# use the official api base using the following line
# openai_api_base = 'https://api.openai.com/v1/chat/completions'
