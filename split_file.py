#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def split_file(input_file, chunk_size=500000):
    """
    Split a large file into smaller files with specified number of rows.
    
    Args:
        input_file (str): Path to the input file
        chunk_size (int): Number of rows per output file (default: 500000)
    """
    try:
        # Get the input file name without extension and its extension
        input_path = Path(input_file)
        base_name = input_path.stem
        extension = input_path.suffix
        
        # Create output directory if it doesn't exist
        output_dir = Path('split_output')
        output_dir.mkdir(exist_ok=True)
        
        # Counter for output files
        file_number = 1
        line_count = 0
        current_output = None
        
        print(f"Starting to split {input_file}...")
        
        # Read the input file and split it
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                # Open a new output file when needed
                if line_count % chunk_size == 0:
                    if current_output:
                        current_output.close()
                    output_file = output_dir / f"{base_name}_part{file_number}{extension}"
                    current_output = open(output_file, 'w', encoding='utf-8')
                    print(f"Creating file: {output_file}")
                    file_number += 1
                
                # Write the line to current output file
                current_output.write(line)
                line_count += 1
        
        # Close the last output file
        if current_output:
            current_output.close()
        
        print(f"\nSplit complete!")
        print(f"Total lines processed: {line_count}")
        print(f"Number of files created: {file_number - 1}")
        print(f"Output files are in the 'split_output' directory")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_file.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    
    split_file(input_file) 
