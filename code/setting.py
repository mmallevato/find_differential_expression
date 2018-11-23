from _make_path_dict import _make_path_dict

FASTQ_INPUTS = (
    (
        '../data/C_1_1.fq.gz',
        '../data/C_1_2.fq.gz',
    ),
    (
        '../data/C_2_1.fq.gz',
        '../data/C_2_2.fq.gz',
    ),
    (
        '../data/C_3_1.fq.gz',
        '../data/C_3_2.fq.gz',
    ),
    (
        '../data/VS_1_1.fq.gz',
        '../data/VS_1_2.fq.gz',
    ),
    (
        '../data/VS_2_1.fq.gz',
        '../data/VS_2_2.fq.gz',
    ),
    (
        '../data/VS_3_1.fq.gz',
        '../data/VS_3_2.fq.gz',
    ),
)

REFERENCE_CDNA_FASTA_FILE_PATH = '../data/Mus_musculus.GRCm38.cdna.all.fa.gz'

GENE_TO_PEEK = (
    'AMOTL2',
    'CTGF',
    'CYR61',
    'DUSP6',
    'TRIB3',
    'CCND1',
)

GENE_SET_TO_PEEK = (
    'YAP signature based on cell NIH3T3_MCD10A in paper GENES & DEVELOPMENT 22:1962–1971 2008',
    'CORDENONSI_YAP_CONSERVED_SIGNATURE',
    'IPA_YAP1_UP',
)

N_JOB = 1

TARGET_ASCENDING = None

EXTREME_FEATURE_THRESHOLD = 24

N_SAMPLING = 10

N_PERMUTATION = 10

TARGET_TYPE = 'binary'

PLOT_STD = 2

PATH_DICT = _make_path_dict()
