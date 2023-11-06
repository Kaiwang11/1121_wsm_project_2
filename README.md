# Demo Repo for 1121_wsm_proj2

Please download WT2G corpus file through the [link](https://drive.google.com/file/d/1EcWOzoftB1BXSntAlJlLC-2I6KY3AgyJ/view)  

### File Tree
<img src="img/file_tree.png" alt="file_tree" width="300"/>

### Part1: Language Model (40 queries)
We have 3 ranking function:  
1. bm25
2. dirichlet smoothing
3. jelinek-mercer smoothing

To achieve these methods through pyserini, you have to modify [pyserini/search/lucene/_searcher.py](https://github.com/castorini/pyserini/blob/master/pyserini/search/lucene/_searcher.py):  
![image info](img/qljm.png)

### Part2: Learning to Rank
Use part1 results to train a ML model, then test on new 10 queries.  
Example: please refer to sparse_retrieval/codes/random_forest.py

### Usage
```bash
./run.sh
```
