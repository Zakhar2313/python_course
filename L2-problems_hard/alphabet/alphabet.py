import typing as tp
import enum


class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2





def extract_alphabet(
        graph: tp.Dict[str, tp.Set[str]]
        ) -> tp.List[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """



def build_graph(
        words: tp.List[str]
        ) -> tp.Dict[str, tp.Set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """



#########################
# Don't change this code
#########################

def get_alphabet(
        words: tp.List[str]
        ) -> tp.List[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
