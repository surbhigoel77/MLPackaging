# MLPackaging


Use the following command to copy the template:

`copier copy path-to-ml-template path-to-new-ml-project`



ml-template/
├── copier.yml                # Template configuration file
├── README.md.tmpl            # Template for README.md
├── data/                     # Folder for data storage
│   └── .gitkeep              # Empty file to keep the folder in git
├── notebooks/                # Jupyter notebooks
│   └── example_notebook.ipynb # Example notebook
├── src/                      # Source code for ML project
│   ├── data_preprocessing.py # Data preprocessing script
│   ├── train_model.py        # Model training script
│   ├── evaluate_model.py     # Model evaluation script
├── models/                   # Folder to store trained models
│   └── .gitkeep
├── tests/                    # Folder for test cases
│   └── test_training.py      # Example test case for training
├── config/                   # Configuration files for the project
│   └── config.yaml.tmpl      # Template for configuration (YAML format)
├── requirements.txt.tmpl     # Template for Python dependencies
└── .gitignore.tmpl           # Template for .gitignore
