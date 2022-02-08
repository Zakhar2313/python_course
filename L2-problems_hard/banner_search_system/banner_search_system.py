import typing as tp

import heapq
import string


def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """



def get_words(
        query: str
        ) -> tp.List[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """


def build_index(
        banners: tp.List[str]
        ) -> tp.Dict[str, tp.List[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """



def get_banner_indices_by_query(
        query: str,
        index: tp.Dict[str, tp.List[int]]
        ) -> tp.List[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """

#########################
# Don't change this code
#########################


def get_banners(
        query: str,
        index: tp.Dict[str, tp.List[int]],
        banners: tp.List[str]
        ) -> tp.List[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################
