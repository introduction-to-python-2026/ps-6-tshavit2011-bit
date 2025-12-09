def create_codon_dict(file_path):
  dict = {}
  file = open(file_path)
  rows = file.readlines()
  file.close()
  for i in range(len(rows)):
    row = rows[i]
    codon = row.strip().split('\t')[0]
    acid = row.strip().split('\t')[2]
    dict[codon] = acid
  return dict


