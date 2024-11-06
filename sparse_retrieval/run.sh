# ./clean.sh


###########################################################################
# We first convert WT2G files into the jsonl format required by pyserini. #
###########################################################################
if test -e "./data/collection/collection.jsonl"; then
        echo "already transformed"
else
        python codes/convert_wt2g_to_jsonl.py
fi


##################################################################
# Secondly, we can build index for our WT2G corpus(247491 docs). #
##################################################################
if test -e "./indexes/collection/"; then
        echo "indexed"
else
        ./codes/build_index.sh

fi
##########################################################
# Then, search and store result in the trec_eval format. #
##########################################################
python codes/main.py --query ../data/topics.401-440.txt --method bm25 --output runs/bm25_40.run
python codes/main.py --query ../data/topics.401-440.txt --method dir --output runs/dir_40.run
python codes/main.py --query ../data/topics.401-440.txt --method jm --output runs/jm_40.run


##############################
# Lastly, do the evaluation. #
##############################
echo "BM25 result on 40 queries"
perl trec_eval.pl ../data/qrels.401-440.txt runs/bm25_40.run
echo "Direchlet Smoothing result on 40 queries"
perl trec_eval.pl ../data/qrels.401-440.txt runs/dir_40.run
echo "Jelinek-Merver Smoothing result on 40 quries"
perl trec_eval.pl ../data/qrels.401-440.txt runs/jm_40.run


############################
# Part2: Learning to Rank. #
############################
python codes/main.py --query ../data/topics.441-450.txt --method bm25 --output runs/bm25_10.run
python codes/main.py --query ../data/topics.441-450.txt --method dir --output runs/dir_10.run
python codes/main.py --query ../data/topics.441-450.txt --method jm --output runs/jm_10.run
echo "BM25 result on 10 queries"
perl trec_eval.pl ../data/qrels.441-450.txt runs/bm25_10.run
echo "Direchlet Smoothing result on 10 queries"
perl trec_eval.pl ../data/qrels.441-450.txt runs/dir_10.run
echo "Jelinek-Merver Smoothing result on 10 quries"
perl trec_eval.pl ../data/qrels.441-450.txt runs/jm_10.run
echo "Learning to Rank result"

python codes/random_forest.py
perl trec_eval.pl ../data/qrels.441-450.txt runs/random_forest_10.run
