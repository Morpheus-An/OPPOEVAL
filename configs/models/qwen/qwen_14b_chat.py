from mmengine.config import read_base

with read_base():
    from ..imports import *

_meta_template = dict(
    round=[
        dict(role="HUMAN", begin='\n<|im_start|>user\n', end='<|im_end|>'),
        dict(role="BOT", begin="\n<|im_start|>assistant\n",
             end='<|im_end|>', generate=True),
    ],
)

name = "qwen_14b_chat"
path = osp.join(model_base, name)

qwen_14b_chat = dict(
    type=HuggingFaceCausalLM,
    abbr=name,
    path=path,
    tokenizer_path=path,
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True
    ),
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True,
        use_fast=False,
    ),
    pad_token_id=151643,
    max_out_len=256,
    max_seq_len=2048,
    batch_size=8,
    meta_template=_meta_template,
    run_cfg=dict(num_gpus=1, num_procs=1),
    end_str='<|im_end|>',
)
