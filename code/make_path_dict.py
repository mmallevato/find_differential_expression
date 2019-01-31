from os import listdir

from ccal import establish_path


def make_path_dict(setting):

    path_dict = dict(
        kallisto_directory_path="../output/kallisto",
        gene_x_sample_file_path="../output/gene_x_sample.processed.tsv",
        target_x_sample_file_path="../output/target_x_sample.tsv",
        differentially_expressed_gene_directory_path="../output/differentially_expressed_gene",
        gene_set_x_sample_file_path="../output/gene_set_x_sample.tsv",
        differentially_expressed_gene_set_directory_path="../output/differentially_expressed_gene_set",
        hill_plot_directory_path="../output/hill_plot",
        expanded_gene_set_directory_path="../output/expanded_gene_set",
        highlight_directory_path="../output/highlight",
        mountain_plot_directory_path="../output/mountain_plot",
    )

    path_dict.update(
        gene_set_file_paths=tuple(
            "{}/{}".format(setting["gene_set_directory_path"], file_name)
            for file_name in sorted(listdir(setting["gene_set_directory_path"]))
        )
    )

    for path_name, path in path_dict.items():

        if "directory" in path_name:

            establish_path(path, "directory")

    return path_dict
