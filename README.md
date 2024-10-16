# Email Content Editor

This repository contains two main components: a Streamlit app for editing email content and a Python script for cleaning YAML files containing email templates.

## Files

1. `app.py`: A Streamlit application for editing email content.
2. `yaml_to_plain_text.py`: A Python script for cleaning and extracting text from YAML files.

## Streamlit App (app.py)

The Streamlit app provides a user-friendly interface for editing email content stored in YAML files.

### Features

- Upload YAML files containing email templates
- Extract and display main content from the YAML file
- Edit email content, including ID and full text
- Save changes and download the updated YAML file

### Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Upload a YAML file containing email data.
3. Edit the content as needed (do not modify the ID field).
4. Click "Save Changes" to update the file.
5. Download the modified YAML using the provided button.

Note: The text editor supports Markdown formatting.

## YAML Cleaner (yaml_to_plain_text.py)

This script processes YAML files containing email templates and extracts clean, plain text versions.

### Features

- Removes line continuation backslashes
- Strips Markdown formatting
- Removes extra newlines
- Cleans up leading/trailing whitespace

### Usage - Clean text of emails

1. Place your YAML files in the `emails_updated/` directory.
2. Run the script:
   ```
   python yaml_to_plain_text.py
   ```
3. Clean text versions of the emails will be saved as `.txt` files with the prefix `clean_`.


## Installation

1. Install the required packages:
   ```
   conda env create -f environment_dev.yml
   ```