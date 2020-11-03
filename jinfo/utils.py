def one_hot_dna(input_seq_str: str, max_seq_len: int):
    """
    One hot encode a string format dna sequence.
    Add zero padding up to the maximum length.
    Returns: 1D numpy array of length 4*max_seq_len
    """
    import numpy as np

    encode_dict = {
        "A": [1, 0, 0, 0],
        "T": [0, 1, 0, 0],
        "C": [0, 0, 1, 0],
        "G": [0, 0, 0, 1],
        "X": [0, 0, 0, 0],
    }
    input_seq_upper = input_seq_str.upper()
    padding = "".join(["X" for i in range(max_seq_len - len(input_seq_str))])
    encoded_dna = [encode_dict[base] for base in input_seq_upper + padding]
    np_encoded = np.array(encoded_dna, dtype=int)
    return np_encoded.flatten()


def random_dna(seq_length: int) -> str:
    """
    Generate a random DNA sequence for primer design
    Returns: String of length seq_length
    """
    import random

    dna_base_list = ["A", "T", "C", "G"]
    seq_list = [random.choice(dna_base_list) for i in range(seq_length)]
    return "".join(seq_list)


def DNASeq_from_NCBI():
    """
    Fetch a DNA sequence using the NCBI Entrez api
    Returns ji.DNASeq object
    """
    from jinfo.sequence import DNASeq

    return


def seq_list_to_fasta(
    seq_list: list, file_name: str = None, label_list: list = None
) -> str:
    """
    Covnert a list of Seq objects to a fasta format string
    Optionally add labels and save to file
    Returns: fasta string
    """
    fasta_str = ""
    for i, seq_obj in enumerate(seq_list):
        if label_list:
            label = label_list[i]
        else:
            label = f"Sequence_{i}"
        fasta_str += f">{label}\n{seq_obj.seq}\n\n"

    if file_name:
        with open(file=file_name, mode="w") as text_file:
            text_file.write(fasta_str)
    return fasta_str


def seq_list_from_fasta(seq_list: list, filename: str):
    return


def alignment_from_fasta(path: str):
    from jinfo.alignment import alignment

    return alignment()


if __name__ == "__main__":
    pass
