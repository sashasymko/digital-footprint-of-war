## The Digital Footprint of War: Collection and Analysis of Instagram Data Using Statistical and Machine Learning Methods

Analysis of Instagram communication behavior around the onset of the full-scale Russian invasion of Ukraine on February 24, 2022, using statistical methods and machine learning.

### Research questions:

1. Does the online activity of Ukrainian Instagram users change due to the 2022 full-scale invasion?
2. How long do changes in online interactions last (short-term vs longitudinal effects)?
3. Is there a meaningful correspondence between changes in online activity and major war events?

### Data Access
The data used in this study is not publicly available. Researchers interested in accessing the dataset may contact Dr. Olya Hakobyan at olya.hakobyan@uni-bielefeld.de.

The massive attacks dataset is publicly available on [Kaggle](https://www.kaggle.com/datasets/piterfm/massive-missile-attacks-on-ukraine). Download the following two files from this dataset:

- missile_attacks_daily.csv
- missiles_and_uavs.csv

### Setup
We recommend using Python 3.11.4 for compatibility.

1. **Clone the repository**

```bash
git clone https://github.com/sashasymko/digital-footprint-of-war.git
cd digital-footprint-of-war
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create data folders**

```bash
python setup.py
```

4. **Place your data files**

Once you have access to the datasets, place them as follows:

```
data/
├── raw_data/            ← Ukrainian Instagram data
├── control_data/        ← German WhatsApp data
└── external_data/       ← Files from Kaggle
    ├── missile_attacks_daily.csv
    └── missiles_and_uavs.csv
```

5. **Running the Analysis**

Run notebooks in the following order:

```
01_data_preprocessing/    ← run all notebooks in order (01 → 04)
02_rq1/
    ├── 01_descriptive_analysis/    ← run all notebooks in order (01 → 05)
    ├── 02_clustering/              ← run clustering notebook
    └── 03_classification/          ← run all notebooks in order (01 → 03)
03_rq2/                   ← run all notebooks in order (01 → 03)
04_rq3/                   ← run all notebooks in order (01 → 04)
```
Note: research question folders (02_rq1, 03_rq2, 04_rq3) can be run in any order, but notebooks within each folder must be run in the numbered order.

01_data_preprocessing/ must be run first before any analysis.
