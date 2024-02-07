from mmengine.config import read_base

with read_base():
    from ..imports import *

_meta_template = dict(
    begin="<s>",
    round=[
        dict(role="HUMAN", begin='[INST]', end='[/INST]'),
        dict(role="BOT", begin="", end='</s>', generate=True),
    ],
    eos_token_id=2
)

name = 'mistral_7b_instruct_v02'
path = osp.join(model_base, name)


mistral_7b_instruct_v02 = dict(
    abbr=name,
    type=HuggingFaceCausalLM,
    path=path,
    tokenizer_path=path,
    model_kwargs=dict(
        device_map='auto',
        trust_remote_code=True,
    ),
    tokenizer_kwargs=dict(
        padding_side='left',
        truncation_side='left',
        trust_remote_code=True,
    ),
    meta_template=_meta_template,
    max_out_len=512,
    max_seq_len=8 * 1024,
    batch_size=8,
    run_cfg=dict(num_gpus=1, num_procs=1),
)
