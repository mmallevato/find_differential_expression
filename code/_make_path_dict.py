from os import listdir

from ccal import establish_path


def _make_path_dict():

    gene_set_directory_path = '../data/gene_set'

    path_dict = dict(
        enst_file_path='../data/enst.tsv',
        sample_id_sample_name_file_path='../data/sample_id_sample_name.tsv',
        gene_set_directory_path='../data/gene_set',
        kallisto_directory_path='../output/kallisto',
        gene_x_sample_file_path='../output/gene_x_sample__processed.tsv',
        target_x_sample_file_path='../output/target_x_sample.tsv',
        differentially_expressed_gene_directory_path=
        '../output/differentially_expressed_gene',
        gene_set_x_sample_file_path='../output/gene_set_x_sample.tsv',
        differentially_expressed_gene_set_directory_path=
        '../output/differentially_expressed_gene_set',
        hill_plot_directory_path='../output/hill_plot',
        expanded_gene_set_directory_path='../output/expanded_gene_set',
        highlight_directory_path='../output/highlight',
        mountain_plot_directory_path='../output/mountain_plot',
    )

    path_dict.update(
        gene_set_file_paths=tuple('{}/{}'.format(
            gene_set_directory_path,
            file_name,
        ) for file_name in sorted(listdir(gene_set_directory_path))))

    for path_name, path in path_dict.items():

        if 'directory' in path_name:

            establish_path(
                path,
                'directory',
            )

    return path_dict
