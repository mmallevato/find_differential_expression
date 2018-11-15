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

OVERWRITE = False

GENE_TO_PEEK = (
    'AMOTL2',
    'CTGF',
    'CYR61',
    'DUSP6',
    'TRIB3',
    'CCND1',
)

GENE_SET_TO_PEEK = (
    'IPA_YAP1_UP',
    'YAP.mt.Lung_SALE_Skin_PMEL.24_UP',
    'YAP signature based on mechanism',
)

N_JOB = 1

DROP_NEGATIVE_TARGET = True

TARGET_ASCENDING = None

TARGET_TYPE = 'binary'

EXTREME_FEATURE_THRESHOLD = 24

N_SAMPLING = 10

N_PERMUTATION = 10

PLOT_FEATURES_STD_MAX = 2.4
