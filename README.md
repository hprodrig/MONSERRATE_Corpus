# MONSERRATE Corpus

MONSERRATE is a dataset specifically created to automatically evaluate Question Generation systems. It has, on average, 26 questions associated to each source sentence, attempting to be an "exhaustive" reference.

## But why?

Despite the growing interest in Question Generation, evaluating these systems remains notably difficult. Many authors rely on metrics like BLEU or ROUGE instead of relying on manual evaluations, as their computation is mostly free. However, corpora generally used as reference is very incomplete, containing just a couple of hypotheses per source sentence. For example, the most used and created large datasets, SQuAD and MS Marco, only have, at most, a single reference question per source sentence. 

## Dataset

In [corpus](corpus) you can find the full dataset, brokedown in the following files:

* Source sentences (73): sourceSentences.txt;
* Full reference (over 1900 questions): fullReference.txt;
* Reference sentences and questions aligned in separate files: referenceSentences.txt, referenceQuestions.txt.

Examples:

Sentence | Questions
----- | -----
When you buy the ticket, you will receive a map which allows you to go around easily by yourself. | How can I get a map? <br /> How can I get a map of the palace? <br /> What does one receive upon buying the ticket? <br /> What will you receive when you buy a ticket? <br /> Why is a map useful?
The estate of Monserrate was rented by Gerard de Visme (1789), a wealthy English merchant, who built a house there in the neo-Gothic style. | Who was Gerard de Visme? <br /> What did Gerard de Visme build? <br /> What was Gerard de Visme's profession? <br /> What was Gerard de Visme's nationality? <br /> Was the estate of Monserrate ever rented? <br /> What style was Gerard de Visme's house? <br /> When did Gerard de Visme rent the estate?

## Benchmark

We benchmarked three available state of the art systems, each with a different approach to the problem of QG:

* H&S: Heilman, M. and Smith, N. (2010);
* D&A: Du, X. et al (2017);
* GEN: Rodrigues, H. et al (2018).


System | ROUGE | METEOR | BLEU1 | BLEU4 | EACS | GMS | STCS | VECS
:------ | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----:
H&S | **69.00** | 46.38 | 83.71 | **45.56** | 92.51 | **86.11** | 73.26 | 77.92
D&A | 63.71  | 37.58  | 77.40 | 26.63 | **92.52** | 85.51 |  74.47 | 77.54
GEN (args) | 65.81 | **46.44** | 81.80 | 40.61 | 92.25 | 85.86 | 71.17 | **80.89**


Contact us with your results to appear on the table!

## Usage

We used [Maluba Project](https://github.com/Maluuba/nlg-eval) in our experiments. You can find a [script](script) (requires Maluba instalation) to automatically evaluate your system output on **MONSERRATE**. But the dataset is also publicly available to be used as you see fit.

## Citation

TBD

## Acknowledgements
Hugo Rodrigues was supported by the Carnegie Mellon-Portugal program (SFRH/ BD/51916/2012). This work was also supported by national funds through Fundação para a Ciência e Tecnologia (FCT) with reference UIDB/50021/2020.

## Contact Information

Hugo Rodrigues: hugo`.`p`.`rodrigues`@`tecnico.ulisboa.pt
