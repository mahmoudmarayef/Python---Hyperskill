def get_complementary_strand(origin: str) -> str:
    c_strand = ""
    c_principle = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        " ": " "
    }
    for vitamin in origin:
        c_strand = "".join([c_strand, c_principle[vitamin]])
    return c_strand


def cut_plasmid(strand: str, sequence: str) -> (str, str):
    complement_strand = get_complementary_strand(strand)
    complement_sequence = get_complementary_strand(sequence)
    cut_origin_index = strand.index(sequence)
    cut_complement_index = complement_strand.index(complement_sequence)
    return (" ".join([strand[:cut_origin_index + 1], strand[cut_origin_index + 1:]]),
            " ".join([complement_strand[:cut_complement_index + 5], complement_strand[cut_complement_index + 5:]]))


def cut_gfp(strand: str, restriction_site: str) -> (str, str):
    complementary_restriction_site, complementary_strand = get_complementary_strand(
        restriction_site), get_complementary_strand(strand)
    origin_start, origin_end = strand.index(restriction_site.split()[0]), strand.index(
        restriction_site.split()[1])

    complementary_start, complementary_end = complementary_strand.index(
        complementary_restriction_site.split()[0]), complementary_strand.index(
        complementary_restriction_site.split()[1])

    return (strand[origin_start + 1:origin_end + 1], complementary_strand[
                                                     complementary_start + len(complementary_restriction_site.split()[
                                                                                   0]) - 1:complementary_end + len(
                                                         complementary_restriction_site.split()[1]) - 1])


def glowing_bacteria(o_strand, gfp_strand, o_strand_sticky,
                     c_strand, c_gfp_strand_sticky,
                     c_strand_sticky):
    print(o_strand, gfp_strand, o_strand_sticky, sep="")
    print(c_strand, c_gfp_strand_sticky, c_strand_sticky, sep="")


if __name__ == '__main__':
    with open(input()) as file:
        original_plasmid_strand, plasmid_cut, original_gfp_strand, gfp_restriction_sites = file.readlines()
        complementary_plasmid_strand = get_complementary_strand(original_plasmid_strand.rstrip("\n"))
        plasmid_cut, complement_cut = cut_plasmid(original_plasmid_strand.rstrip("\n"), plasmid_cut.rstrip("\n"))
        original_gfp_strand_sticky, complementary_gfp_strand_sticky = cut_gfp(original_gfp_strand.rstrip("\n"), gfp_restriction_sites.rstrip("\n"))
        glowing_bacteria(plasmid_cut.split()[0], original_gfp_strand_sticky, plasmid_cut.split()[1],
                         complement_cut.split()[0], complementary_gfp_strand_sticky, complement_cut.split()[1])
