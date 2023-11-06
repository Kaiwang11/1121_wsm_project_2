import re
import pandas as pd


def read_title(query_path):
    with open(query_path, 'r', encoding='utf-8') as f:
        texts = f.read()
        qids = re.findall('<num> Number: (.*?)\n', texts)
        titles = re.findall('<title> (.*?)\n\n<desc>', texts)

    query = dict()
    for qid, title in zip(qids, titles):
        query[qid.strip()] = title

    return query


def read_topic(query_path):
    with open(query_path, 'r', encoding='utf-8') as f:
        texts = f.read()
        qids = re.findall('<num> Number: (.*?)\n', texts)
        descs = re.findall('<top>\n\n(.*?)\n</top>', texts, re.S)

    query = dict()
    for qid, desc in zip(qids, descs):
        query[qid.strip()] = desc

    return query


def read_run(run_path):
    colnames = ['qid', 'constant', 'docid', 'rank', 'score', 'method']
    df = pd.read_csv(run_path, sep=" ", header=None, names=colnames)

    method = df['method'][0]
    df.rename(columns={'score': method}, inplace=True)

    df['ids'] = df['qid'].apply(lambda x: str(x)) + "_" + df['docid']
    df = df[['ids', method]]

    return df


def read_qrels(qrels_path):
    colnames = ['qid', 'constant', 'docid', 'relevance']
    df = pd.read_csv(qrels_path, sep=" ", header=None, names=colnames)

    df['ids'] = df['qid'].apply(lambda x: str(x)) + "_" + df['docid']
    df = df[['ids', 'relevance']]

    return df
