import typing as tp


def get_unique_page_ids(records: tp.List[tp.Mapping[str, tp.Any]]) -> tp.Set[int]:
    """
    Get unique web pages visited
    :param records: records of hit-log
    :return: Unique web pages
    """


def get_unique_page_ids_visited_after_ts(records: tp.List[tp.Mapping[str, tp.Any]], ts: int) -> tp.Set[int]:
    """
    Get unique web pages visited after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :return: Unique web pages visited in hit-log after some timestamp
    """


def get_unique_user_ids_visited_page_after_ts(
        records: tp.List[tp.Mapping[str, tp.Any]],
        ts: int,
        page_id: int
        ) -> tp.Set[int]:
    """
    Get unique users visited given web page after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :param page_id: web page identifier
    :return: Unique web pages visited in hit-log after some timestamp
    """



def get_events_by_device_type(
        records: tp.List[tp.Mapping[str, tp.Any]],
        device_type: str
        ) -> tp.List[tp.Mapping[str, tp.Any]]:
    """
    Filter events for given device type with order preservation
    :param records: records of hit-log
    :param device_type: device typy name to filter by
    :return: filtered events
    """

DEFAULT_REGION_ID = 100500


def get_region_ids_with_none_replaces_by_default(
        records: tp.List[tp.Mapping[str, tp.Any]]
        ) -> tp.List[int]:
    """
    Extract visited regions with order preservation. If region not defined, replace it by default region id
    :param records: records of hit-log
    :return: region ids
    """


def get_region_id_if_not_none(
        records: tp.List[tp.Mapping[str, tp.Any]]
        ) -> tp.List[int]:
    """
    Extract visited regions if they are defined with order preservation
    :param records: records of hit-log
    :return: region ids
    """


def get_keys_where_value_is_not_none(r: tp.Mapping[str, tp.Any]) -> tp.List[str]:
    """
    Extract keys where values are defined
    :param r: record of hit-log
    :return: keys where values are defined
    """


def get_record_with_none_if_key_not_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: tp.Set[str]
        ) -> tp.Dict[str, tp.Any]:
    """
    Get record with other keys replaced by None
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: record with other keys replaced by None
    """


def get_record_with_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: tp.Set[str]
        ) -> tp.Dict[str, tp.Any]:
    """
    Filter record by keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered record
    """


def get_keys_if_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: tp.Set[str]
        ) -> tp.Set[str]:
    """
    Filter keys from record by given keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered record
    """
