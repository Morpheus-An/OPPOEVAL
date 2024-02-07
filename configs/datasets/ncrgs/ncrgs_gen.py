# fr
from oppoeval.datasets import ncrgsDataset
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.utils.text_postprocessors import first_option_postprocess

reader_cfg = dict(
    input_columns=['context', 'question', 'A', 'B', 'C', 'D'],
    output_column='label',
    test_split='test'
)

infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(
                    role="HUMAN",
                    prompt="{context}\n{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n答案:"
                )
            ], ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer),
)

eval_cfg = dict(
    evaluator=dict(type=AccEvaluator),
    pred_role="BOT",
    pred_postprocessor=dict(type=first_option_postprocess, options='ABCD'),
)


ncrgs_datasets = [
    dict(
        type=ncrgsDataset,
        path='oppodata/zh-spec/ncr-gs',
        reader_cfg=reader_cfg,
        infer_cfg=infer_cfg,
        eval_cfg=eval_cfg
    )
]
