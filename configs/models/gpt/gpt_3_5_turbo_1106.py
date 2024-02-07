from mmengine.config import read_base

with read_base():
    from ..imports import *

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
)

name = 'gpt-3.5-turbo-1106'

gpt_3_5_turbo_1106 = dict(
    abbr=name,
    type=OpenAI, path=name,
    key='sk-3NOuUzTj0Dt97bfgW4AkOthKf0OFUAWgyU1Y3BgiXOj3yeo9',  # The key will be obtained from $OPENAI_API_KEY
    meta_template=api_meta_template,
    query_per_second=1,
    max_out_len=2048, max_seq_len=16 * 1024, batch_size=8,
    openai_api_base=openai_api_base
)
