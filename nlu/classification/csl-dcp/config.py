from commons.common_import import *
global ParentDataset
EvalFuncDict.clear()


TaskDescription = """\
请你完成论文学科分类任务。\
给定一个论文片段，\
请你对其所属学科领域进行分类。
一共有67个类别，分别为（使用逗号分割）：
纺织科学与工程，药学，动力工程及工程热物理，哲学，地理学，军事学，\
材料科学与工程，核科学与技术，民族学，体育学，政治学，食品科学与工程，历史学，\
矿业工程，基础医学/临床医学，农业工程，测绘科学与技术，控制科学与工程，\
公共管理，地球物理学，法学，化学/化学工程与技术，土木工程，数学，机械工程，\
大气科学，石油与天然气工程，水产，图书馆、情报与档案管理，理论经济学，\
应用经济学，生物学/生物科学与工程，园艺学，新闻传播学，工商管理，口腔医学，\
计算机科学与技术，信息与通信工程，艺术学，农林经济管理，力学，海洋科学，\
环境科学与工程，水利工程，交通运输工程，中医学/中药学，电气工程，\
兵器科学与技术，林学/林业工程，船舶与海洋工程，光学工程，冶金工程，建筑学，\
作物学，地质学/地质资源与地质工程，心理学，畜牧学/兽医学，物理学，\
公共卫生与预防医学，教育学，电子科学与技术，天文学，社会学，植物保护，\
农业资源利用，中国语言文学，航空宇航科学与技术
请你直接输出67个类别中的一个，不要输出多余文字。
"""
QuestionPrompt = """\
内容：{content}
类别：{answer}
"""


class Dataset(ParentDataset):
    Description = {
        "name": "CSL - dcp"
    }
    available_classes = [
        "纺织科学与工程", "药学", "动力工程及工程热物理", "哲学", "地理学",
        "军事学", "材料科学与工程", "核科学与技术", "民族学", "体育学",
        "政治学", "食品科学与工程", "历史学", "矿业工程", "基础医学/临床医学",
        "农业工程", "测绘科学与技术", "控制科学与工程", "公共管理", "地球物理学",
        "法学", "化学/化学工程与技术", "土木工程", "数学", "机械工程", "大气科学",
        "石油与天然气工程", "水产", "图书馆、情报与档案管理", "理论经济学",
        "应用经济学", "生物学/生物科学与工程", "园艺学", "新闻传播学",
        "工商管理", "口腔医学", "计算机科学与技术", "信息与通信工程", "艺术学",
        "农林经济管理", "力学", "海洋科学", "环境科学与工程", "水利工程",
        "交通运输工程", "中医学/中药学", "电气工程", "兵器科学与技术",
        "林学/林业工程", "船舶与海洋工程", "光学工程", "冶金工程", "建筑学",
        "作物学", "地质学/地质资源与地质工程", "心理学", "畜牧学/兽医学",
        "物理学", "公共卫生与预防医学", "教育学", "电子科学与技术", "天文学",
        "社会学", "植物保护", "农业资源利用", "中国语言文学",
        "航空宇航科学与技术"
    ]

    def analyse_file(self, fp: TextIO, sample_num: Optional[int] = None) -> List[Tuple[Any, Any]]:
        """
        :param fp: 带读取数据集的指针，以文本模式打开，utf-8编码
        :param sample_num: 希望从数据集中读取样例数目，None表示全部读取
        :return: 格式化后的样例列表。每个样例分为两部分，一部分用来生成prompt，一部分为标准答案，每部分具体格式不限制。
        """
        if sample_num == None:
            sample_num = Metric.HUGE_POSITIVE
        dataset = []
        while line := fp.readline():
            if len(dataset) > sample_num:
                break
            _, content, keywords = line.strip().split('\t')
            dataset.append(((content, ), keywords))
        return dataset

    def fill_prompt(self, sample: Any, answer: Any) -> Dict[str, str]:
        """
        :param sample: 一个样例
        :param answer: 该样例对应的答案
        :return: 文件开头Prompt模板中有一些未填充的变量，这里需返回一个字典，以这些变量名称为键，以该样例的信息为值
        """
        content, *_ = sample
        return {
            'content': content,
            'answer': answer
        }

    def validate(self, llm_answer: str, std_answer: Any) -> ScoreType:
        """
        :param llm_answer: 大模型给出的答案
        :param std_answer: 标准答案
        :return: 对模型给出的答案的评分，一般为布尔值或分数，也可以为其他
        注：该函数仅用于评判llm答案的准确性，其他指标请使用 EvalFunc 装饰器添加（参见下面的函数）。
        """
        llm_answer = clean_newlines(llm_answer)
        lines = llm_answer.split('\n')
        score = 0
        for line in lines[::-1]:
            hits = [(c in line) for c in self.available_classes]
            if sum(hits) == 1:
                idx = hits.index(True)
                ans = self.available_classes[idx]
                score = int(ans == std_answer)
                break
        self.info = None
        return score
