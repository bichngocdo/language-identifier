# An N-Gram Based Language Identifier
This project implements the approach described on: [William B. Cavnar and John M. Trenkle - **N-Gram-Based Text Categorization**](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.9367).

Main modules are in package `langid`:
* `ngramprofile.py`: language profile class and methods
* `utils.py`: helper functions to iterate n-grams in a file

### Sample Codes
Sample codes are in folder *sample*. This folder includes:

1. Data:
  * Data were downloaded from [Leipzig Corpora](http://corpora2.informatik.uni-leipzig.de/download.html) in 4 languages: English, German, Italian and Spanish.
  * List of used data:
    - [eng-uk_web_2002_30K](http://corpora2.informatik.uni-leipzig.de/downloads/eng-uk_web_2002_30K-text.tar.gz)
    - [deu_web_2002_30K](http://corpora2.informatik.uni-leipzig.de/downloads/deu_web_2002_30K-text.tar.gz)
    - [ita_web_2011_30K](http://corpora2.informatik.uni-leipzig.de/downloads/ita_web_2011_30K.tar.gz)
    - [spa_wikipedia_2011_30K](http://corpora2.informatik.uni-leipzig.de/downloads/spa_wikipedia_2011_30K-text.tar.gz)
  * The *sentence* file in each archive was split into 20K chunks, the first 10 chunks were used as testing data, while the 11th chunk was used as training data.
  * The language code is the name of each training file and is the prefix of each testing file.
2. Codes:
  * `train_languages.py`: Read each training file in folder *sample/training* and write the corresponding model to folder *sample/models*
  * `test_languages.py`: Read each testing file in folder *sample/testing* and report the accuracy
3. Result: The accuracy of this dataset is `1.0`.
