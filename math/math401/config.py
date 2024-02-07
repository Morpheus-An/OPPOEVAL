from commons.common_import import *
global ParentDataset
EvalFuncDict.clear()


TaskDescription = """\
请你进行算式运算。\
式子中的 e 指自然对数的底数，i 指虚数单位， π 指圆周率。\
log 10 指以 10 为底数的对数， log 2 指以 2 为底数的对数。\
你的计算结果应当以 10 进制表示，分数、循环小数、无理数应该保留至少 4 位小数。\
请你以“答案：<计算结果>”的形式给出答案。比如, 计算结果是 9 时，请输出“答案：9”。\
请你直接给出计算结果，不要输出其他任何多余字符。
"""
QuestionPrompt = """\
算式：
{question}
答案：{answer}
"""


class Dataset(ParentDataset):
    Description = {
        "name": "math401",
    }

    _passages = []

    def analyse_file(self, fp: TextIO, sample_num: Optional[int] = None) -> List[Tuple[Any, Any]]:
        """
        :param fp: 带读取数据集的指针，以文本模式打开，utf-8编码
        :param sample_num: 希望从数据集中读取样例数目，None表示全部读取
        :return: 格式化后的样例列表。每个样例分为两部分，一部分用来生成prompt，一部分为标准答案，每部分具体格式不限制。
        """
        if sample_num is None:
            sample_num = Metric.HUGE_POSITIVE
        dataset = []
        while line := fp.readline():
            if len(dataset) >= sample_num:
                break
            line = eval(line)
            dataset.append(((line['query'], ), line['response']))
        return dataset

    def fill_prompt(self, sample: Any, answer: Any) -> Dict[str, str]:
        """
        :param sample: 一个样例
        :param answer: 该样例对应的答案
        :return: 文件开头Prompt模板中有一些未填充的变量，这里需返回一个字典，以这些变量名称为键，以该样例的信息为值
        """
        question, = sample
        return {
            'question': question,
            'answer': answer,
        }

    def validate(self, llm_answer: str, std_answer: Any) -> Any:
        """
        :param llm_answer: 大模型给出的答案
        :param std_answer: 标准答案
        :return: 对模型给出的答案的评分，一般为布尔值或分数，也可以为其他
        """
        idx = llm_answer.rfind("答案：")
        if idx > -1:
            llm_answer = llm_answer[idx+3:]
        try: # threshold 0.001
            if abs(float(llm_answer) - float(std_answer)) < 1e-3:
                score = True
            else:
                score = False
        except ValueError:
            idx = llm_answer.find(std_answer)
            if idx == -1:
                score = 0
            else:
                ans = (' ' + llm_answer + ' ')[idx: idx + len(std_answer) + 2]
                if ans[0] not in '-0123456789' and ans[-1] not in '0123456789.':
                    score = True
                else:
                    score = False
        self.info = None
        return score
