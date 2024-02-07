from commons.common_import import *
global ParentDataset
EvalFuncDict.clear()


TaskDescription = """\
请阅读以下文章，并回答文章后面的问题。\
你回答时只要输出正确答案的序号即可，不要输出多余的文字。
"""
QuestionPrompt = """
{passage}
问题: {question}
{choices}
答案：
{answer}
"""


class Dataset(ParentDataset):
    Description = {
        "name": "C3 - m",
    }

    _passage_list = []

    def analyse_file(self, fp: TextIO, sample_num: Optional[int] = None) -> List[Tuple[Any, Any]]:
        """
        :param fp: 带读取数据集的指针，以文本模式打开，utf-8编码
        :param sample_num: 希望从数据集中读取样例数目，None表示全部读取
        :return: 格式化后的样例列表。每个样例分为两部分，一部分用来生成prompt，一部分为标准答案，每部分具体格式不限制。
        """
        if sample_num is None:
            sample_num = 999999999
        dataset = []
        for passage, question_list, _ in json.load(fp)[:sample_num]:
            passage_idx = len(self._passage_list)
            self._passage_list.append(''.join(passage))
            for question in question_list:
                choices = question['choice']
                answer = question['answer']
                answer_choice = "ABCDE"[choices.index(answer)]
                dataset.append((
                    (passage_idx, question['question'], choices),
                    answer_choice
                ))
            # dataset.extend([
                # ((passage_idx, question['question'], question['choice']), question['answer'])
                # for question in question_list
            # ])
        print(dataset[0])
        return dataset

    def fill_prompt(self, sample: Any, answer: Any) -> Dict[str, str]:
        """
        :param sample: 一个样例
        :param answer: 该样例对应的答案
        :return: 文件开头Prompt模板中有一些未填充的变量，这里需返回一个字典，以这些变量名称为键，以该样例的信息为值
        """
        letter_list = "ABCDEE"
        passage_idx, question, choice_list = sample
        answer_idx = -1
        for i, choice in enumerate(choice_list):
            if choice == answer:
                answer_idx = i
                break
        return {
            'passage': self._passage_list[passage_idx],
            'question': question,
            'choices': '\n'.join([f"{letter}.{choice}" for letter, choice in zip(letter_list, choice_list)]),
            'answer': f'{letter_list[answer_idx]}'
            # 'answer': f'{letter_list[answer_idx]}.{answer}'
        }
        # return f"请阅读以下文章，并回答文章后面的问题：\n{self._passage_list[passage_idx]}\n" +\
        #        f"问题: {question}\n（请选择正确答案，你的回答一定要完整地包括正确答案的序号和内容）\n" +\
        #        '\n'.join([f"{letter}.{choice}" for letter, choice in zip("ABCDEE", choice_list)])

    def validate(self, llm_answer: str, std_answer: Any) -> Any:
        """
        :param llm_answer: 大模型给出的答案
        :param std_answer: 标准答案
        :return: 对模型给出的答案的评分，一般为布尔值或分数，也可以为其他
        """
        llm_answer = clean_newlines(llm_answer)
        lines = llm_answer.upper().split('\n')
        score = 0
        # try to find the prefix
        idx = llm_answer.find("答案：")
        if idx > 0:
            ans = llm_answer[idx+3]
            score = int(ans == std_answer)
        else:  # no prefix found
            for line in lines[::-1]:
                hits = [(c in line) for c in "ABCDE"]
                if sum(hits) == 1:
                    idx = hits.index(True)
                    ans = "ABCDE"[idx]
                    score = int(ans == std_answer)
                    break
        self.info = None
        return score

        '''
        for line in llm_answer.split('\n')[::-1]:
            for _letter in 'ABCDE':
                pos = line.find(_letter + '.')
                if pos != -1:
                    score = line[pos + 2:].strip()[:len(std_answer)] == std_answer
                    break
            else:
                continue
            break
        else:
            score = llm_answer.find(std_answer) != -1
        self.info = None
        return score
       '''
