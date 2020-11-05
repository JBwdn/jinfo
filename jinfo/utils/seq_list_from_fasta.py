from typing import Union, Optional, List
from jinfo.sequence import BaseSeq, DNASeq, RNASeq, AASeq

ANY_SEQ = Union[BaseSeq, DNASeq, RNASeq, AASeq]


def seq_list_from_fasta(file_path: str, seq_type: Optional[ANY_SEQ]) -> List[ANY_SEQ]:
    """
    Parse a multifasta file

    Returns list of BaseSeq objects
    """

    from jinfo.sequence import BaseSeq
    import re

    with open(file_path, "r") as text_file:
        fasta_str = text_file.read()

    label_list = re.findall(r"^>(.*)", fasta_str, re.MULTILINE)
    fasta_lines = fasta_str.split("\n")
    seq_list = []

    for i in range(len(label_list)):
        label_index = fasta_lines.index(">" + label_list[i])
        if i == len(label_list) - 1:
            seq_string = "".join(fasta_lines[label_index + 1 :])
        else:
            next_label_index = fasta_lines.index(">" + label_list[i + 1])
            seq_string = "".join(fasta_lines[label_index + 1 : next_label_index])

        if seq_type is None:
            seq_list.append(BaseSeq(sequence=seq_string, label=label_list[i]))
        else:
            seq_list.append(seq_type(sequence=seq_string, label=label_list[i]))
    return seq_list


if __name__ == "__main__":
    pass
