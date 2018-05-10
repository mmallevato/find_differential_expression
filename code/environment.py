import os

import ccal
import pandas as pd


def make_match_panels(target_x_sample, feature_x_sample, n_job,
                      extreme_feature_threshold, n_sampling, n_permutation,
                      to_peek, title_prefix, directory_path):

    for index, target in target_x_sample.iterrows():

        print(index)

        to_keep = target != -1

        target = target[to_keep]

        file_path_prefix = '{}/{}'.format(directory_path, index)

        scores_file_path = '{}.match_panel.tsv'.format(file_path_prefix)

        if os.path.isfile(scores_file_path):

            scores = pd.read_table(scores_file_path, index_col=0)

        else:

            scores = None

        if target.unique().size == 2:

            target_type = 'binary'

        elif 2 < target.unique().size:

            target_type = 'categorical'

        title = '{}{}'.format(title_prefix, index)

        scores = ccal.make_match_panel(
            target,
            feature_x_sample,
            target_ascending=True,
            scores=scores,
            n_job=n_job,
            extreme_feature_threshold=extreme_feature_threshold,
            n_sampling=n_sampling,
            n_permutation=n_permutation,
            title=title,
            target_type=target_type,
            file_path_prefix=file_path_prefix)

        common_indices = feature_x_sample.index & scores.index & set(to_peek)

        if 0 < len(common_indices):

            ccal.make_match_panel(
                target,
                feature_x_sample.loc[common_indices],
                scores=scores.loc[common_indices],
                target_ascending=True,
                extreme_feature_threshold=None,
                title=title,
                target_type=target_type)
