import json

def save_paragraph(paragraph_dict, output_file):
    with open(output_file, 'w') as file:
        json.dump(paragraph_dict, file, indent=4)
        
def create_paragraph_list(file_path):
    paragraph_list = []

    with open(file_path, 'r') as file:
        current_paragraph = ''
        for line in file:
            if line.strip():  # Check if line is not empty
                current_paragraph += line
            else:
                # Split paragraph into input and target
                lines = current_paragraph.strip().split('\n')
                input_text = lines[0]
                target_text = '\n'.join(lines[1:])
                
                # Add input and target to list
                paragraph_list.append({'input': input_text, 'target': target_text})
                
                # Reset current_paragraph for the next paragraph
                current_paragraph = ''

        # Add the last paragraph
        if current_paragraph:
            lines = current_paragraph.strip().split('\n')
            input_text = lines[0]
            target_text = '\n'.join(lines[1:])
            paragraph_list.append({'input': input_text, 'target': target_text})

    return paragraph_list

# Example usage
file_path = 'ghazals.txt'
paragraph_list = create_paragraph_list(file_path)
save_paragraph(paragraph_list,"list.txt")
