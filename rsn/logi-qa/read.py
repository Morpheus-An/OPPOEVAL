# from datasets import Dataset
# test_path = '/home/data_91_d/tangyh/data/rsn/logi-qa/test.txt'
# train_path = '/home/data_91_d/tangyh/data/rsn/logi-qa/train.txt'
# eval_path = '/home/data_91_d/tangyh/data/rsn/logi-qa/eval.txt'

# p = test_path
# print(p)

# with open(p, 'r', encoding='utf-8') as f:
#     lines = f.read()
# chunks = [e.strip() for e in lines.split('\n\n')]
# data_lists = []
# for chk in chunks:
#     l = chk.split('\n')
#     data_lists.append({
#         'label': l[0].upper(),
#         'context': l[1],
#         'question': l[1],
#         'A': l[3][2:],  # truncate the default letter
#         'B': l[4][2:],
#         'C': l[5][2:],
#         'D': l[6][2:],
#     })
# dataset = Dataset.from_list(data_lists)
# print(dataset)

