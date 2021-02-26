from nlgeval import NLGEval

from collections import defaultdict
from argparse import ArgumentParser
import numpy as np
import copy
import sys
import pathlib

def eval(gen_file, src_gen_file, src_ref_file, tgt_ref_file, name, verbose=False):
    """                                                                                                                                                                              
        Given an aligned generation pair of files, calculate automatic metrics' scores (using Maluba project) for that aligned reference.                                            
        Output files into name directory.                                                                                                                                            
    """

    pathlib.Path(name).mkdir(parents=True, exist_ok=True)


    ref_pairs = []
    with open(src_ref_file, encoding='utf-8') as infile:
        for line in infile:
            pair = {}
            pair['sentence'] = line[:-1].lower()
            ref_pairs.append(pair)

    with open(tgt_ref_file, encoding='utf-8') as infile:
        cnt = 0
        for line in infile:
            ref_pairs[cnt]['question'] = line[:-1].replace('\r', '').replace('?', '').strip().lower()
            cnt += 1

    gen_pairs = []
    with open(src_gen_file, encoding='utf-8') as infile:
        for line in infile:
            pair = {}
            pair['sentence'] = line[:-1].lower()
            gen_pairs.append(pair)

    with open(gen_file, encoding='utf-8') as infile:
        cnt = 0
        for line in infile:
            gen_pairs[cnt]['hypothesis'] = line[:-1].replace('\r', '').replace('?', '').strip().lower()
            cnt += 1
         
 
    gen = defaultdict(lambda: [])
    ref = defaultdict(lambda: [])

    for pair in gen_pairs[:]:
        key = pair['sentence']
        gen[key].append(pair['hypothesis'])

    for pair in ref_pairs[:]:
	      key = pair['sentence']
        ref[key].append(pair['question'])


    if verbose:
        count = 0
	      print('Qs for sentences w/o reference:')
        for k in gen.keys():
            if k not in ref:
		            print(k.encode('utf-8'))
                count += len(gen[k])
                for q in gen[k]:
                    print('\t\t{}'.format(q))
        if count>0:
            print('WARNING: Total number of questions not evaluated: ' + str(count))

    if verbose:
        print('Got a reference of size: ' + str(sum(len(v) for k,v in ref.items())))
        print('Number of generated questions: ' + str(sum(len(v) for k,v in gen.items())))
        print('Starting...')


    nlgeval = NLGEval()
    metrics = ['Bleu_1', 'Bleu_2', 'Bleu_3', 'Bleu_4', 'METEOR', 'ROUGE_L', 'SkipThoughtCS', 'EmbeddingAverageCosineSimilairty', 'VectorExtremaCosineSimilarity', 'GreedyMatchingSco\
re']

    results = {}
    resultsSolo = {}
    
    
    for m in metrics:
        results[m] = 0
        resultsSolo[m] = []

    srcSen = ref.keys()

    countGenUsed = 0
    countRefUsed = 0
    for id in srcSen:
        countRefUsed += 1
        if id not in gen:
            continue;
        hypo = gen[id]
        r = ref[id]
        countGenUsed += len(hypo)

	      if verbose:
            print('Computing sentence ' + str(countRefUsed))

	      for h in hypo:
            metrics_dict = nlgeval.compute_individual_metrics(r, h)
            for m in metrics:
                results[m] += metrics_dict[m]
                resultsSolo[m].append(metrics_dict[m])
        if verbose:
            print('Parsed questions: ' + str(countGenUsed))


    if verbose:
        print('Writting files to ' + name + '...')

    for m in metrics:
        with open(name+'/'+m, 'w') as f:
            f.write(m+'\t\t\t\n')
            f.write(str(results[m]/countGenUsed)+'\t\t\t\n')
            f.write(m+'\t\t\t\n')
            f.write(str(countGenUsed)+'\t\t\t\n')

      	with open(name+'/'+m+'IndScores', 'w') as f:
            for sc in resultsSolo[m]:
                f.write(str(sc)+'\n')
          
          
  

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-gen", "--gen_file", dest="gen_file", help="Output questions file.")
    parser.add_argument("-src_gen", "--src_gen_file", dest="src_gen_file", help="Output source sentences file aligned with gen_file.")
    parser.add_argument("-src_ref", "--src_ref_file", dest="src_ref_file", default="sentencessReferenceAligned.txt", help="Reference sentences file.")
    parser.add_argument("-tgt_ref", "--tgt_ref_file", dest="tgt_ref_file", default="questionsReferenceAligned.txt", help="Reference questions file.")
    parser.add_argument("-name", "--name", dest="name", default="example", help="Destination folder name.")
    parser.add_argument("-v", "--verbose", dest="verbose", default=False, action="store_true", help="Print some info to stout.")

    args = parser.parse_args()

    eval(args.gen_file, args.src_gen_file, args.src_ref_file, args.tgt_ref_file, args.name, args.verbose)


