from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'vicuna_7b_v15'
path = osp.join(model_base, name)


vicuna_7b_v15 = dict(
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
    max_out_len=512,
    max_seq_len=4 * 1024,
    batch_size=8,
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True
    ),
    use_fastchat_template=True,  # set as True for vicuna
    run_cfg=dict(num_gpus=1, num_procs=1)
)
