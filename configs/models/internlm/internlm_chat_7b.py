from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'internlm_chat_7b'
path = osp.join(model_base, name)


_meta_template = dict(
    round=[
        dict(role='HUMAN', begin='<|User|>:', end='\n'),
        dict(role='BOT', begin='<|Bot|>:', end='<eoa>\n', generate=True),
    ],
)

internlm_chat_7b = dict(
    type=HuggingFaceCausalLM,
    abbr=name,
    path=path,
    tokenizer_path=path,
    model_kwargs=dict(
        trust_remote_code=True,
        device_map='auto',
    ),
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        use_fast=False,
        trust_remote_code=True,
    ),
    max_out_len=100,
    max_seq_len=2048,
    batch_size=8,
    meta_template=_meta_template,
    run_cfg=dict(num_gpus=1, num_procs=1),
    end_str='<eoa>',
)

