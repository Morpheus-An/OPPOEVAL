from mmengine.config import read_base

with read_base():
    from ..imports import *


name = 'chatglm2_6b'
path = osp.join(model_base, name)

chatglm2_6b = dict(
    type=HuggingFace,
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
        trust_remote_code=True,
    ),
    max_out_len=100,
    max_seq_len=4096,
    batch_size=8,
    run_cfg=dict(num_gpus=1, num_procs=1),
)
