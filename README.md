
# Sofia - Gender Prediction Model

Sofia - a machine learning model that can predict whether a given name is likely male or female. This model has been trained on the [Gender By Name](https://archive.ics.uci.edu/dataset/591/gender+by+name) dataset from the UCI repo. 

## Project Overview

The goal of this model is to predict the gender (M/F) based on the input name. It uses a straightforward but effective approach, extracting features from the first and last letters of names, and applies a `RandomForestClassifier`model to predict gender.

## Features

- **Data Preprocessing:** The dataset is preprocessed by extracting first and last letter of each name.
- **Model Training:** A `RandomForestClassifier` is trained on the extracted features (namely; first and last letter of each name) to predict the gender of the given name.
- **Web Application:** The model has been integrated into a Streamlit web application which allows users to input a name and get a prediction.
- **Exploratory Data Analysis (EDA):** Visualizations can be created to analyze the distribution of genders, name lengths, and letter frequencies in the dataset.

## Dataset

We use the following attributes:

| Attribute | Description                          | Type   |
|-----------|--------------------------------------|--------|
| Name      | The given name (used for feature extraction) | Text   |
| Gender    | The target label (M = 1, F = 0)     | Binary |

> **Note:**  
> Attributes like *Count* and *Probability* were discarded since they aren't necessary for the current approach.

## Requirements

- python 3.6 or higher
- pandas
- numpy
- scikit-learn
- streamlit
- matplotlib
- seaborn
- joblib

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

## Training the Model

1. Find the root folder and cd into `/scripts`:

```bash
cd your_dir/sofia/scripts
```

2. Run the `model.py` script to train the model and save it:

```bash
python train.py
```

> This will generate a model called `gender_model.pkl` which will be saved to the `model` directory inside the root directory.

## Running the Application

1. Start the Streamlit app:

```bash
streamlit run app.py
```

**Warning**: This won't work if you are inside the `/scripts` directory, make sure you are inside the root (`/sofia`) directory.

**Tip**: You can use the following command to go back to the root directory.

```bash
cd ..
```

> This should automatically open a new window in your **browser** with the app running but if it doesn't; open http://localhost:8501 in your browser.
## Exploratory Data Analysis (EDA)

The EDA script `eda.py` performs analyses on the dataset, including:

- Gender distribution plot
- Name length distribution plot
- Frequency of first and last letters of the names

### Running EDA:

To run the EDA script, simply execute (make sure you are inside the `/scripts` directory):

```bash
python eda.py
```

This will generate the following visualizations in the `eda` directory (inside the root directory):

- `gender_distribution.png`
- `name_length_distribution.png`
- `first_letter_freq.png`
- `last_letter_freq.png`

## File Structure
![file structure](https://cdn.discordapp.com/attachments/1362063228066336838/1362095919771816216/image.png?ex=6801262d&is=67ffd4ad&hm=3fe50d7dde77364c4201e79ff3f55e2bebf1ffde0971ba780b14b77eb01f0c40&)

## License

This project is open source and available under the MIT License.

## Demo

The demo contains the execution of the trainer script as well as the EDA. The web app is also showcased.

[demo.webm](https://private-user-images.githubusercontent.com/207870563/434409163-d30984e3-4330-4364-8e40-3123382d9a65.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ4MTgyMjcsIm5iZiI6MTc0NDgxNzkyNywicGF0aCI6Ii8yMDc4NzA1NjMvNDM0NDA5MTYzLWQzMDk4NGUzLTQzMzAtNDM2NC04ZTQwLTMxMjMzODJkOWE2NS53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDQxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA0MTZUMTUzODQ3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTMwZWUxZGYzM2U5NDA2NzExYTcxNzU4OTVlZmFlNGFlMTNjODNmNTE4MDZmZTA0OTc4MmUyZjllYWQ2ODIzMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.5DZpohaIKghKdE2Aob8FJKlH43EA7mhRoRITUSAujGA)