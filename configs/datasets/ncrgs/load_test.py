from opencompass.registry import LOAD_DATASET
# from opencompass.datasets import LogiqaDataset
# from oppoeval.datasets import ncrgsDataset
from oppoeval.datasets import ncrgs_datasets
import torch
print(torch.cuda.device_count())
path = '/home/ant/opencompass/oppodata/zh-spec/ncr-gs'
reader_cfg = dict(
    input_columns=['context', 'question', 'A', 'B', 'C', 'D'],
    output_column='label',
    train_range='[:100]',
    test_split='test'  # use which split as the test set
)
cfg = dict(
    type=ncrgsDataset,
    path=path,
    reader_cfg=reader_cfg
)
logiqa = LOAD_DATASET.build(cfg)
dataset = logiqa.reader.dataset  # huggingface DatasetDict
assert logiqa.test == dataset['test']
assert logiqa.train == dataset['train']
print(len(dataset))  # number of data split
print(len(logiqa.train))
print(len(logiqa.test))
print(logiqa.test[0])  # first element in the test 
# from opencompass.registry import LOAD_DATASET
# from oppoeval.datasets import LogiqaDataset
# # from opencompass.datasets import LogiqaDataset 

# path = '/home/data_91_d/tangyh/data/rsn/logi-qa'
# reader_cfg = dict(
#     input_columns=['context', 'question', 'A', 'B', 'C', 'D'],
#     output_column='label',
#     train_range='[:100]',
#     test_split='test'  # use which split as the test set
# )
# cfg = dict(
#     type=LogiqaDataset,
#     path=path,
#     reader_cfg=reader_cfg
# )
# logiqa = LOAD_DATASET.build(cfg)
# dataset = logiqa.reader.dataset  # huggingface DatasetDict
# assert logiqa.test == dataset['test']
# assert logiqa.train == dataset['train']
# print(len(dataset))  # number of data split
# print(len(logiqa.train))
# print(len(logiqa.test))
# print(logiqa.test[0])  # first element in the test set
