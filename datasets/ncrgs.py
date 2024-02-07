from .imports import *



@LOAD_DATASET.register_module()
class ncrgsDataset(BaseDataset):
    @staticmethod
    def load_single(path:str, datafile:str) -> Dataset:
        p = osp.join(path, datafile)
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        data_lists = []
        count = 0
        for d in data:
            for q in d['Questions']:
                data_lists.append({
                    'context': d['Content'],
                    'label': q['Answer'],
                    'question': q['Question'],
                })
                for i in range(len(q['Choices'])):
                    data_lists[-1][chr(ord('A')+i)] = q['Choices'][i][2:]

        dataset = Dataset.from_list(data_lists)
        return dataset 

    @staticmethod
    def load(path):
        '''
        path: folder of the dataset
        '''
        test_dataset = ncrgsDataset.load_single(path, 'test.json')
        return test_dataset
       


