__author__ = 'sapphire'

import sys
import os.path

import langid.ngramprofile as ngramprofile
import ioutils


def read_models(folder):
    model_paths = ioutils.list_files_only(folder)
    models = list()
    for model_path in model_paths:
        models.append(ngramprofile.load_profile(model_path))
    return models


def identify_language(models, document):
    min_distance = sys.maxint
    best_model = None
    for model in models:
        distance = model.compare(document)
        if distance < min_distance:
            min_distance = distance
            best_model = model
    return best_model.language


def process_batch(models, folder):
    total = 0
    no_correct = 0
    confusion_matrix = dict()

    paths = ioutils.list_files_only(folder)
    for path in paths:
        total += 1
        with open(path, 'r') as f:
            print 'Process file', path,
            document = ngramprofile.build_profile(f)
            document.language = os.path.splitext(os.path.basename(path))[0].split('-')[0]
        predicted_language = identify_language(models, document)
        print 'Predict:', predicted_language, 'expect:', document.language
        if predicted_language == document.language:
            no_correct += 1
        else:
            if document.language not in confusion_matrix:
                confusion_matrix[document.language] = dict()
            confusion_matrix[document.language][predicted_language] = confusion_matrix.get(predicted_language, 0) + 1
    print 'Accuracy:', no_correct * 1.0 / total


if __name__ == '__main__':
    models = read_models('models')
    process_batch(models, 'testing')
