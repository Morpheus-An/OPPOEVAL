from mmengine.config import read_base

with read_base():
    from ..imports import *

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
)

name = 'gpt-4'

gpt_4 = dict(
    abbr=name,
    type=OpenAI, path=name,
    key='ENV',  # The key will be obtained from $OPENAI_API_KEY
    meta_template=api_meta_template,
    query_per_second=1,
    max_out_len=2048, max_seq_len=32 * 10245, batch_size=8,
    openai_api_base=openai_api_base
)
