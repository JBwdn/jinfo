import jinfo as j

clf_aa_list = j.seq_list_from_fasta("CLF_known.fasta")
clf_alignment = j.multialign(clf_aa_list, maxiters=1)
clf_tree = clf_alignment.calc_tree()
print(clf_tree.tree)
