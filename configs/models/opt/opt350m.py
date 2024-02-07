from mmengine.config import read_base

with read_base():
    from ..imports import *

name = 'opt350m'
path = osp.join(model_base, name)

opt125m = dict(
    abbr=name,
    type=HuggingFaceCausalLM,
    path=path,
    tokenizer_path=path,
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True),
    model_kwargs=dict(
        device_map='auto', trust_remote_code=True
    ),
    max_seq_len=2048,
    max_out_len=100,
    batch_size=64,
    run_cfg=dict(num_gpus=1),
)
