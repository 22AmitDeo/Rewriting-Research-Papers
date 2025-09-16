import json
import sys

def txt_to_json_simple(input_file, output_file):
    """
    Convert a text file to JSON format (simple version).
    Each line becomes an item in a JSON array.
    """
    try:
        # Read the text file
        with open(input_file, 'r', encoding='utf-8') as txt_file:
            lines = txt_file.readlines()
        
        # Remove whitespace and empty lines
        lines = [line.strip() for line in lines if line.strip()]
        
        # Create JSON data
        json_data = {"content": lines}
        
        # Write to JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Successfully converted {input_file} to {output_file}")
        print(f"Processed {len(lines)} lines")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.txt output.json")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        txt_to_json_simple(input_file, output_file)