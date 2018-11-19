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
    'CORDENONSI_YAP_CONSERVED_SIGNATURE',
    'GO_HIPPO_SIGNALING',
    'Hippo Pathway Genes',
    'IPA_YAP1_DN',
    'IPA_YAP1_UP',
    'REACTOME_SIGNALING_BY_HIPPO',
    'REACTOME_YAP1_AND_WWTR1_TAZ_STIMULATED_GENE_EXPRESSION',
    'YAP signature based on cell HEK293 in paper Cell 150, 780–791, August 17, 2012',
    'YAP signature based on cell NIH3T3_MCD10A in paper GENES & DEVELOPMENT 22:1962–1971 2008',
    'YAP signature based on cell SCC2 Oral Cancer in paper Mol Cancer Res; 13(6) June 2015',
    'YAP signature based on mechanism',
    'YAP.24_DN',
    'YAP.24_UP',
    'YAP.Breast_HMLE.24_DN',
    'YAP.Breast_HMLE.24_UP',
    'YAP.Breast_HMLE_DN',
    'YAP.Breast_HMLE_Lung_SALE.24_DN',
    'YAP.Breast_HMLE_Lung_SALE.24_UP',
    'YAP.Breast_HMLE_Lung_SALE_DN',
    'YAP.Breast_HMLE_Lung_SALE_UP',
    'YAP.Breast_HMLE_Skin_PMEL.24_DN',
    'YAP.Breast_HMLE_Skin_PMEL.24_UP',
    'YAP.Breast_HMLE_Skin_PMEL_DN',
    'YAP.Breast_HMLE_Skin_PMEL_UP',
    'YAP.Breast_HMLE_UP',
    'YAP.mt.24_DN',
    'YAP.mt.24_UP',
    'YAP.mt.Breast_HMLE.24_DN',
    'YAP.mt.Breast_HMLE.24_UP',
    'YAP.mt.Breast_HMLE_DN',
    'YAP.mt.Breast_HMLE_Lung_SALE.24_DN',
    'YAP.mt.Breast_HMLE_Lung_SALE.24_UP',
    'YAP.mt.Breast_HMLE_Lung_SALE_DN',
    'YAP.mt.Breast_HMLE_Lung_SALE_UP',
    'YAP.mt.Breast_HMLE_Skin_PMEL.24_DN',
    'YAP.mt.Breast_HMLE_Skin_PMEL.24_UP',
    'YAP.mt.Breast_HMLE_Skin_PMEL_DN',
    'YAP.mt.Breast_HMLE_Skin_PMEL_UP',
    'YAP.mt.Breast_HMLE_UP',
    'YAP.mt.Lung_SALE.24_DN',
    'YAP.mt.Lung_SALE.24_UP',
    'YAP.mt.Lung_SALE_DN',
    'YAP.mt.Lung_SALE_Skin_PMEL.24_DN',
    'YAP.mt.Lung_SALE_Skin_PMEL.24_UP',
    'YAP.mt.Lung_SALE_Skin_PMEL_DN',
    'YAP.mt.Lung_SALE_Skin_PMEL_UP',
    'YAP.mt.Lung_SALE_UP',
    'YAP.mt_DN',
    'YAP.mt_UP',
    'YAP1_DN',
    'YAP1_UP',
    'YAP_DN',
    'YAP_UP',
)

N_JOB = 1

TARGET_ASCENDING = None

EXTREME_FEATURE_THRESHOLD = 24

N_SAMPLING = 10

N_PERMUTATION = 10

TARGET_TYPE = 'binary'

PLOT_STD = 2

PATH_DICT = _make_path_dict()
