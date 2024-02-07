from .imports import *

@LOAD_DATASET.register_module()
class MyDataset(BaseDataset):
    @staticmethod
    def load_single(...) -> Dataset:  
        dataset = ...
        return dataset
        
         
    @staticmethod
    def load(path):
        '''
        path: folder of the dataset
        '''
        train_dataset = MyDataset.load_single(...)
        val_dataset = MyDataset.load_single(...)
        test_dataset = MyDataset.load_single(...)
        other_datasets = ...
        return DatasetDict({
            'train': train_dataset,
            'validation': val_dataset,
            'test': test_dataset,
            'some_other_splits': ...
        })
