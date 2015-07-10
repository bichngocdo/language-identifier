__author__ = 'sapphire'

import os
import os.path

import langid.ngramprofile as ngramprofile


def train_language_models(input_folder, output_folder=None):
    assert os.path.isdir(input_folder)
    if output_folder is None:
        output_folder = input_folder
    assert os.path.isdir(output_folder)

    # Read all files in the input folder
    training_paths = list()
    model_paths = list()
    languages = list()
    for name in os.listdir(input_folder):
        training_path = os.path.join(input_folder, name)
        if os.path.isfile(training_path):
            language = os.path.splitext(name)[0]
            languages.append(language)
            training_paths.append(training_path)
            model_paths.append(os.path.join(output_folder, language + '.yaml'))

    # Build language models
    for data, model, language in zip(training_paths, model_paths, languages):
        with open(data, 'r') as f:
            print 'Process file', data
            profile = ngramprofile.build_profile(f)
            profile.language = language
            ngramprofile.dump_profile(profile, model)


if __name__ == '__main__':
    train_language_models('training', 'models')
