from os import listdir

from ccal import establish_path


def make_path_dict(setting):

    path_dict = {}

    for name in (
        "kallisto/",
        "gene_x_sample.processed.tsv",
        "target_x_sample.tsv",
        "differentially_expressed_gene/",
        "gene_set_x_sample.tsv",
        "differentially_expressed_gene_set/",
        "hill_plot/",
        "expanded_gene_set/",
        "highlight/",
        "mountain_plot/",
    ):

        path_dict[name] = "{}/{}".format(setting["output_directory_path"], name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    path_dict["gene_set_file_paths"] = tuple(
        "{}/{}".format(setting["gene_set_directory_path"], name)
        for name in sorted(listdir(setting["gene_set_directory_path"]))
    )

    return path_dict
