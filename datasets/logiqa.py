from .imports import *


@LOAD_DATASET.register_module()
class LogiqaDataset(BaseDataset):
    @staticmethod
    def load_single(path:str, datafile:str) -> Dataset:
        p  =osp.join(path, datafile)
        with open(p, 'r', encoding = 'utf-8') as f:
            lines = f.read()
        chunks = [e.strip() for e in lines.split('\n\n')]
        data_lists = []
        for chk in chunks:
            l = chk.split('\n')
            data_lists.append({
                'label': l[0].upper(),
                'context':l[1],
                'question':l[2],
                'A':l[3][2:], # truncate the default letter
                'B':l[4][2:],
                'C':l[5][2:],
                'D':l[6][2:],
                })
        dataset = Dataset.from_list(data_lists)
        return dataset

    @staticmethod
    def load(path):
        '''
        path: folder of the dataset
        '''
        train_dataset = LogiqaDataset.load_single(path, 'train.txt')
        val_dataset = LogiqaDataset.load_single(path, 'eval.txt')
        test_dataset = LogiqaDataset.load_single(path, 'test.txt')
        return DatasetDict({
            'train': train_dataset,
            'validation': val_dataset,
            'test': test_dataset
        })
