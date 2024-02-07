import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

path = './models/internlm_chat_7b'
tokenizer = AutoTokenizer.from_pretrained(
    path,
    local_files_only=True,
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    path,
    local_files_only=True,
    torch_dtype=torch.float16,
    trust_remote_code=True
).cuda()
model = model.eval()

response, history = model.chat(tokenizer, "hello", history=[])
print(response)

response, history = model.chat(
    tokenizer, "please provide three suggestions about time management", history=history)
print(response)
