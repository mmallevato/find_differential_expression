from os.path import isfile

from ccal import make_match_panel
from pandas import read_table


def make_match_panels(
    target_x_sample,
    feature_x_sample,
    n_job,
    extreme_feature_threshold,
    n_sampling,
    n_permutation,
    title_prefix,
    directory_path,
    reset=False,
):

    for index, target in target_x_sample.iterrows():

        print(index)

        target = target[target != -1]

        file_path_prefix = '{}/{}'.format(
            directory_path, 
            index,
        )

        scores_file_path = '{}.tsv'.format(file_path_prefix)

        if not reset and isfile(scores_file_path):

            scores = read_table(
                scores_file_path, 
                index_col=0,
            )

            scores = scores.loc[feature_x_sample.index]

        else:

            scores = None

        n_target_unique_value = target.unique().size

        if n_target_unique_value == 2:

            target_type = 'binary'

        elif 2 < n_target_unique_value:

            target_type = 'categorical'

        title = '{}{}'.format(
            title_prefix, 
            index,
        )

        make_match_panel(
            target,
            feature_x_sample,
            target_ascending=True,
            scores=scores,
            n_job=n_job,
            extreme_feature_threshold=extreme_feature_threshold,
            n_sampling=n_sampling,
            n_permutation=n_permutation,
            target_type=target_type,
            title=title,
            file_path_prefix=file_path_prefix,
        )
