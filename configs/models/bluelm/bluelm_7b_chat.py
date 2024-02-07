from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'bluelm_7b_chat'
path = osp.join(model_base, name)

_meta_template = dict(
    round=[
        dict(role='HUMAN', begin='[|Human|]:'),
        dict(role='BOT', begin='[|AI|]:', generate=True),
    ],
)

bluelm_7b_chat = dict(
    type=HuggingFaceCausalLM,
    abbr=name,
    path=path,
    tokenizer_path=path,
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True,
        # torch_dtype=torch.bfloat16
    ),
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True,
        use_fast=False,
    ),
    meta_template=_meta_template,
    max_out_len=100,
    max_seq_len=2048,
    batch_size=8,
    run_cfg=dict(num_gpus=1, num_procs=1),
)
