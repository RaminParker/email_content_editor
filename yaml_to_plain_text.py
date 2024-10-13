import yaml
import re

def extract_clean_text(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    for item in data['layout']:
        if item['type'] == 'layout/email/main-content':
            text = item['props']['text']
            
            # Remove line continuation backslashes
            text = text.replace('\\\n', '')
            
            # Remove Markdown formatting
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)  # Remove links
            text = re.sub(r'\*(.+?)\*', r'\1', text)  # Remove asterisks
            
            # Remove extra newlines
            text = re.sub(r'\n{3,}', '\n\n', text)
            
            # Remove leading/trailing whitespace
            text = text.strip()
            
            return text

    return "Text not found"



if __name__ == "__main__":
    email_list = ['updated_signup-waitlist.yaml', 'updated_signup-waitlist.yaml', 'updated_reminder.yaml',
                  'updated_gewinspiel.yaml', 'updated_allocation-reminder.yaml', 'updated_allocation-ready.yaml',
                  'updated_allocation-failed.yaml', 'updated_allocation-cancel-course.yaml', 'updated_activation.yaml']
    for file in email_list:
        clean_text = extract_clean_text(f'emails_updated/{file}')
        with open(f'clean_{file}.txt', 'w', encoding='utf-8') as file:
            file.write(clean_text)

