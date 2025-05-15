from Bio import SeqIO

input_files = [
    "D:/first/pythonProject/sequence (2).gb",
    "D:/first/pythonProject/sequence (3).gb"
]
output_file = "combined_species.gb"

with open(output_file, "w", encoding="utf-8") as outfile:
    for file in input_files:
        for record in SeqIO.parse(file, "genbank"):
            SeqIO.write(record, outfile, "genbank")

print(f"Файлы успешно объединены в {output_file}.")