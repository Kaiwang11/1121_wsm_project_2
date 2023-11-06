from pyserini.search.lucene import LuceneSearcher
from tqdm import tqdm
import os


def search(searcher, query, args):
    output = open(args.output, 'w')
        
    print(f'Do {args.method} search...')
    for qid, qtext in tqdm(query.items()):
        hits = searcher.search(qtext, k=args.k)
        for i in range(len(hits)):
            # trec format: qid Q0 docid rank score method
            output.write(f'{qid} Q0 {hits[i].docid} {i+1} {hits[i].score:.5f} {args.method}\n')


'''
### searching methods for debug

def bm25_search(args):
    searcher = LuceneSearcher(args.index)

    # if no set, the default similarity is bm25 with k1=0.9, b=0.4
    searcher.set_bm25(k1=2, b=0.75)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('BM25 Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')

def my_bm25_search(args):
    searcher = LuceneSearcher(args.index)

    searcher.set_my_bm25(k1=2, b=0.75)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('My BM25(k1=2, b=0.75) Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')

def qld_search(args):
    searcher = LuceneSearcher(args.index)

    searcher.set_qld(mu=1000)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('Dirichlet Smoothing Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')

def my_qld_search(args):
    searcher = LuceneSearcher(args.index)

    searcher.set_my_qld(mu=1000)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('My Dirichlet(mu=1000) Smoothing Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')

def qljm_search(args):
    searcher = LuceneSearcher(args.index)

    searcher.set_qljm(jm_lambda=0.8)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('Jelinek-Mercer Smoothing Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')

def my_qljm_search(args):
    searcher = LuceneSearcher(args.index)

    searcher.set_my_qljm(jm_lambda=0.8)
    hits = searcher.search(args.query, args.k)
    
    print()
    print('My Jelinek-Mercer(lambda=0.8) Smoothing Search Results:')
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:12} {hits[i].score:.6f}')
'''
