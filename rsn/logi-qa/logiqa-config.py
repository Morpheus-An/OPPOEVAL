# from commons.common_import import *
# global ParentDataset
# EvalFuncDict.clear()


# TaskDescription = """\
# 请阅读以下描述，并回答描述后面的问题。\
# 你回答时只要输出正确答案的序号即可，不要输出多余的文字。\
# 请使用“答案：[你认为正确的选项]”的格式回答。\
# 比如，如果你认为正确选项为B，那么回答 “答案：B”。
# """
# QuestionPrompt = """
# {description}
# 问题: {question}
# {choices}
# 答案：
# {answer}
# """


# class Dataset(ParentDataset):
#     Description = {
#         "name": "LogiQA",
#     }

#     _passage_list = []

#     def analyse_file(self, fp: TextIO, sample_num: Optional[int] = None) -> List[Tuple[Any, Any]]:
#         """
#         :param fp: 带读取数据集的指针，以文本模式打开，utf-8编码
#         :param sample_num: 希望从数据集中读取样例数目，None表示全部读取
#         :return: 格式化后的样例列表。每个样例分为两部分，一部分用来生成prompt，一部分为标准答案，每部分具体格式不限制。
#         """
#         if sample_num is None:
#             sample_num = Metric.HUGE_POSITIVE
#         dataset = []
#         ans_list = ['a\n', 'b\n', 'c\n', 'd\n']
#         while line := fp.readline():
#             if line in ans_list:
#                 description = fp.readline()[:-1]
#                 question = fp.readline()[:-1]
#                 choices = [fp.readline()[2:-1].strip() for _ in range(4)]
#                 # answer = choices[ans_list.index(line)]
#                 answer = line.strip().upper()
#                 dataset.append(((description, question, choices), answer))
#         # print(dataset[0])
#         return dataset

#     def fill_prompt(self, sample: Any, answer: Any) -> Dict[str, str]:
#         """
#         :param sample: 一个样例
#         :param answer: 该样例对应的答案
#         :return: 文件开头Prompt模板中有一些未填充的变量，这里需返回一个字典，以这些变量名称为键，以该样例的信息为值
#         """
#         letter_list = "ABCDE"
#         description, question, choices = sample
#         return {
#             'description': description,
#             'question': question,
#             'choices': '\n'.join([f"{letter}.{choice}" for letter, choice in zip(letter_list, choices)]),
#             'answer': f'{answer}'
#         }
#         # return f"请阅读以下文章，并回答文章后面的问题：\n{self._passage_list[passage_idx]}\n" +\
#         #        f"问题: {question}\n（请选择正确答案，你的回答一定要完整地包括正确答案的序号和内容）\n" +\
#         #        '\n'.join([f"{letter}.{choice}" for letter, choice in zip("ABCDE", choice_list)])

#     def validate(self, llm_answer: str, std_answer: Any) -> Any:
#         """
#         :param llm_answer: 大模型给出的答案
#         :param std_answer: 标准答案
#         :return: 对模型给出的答案的评分，一般为布尔值或分数，也可以为其他
#         """
#         #NOTE: match the choice
#         llm_answer = clean_newlines(llm_answer)
#         lines = llm_answer.upper().split('\n')
#         score = 0
#         # try to find the prefix
#         idx = llm_answer.find("答案：")
#         if idx > 0:
#             ans = llm_answer[idx+3]
#             score = int(ans == std_answer)
#         else:  # no prefix found
#             for line in lines[::-1]:
#                 hits = [(c in line) for c in "ABCDE"]
#                 if sum(hits) == 1:
#                     idx = hits.index(True)
#                     ans = "ABCDE"[idx]
#                     score = int(ans == std_answer)
#                     break
#         self.info = None
#         return score

