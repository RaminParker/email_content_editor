import yaml
import re
import os

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

    city = "Bamberg"

    if city == "Bamberg":
        email_list = ['updated_signup.yaml', 'updated_signup-waitlist.yaml', 'updated_signup-waitlist.yaml', 'updated_reminder.yaml',
                    'updated_gewinspiel.yaml', 'updated_allocation-reminder.yaml', 'updated_allocation-ready.yaml',
                    'updated_allocation-failed.yaml', 'updated_allocation-cancel-course.yaml', 'updated_activation.yaml']
    elif city == 'Würzburg':
        email_list = ['updated_allocation-cancel-course.yaml', 'updated_allocation-failed.yaml', 'updated_allocation-ready.yaml', 
                    'updated_allocation-ready-temp-correction.yaml', 'updated_signup.yaml', 'updated_signup-waitlist.yaml', 'updated_end.yaml']
    else:
        print("No list defined!")
        exit(1)
    
    # Create the output directory if it doesn't exist
    output_dir = f'emails_updated/{city}'
    os.makedirs(output_dir, exist_ok=True)

    for file in email_list:
        input_file = os.path.join('emails_updated', city, file)
        try:
            clean_text = extract_clean_text(input_file)
            
            # Create output filename
            output_filename = f'clean_{os.path.splitext(file)[0]}.txt'
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(clean_text)
            print(f"Processed and saved: {output_path}")
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {input_file}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {input_file}: {e}")

print("Script execution completed.")