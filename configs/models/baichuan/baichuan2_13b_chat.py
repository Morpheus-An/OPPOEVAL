from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'baichuan2_13b_chat'
path = osp.join(model_base, 'baichuan2_13b_chat')

_meta_template = dict(
    round=[
        dict(role='HUMAN', begin='<reserved_106>'),
        dict(role='BOT', begin='<reserved_107>', generate=True),
    ],
)

baichuan2_13b_chat = dict(
    type=HuggingFaceCausalLM,
    abbr=name,
    path=path,
    tokenizer_path=path,
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True,
        use_fast=False,
    ),
    meta_template=_meta_template,
    max_out_len=256,
    max_seq_len=2048,
    batch_size=8,
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True,
        torch_dtype=torch.bfloat16
    ),
    run_cfg=dict(num_gpus=1, num_procs=1),
)
