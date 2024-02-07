from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'llama_2_13b_chat_hf'
path = osp.join(model_base, name)

llama_2_13b_chat_hf = dict(
    abbr=name,
    type=HuggingFaceCausalLM,
    path=path,
    tokenizer_path=path,
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True
    ),
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True
    ),
    max_seq_len=4 * 1024,
    max_out_len=512,               # Maximum number of generated tokens
    batch_size=8,
    run_cfg=dict(num_gpus=1),
)
