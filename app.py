import streamlit as st
import yaml
import re
import io

def extract_email_content(yaml_data):
    email_content = {}
    
    # Extract basic information
    email_content['type'] = yaml_data.get('type', '')
    email_content['id'] = yaml_data.get('id', '')
    email_content['subject'] = yaml_data.get('subject', '')
    email_content['description'] = yaml_data.get('description', '')
    
    # Extract content from layout
    full_text = ""
    for component in yaml_data.get('layout', []):
        if component['type'] == 'layout/email/main-content':
            full_text += f"{component['props'].get('title', '')}\n\n"
            full_text += f"{component['props'].get('text', '')}\n\n"
    
    email_content['full_text'] = full_text
    
    return email_content

def update_yaml_content(yaml_data, updated_content):
    # Update basic information
    yaml_data['type'] = updated_content['type']
    yaml_data['id'] = updated_content['id']
    yaml_data['subject'] = updated_content['subject']
    yaml_data['description'] = updated_content['description']
    
    # Update the 'text' field in main-content components
    for component in yaml_data.get('layout', []):
        if component['type'] == 'layout/email/main-content':
            component['props']['text'] = updated_content['full_text']
    
    return yaml_data

def main():
    st.title("Email Content Editor")

    # Add a description for the app
    st.markdown(
        """
        **Nutzungshinweis:**
        1. Upload a file containing email data.
        2. This app will extract and display the main content.
        3. Do not edit the field **ID**.
        4. Only edit the field **Full Text**.
        5. Keep in mind that the text is writen in [markdown](https://markdown-it.github.io/)
        6. Keep all global variables as they are.
        7. Once you're done, click **Save Changes** to update the file.
        8. Download the modified YAML using the download button.
        """
    )

    uploaded_file = st.file_uploader("Choose a YAML file", type="yaml")

    if uploaded_file:
        st.subheader(f"File: {uploaded_file.name}")
        
        # Read YAML content
        yaml_content = yaml.safe_load(uploaded_file)
        
        # Extract email content
        email_content = extract_email_content(yaml_content)
        
        # Display and allow editing of basic information
        email_content['id'] = st.text_input("ID", email_content['id'])
        email_content['full_text'] = st.text_area("Full Text", email_content['full_text'], height=300)
        
        # Save button
        if st.button(f"Save Changes"):
            # Update YAML content with edited information
            updated_yaml = update_yaml_content(yaml_content, email_content)
            
            # Convert updated YAML to string
            yaml_str = yaml.dump(updated_yaml, allow_unicode=True, sort_keys=False)
            
            # Provide download link for updated YAML
            st.download_button(
                label=f"Download updated {uploaded_file.name}",
                data=yaml_str,
                file_name=f"updated_{uploaded_file.name}",
                mime="application/x-yaml"
            )

if __name__ == "__main__":
    main()
