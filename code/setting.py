from _make_path_dict import _make_path_dict

FASTQ_INPUTS = (
    ("../data/fastq/NC1_1.fq.gz", "../data/fastq/NC1_2.fq.gz"),
    ("../data/fastq/NC2_1.fq.gz", "../data/fastq/NC2_2.fq.gz"),
    ("../data/fastq/NC3_1.fq.gz", "../data/fastq/NC3_2.fq.gz"),
    ("../data/fastq/NM1_1.fq.gz", "../data/fastq/NM1_2.fq.gz"),
    ("../data/fastq/NM2_1.fq.gz", "../data/fastq/NM2_2.fq.gz"),
    ("../data/fastq/NM3_1.fq.gz", "../data/fastq/NM3_2.fq.gz"),
    ("../data/fastq/WC1_1.fq.gz", "../data/fastq/WC1_2.fq.gz"),
    ("../data/fastq/WC2_1.fq.gz", "../data/fastq/WC2_2.fq.gz"),
    ("../data/fastq/WC3_1.fq.gz", "../data/fastq/WC3_2.fq.gz"),
    ("../data/fastq/WM1_1.fq.gz", "../data/fastq/WM1_2.fq.gz"),
    ("../data/fastq/WM2_1.fq.gz", "../data/fastq/WM2_2.fq.gz"),
    ("../data/fastq/WM3_1.fq.gz", "../data/fastq/WM3_2.fq.gz"),
)

REFERENCE_CDNA_FASTA_FILE_PATH = "../data/Homo_sapiens.GRCh38.cdna.all.fa.gz"

GENE_TO_PEEK = (
    "ABCG2",
    "BMI1",
    "CD34",
    "CD44",
    "CTNNB1",
    "EPAS1",
    "EZH2",
    "HIF1A",
    "KDM5B",
    "KLF4",
    "LGR5",
    "MYC",
    "NANOG",
    "NES",
    "NOTCH1",
    "POU5F1",
    "PROM1",
    "SOX2",
    "TWIST1",
    "ZFP42",
    "ZSCAN4",
)

GENE_SET_TO_PEEK = (
    "Cancer Stem Cell",
    "BENPORATH_ES_CORE_NINE",
    "BENPORATH_ES_WITH_H3K27ME3",
    "HOEBEKE_LYMPHOID_STEM_CELL_UP",
    "IVANOVA_HEMATOPOIESIS_STEM_CELL_AND_PROGENITOR",
    "MIKKELSEN_IPS_LCP_WITH_H3K4ME3",
    "MIKKELSEN_IPS_WITH_HCP_H3K27ME3",
    "GOTZMANN_EPITHELIAL_TO_MESENCHYMAL_TRANSITION_UP",
    "HALLMARK_NOTCH_SIGNALING",
    "HALLMARK_TGF_BETA_SIGNALING",
    "HALLMARK_E2F_TARGETS",
    "HALLMARK_WNT_BETA_CATENIN_SIGNALING",
    "BIOCARTA_WNT_PATHWAY",
    "PRC2_EZH2_UP.V1_UP",
    "E2F3_UP.V1_UP",
    "HINATA_NFKB_TARGETS_KERATINOCYTE_UP",
    "TIAN_TNF_SIGNALING_VIA_NFKB",
    "RODRIGUES_THYROID_CARCINOMA_POORLY_DIFFERENTIATED_UP",
    "RODRIGUES_THYROID_CARCINOMA_POORLY_DIFFERENTIATED_DN",
    "MA_MYELOID_DIFFERENTIATION_UP",
    "ADDYA_ERYTHROID_DIFFERENTIATION_BY_HEMIN",
)

N_JOB = 1

TARGET_ASCENDING = None

EXTREME_FEATURE_THRESHOLD = 24

N_SAMPLING = 10

N_PERMUTATION = 10

TARGET_TYPE = "binary"

PLOT_STD = 2.4

PATH_DICT = _make_path_dict()
