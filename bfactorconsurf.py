def parse_txt_file(txt_file):
    conservation_scores = {}
    with open(txt_file, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('POS'):
                parts = line.split()
                try:
                    pos = int(parts[0])
                    color = int(parts[3])
                    conservation_scores[pos] = color
                except ValueError:
                    continue
    return conservation_scores


def add_color_to_pdb(pdb_file, conservation_scores):
    output_lines = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith('ATOM'):
                pos = int(line[22:26])
                if pos in conservation_scores:
                    color = conservation_scores[pos]
                    # Convert color to B-factor format
                    bfactor = f'{color:6.2f}'
                    line = line[:60] + bfactor + line[66:]
            output_lines.append(line)
    
    with open('output.pdb', 'w') as file:
        file.write(''.join(output_lines))

print("B-factor values added to the output.pdb file.")

# Paths to your PDB and TXT files
pdb_file = input("Enter path to the PDB file (eg. C:\\1AKI.pdb): ")
txt_file = input("Enter path to the TXT file (eg. C:\\consurf_grades.txt): ")

conservation_scores = parse_txt_file(txt_file)
add_color_to_pdb(pdb_file, conservation_scores)
