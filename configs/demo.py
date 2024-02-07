from mmengine.config import read_base
# from oppoeval.datasets import ncrgsDataset
with read_base():
    
    from .datasets.logiqa.logiqa_gen import logiqa_datasets
    from .datasets.ncrgs.ncrgs_gen import ncrgs_datasets
    from .models.opt.opt125m import opt125m
    from .models.gpt.gpt_3_5_turbo_1106 import gpt_3_5_turbo_1106
    from .models.baichuan.baichuan2_7b_chat import baichuan2_7b_chat
    from .models.baichuan.baichuan2_13b_chat import baichuan2_13b_chat
    from .models.qwen.qwen_7b_chat import qwen_7b_chat
    from .models.qwen.qwen_14b_chat import qwen_14b_chat
    from .models.internlm.internlm_chat_7b import internlm_chat_7b
    from .models.bluelm.bluelm_7b_chat import bluelm_7b_chat
    from .models.bluelm.bluelm_7b_base import bluelm_7b_base
    from .models.chatglm.chatglm2_6b import chatglm2_6b
    from .models.llama.llama_2_7b_chat_hf import llama_2_7b_chat_hf
    from .models.llama.llama_2_13b_chat_hf import llama_2_13b_chat_hf
    from .models.mistralai.mistral_7b_instruct_v02 import mistral_7b_instruct_v02
 
logiqa_datasets[0].update(
    dict(reader_cfg=dict(test_range="[:8]"))
)
ncrgs_datasets[0].update(
    dict(reader_cfg=dict(test_range="[:8]"))
)
# datasets = [*logiqa_datasets]
# custom_imports = dict(imports=['ncrgs_gen'], allow_failed_imports=False)
# optimizer = dict(type='CustomOptim')
datasets = [*ncrgs_datasets]

# models = [baichuan2_7b_chat]
# models = [qwen_7b_chat]
# models = [baichuan2_13b_chat]
# models = [qwen_14b_chat]
# models = [internlm_chat_7b]
# models = [bluelm_7b_chat]
# models = [chatglm2_6b]
# models = [llama_2_7b_chat_hf]
# models = [llama_2_13b_chat_hf]
# models = [bluelm_7b_base]
# models = [mistral_7b_instruct_v02]
models = [opt125m]
# models = [gpt_3_5_turbo_1106]

# work_dir = './outputs/logiqa/'
work_dir = './outputs/ncr-gs/'

