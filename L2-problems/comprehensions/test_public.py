import copy
import dis
import types
import typing as tp


from . import comprehensions as comp


def _is_comprehension(instruction: dis.Instruction, comp_name: str) -> bool:
    return isinstance(instruction.argval, types.CodeType) and instruction.argval.co_name == comp_name


def _is_functional_call(instruction: dis.Instruction) -> bool:
    return instruction.opname == 'LOAD_GLOBAL' and instruction.argval in {'map', 'filter'}


def _check_comprehension_structure(func: tp.Callable[..., tp.Any], comprehension_name: str) -> None:
    is_used_comprehension = any(_is_comprehension(i, comprehension_name) for i in dis.get_instructions(func))
    assert is_used_comprehension, "You should use comprehension"

    is_used_functional_call = any(_is_functional_call(i) for i in dis.get_instructions(func))
    assert not is_used_functional_call, "You shouldn't use map/filter functions"

    is_used_loop = any(i.opname == 'SETUP_LOOP' for i in dis.get_instructions(func))
    assert not is_used_loop, "You shouldn't use loops"


TEST_RECORDS: tp.List[tp.Mapping[str, tp.Any]] = [
    {"EventID": 12345, "EventTime": 1568839214, "UserID": 12456,
     "PageID": 10, "RegionID": None, "DeviceType": "Safari"},
    {"EventID": 12346, "EventTime": 1568839215, "UserID": 12456, "PageID": 10, "RegionID": None,
     "DeviceType": "Safari"},
    {"EventID": 12347, "EventTime": 1568839216, "UserID": 12456, "PageID": 11, "RegionID": None,
     "DeviceType": "Safari"},
    {"EventID": 25647, "EventTime": 1568839217, "UserID": 12395, "PageID": 112, "RegionID": 10,
     "DeviceType": "Internet Explorer"},
    {"EventID": 12345, "EventTime": 1568839218, "UserID": 12395, "PageID": 221, "RegionID": 0,
     "DeviceType": "Firefox"},
    {"EventID": 15789, "EventTime": 1568839219, "UserID": 12399, "PageID": 221, "RegionID": 20,
     "DeviceType": "Internet Explorer"}
]


TEST_RECORD: tp.Mapping[str, tp.Any] = TEST_RECORDS[0]


def test_get_unique_page_ids() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_unique_page_ids(test_records)

    _check_comprehension_structure(comp.get_unique_page_ids, '<setcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == {10, 11, 112, 221}


def test_get_unique_page_ids_visited_after_ts() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_unique_page_ids_visited_after_ts(test_records, 1568839216)

    _check_comprehension_structure(comp.get_unique_page_ids_visited_after_ts, '<setcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == {112, 221}


def test_get_unique_user_ids_visited_page_after_ts() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_unique_user_ids_visited_page_after_ts(test_records, 1568839216, 221)

    _check_comprehension_structure(comp.get_unique_user_ids_visited_page_after_ts, '<setcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == {12395, 12399}


def test_get_events_by_device_type() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_events_by_device_type(test_records, "Internet Explorer")

    _check_comprehension_structure(comp.get_events_by_device_type, '<listcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == [
        {"EventID": 25647, "EventTime": 1568839217, "UserID": 12395, "PageID": 112, "RegionID": 10,
         "DeviceType": "Internet Explorer"},
        {"EventID": 15789, "EventTime": 1568839219, "UserID": 12399, "PageID": 221, "RegionID": 20,
         "DeviceType": "Internet Explorer"}
    ]


def test_get_region_ids_with_none_replaces_by_default() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_region_ids_with_none_replaces_by_default(test_records)

    _check_comprehension_structure(comp.get_region_ids_with_none_replaces_by_default, '<listcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == [100500, 100500, 100500, 10, 0, 20]


def test_get_region_id_if_not_none() -> None:
    test_records = copy.deepcopy(TEST_RECORDS)
    result = comp.get_region_id_if_not_none(test_records)

    _check_comprehension_structure(comp.get_region_id_if_not_none, '<listcomp>')

    assert test_records == TEST_RECORDS, "You shouldn't change inputs"
    assert result == [10, 0, 20]


def test_get_keys_where_value_is_not_none() -> None:
    test_r = copy.deepcopy(TEST_RECORD)
    result = comp.get_keys_where_value_is_not_none(test_r)

    _check_comprehension_structure(comp.get_keys_where_value_is_not_none, '<listcomp>')

    assert test_r == TEST_RECORD, "You shouldn't change inputs"
    assert sorted(result) == sorted(["EventID", "EventTime", "UserID", "PageID", "DeviceType"])


def test_get_record_with_none_if_key_not_in_keys() -> None:
    test_r = copy.deepcopy(TEST_RECORD)
    result = comp.get_record_with_none_if_key_not_in_keys(test_r, {"EventID", "UserID"})

    _check_comprehension_structure(comp.get_record_with_none_if_key_not_in_keys, '<dictcomp>')

    assert test_r == TEST_RECORD, "You shouldn't change inputs"
    assert result == {"EventID": 12345, "EventTime": None, "UserID": 12456, "PageID": None, "RegionID": None,
                      "DeviceType": None}


def test_get_record_with_key_in_keys() -> None:
    test_r = copy.deepcopy(TEST_RECORD)
    result = comp.get_record_with_key_in_keys(test_r, {"EventID", "UserID"})

    _check_comprehension_structure(comp.get_record_with_key_in_keys, '<dictcomp>')

    assert test_r == TEST_RECORD, "You shouldn't change inputs"
    assert result == {"EventID": 12345, "UserID": 12456}


def test_get_keys_if_key_in_keys() -> None:
    test_r = copy.deepcopy(TEST_RECORD)
    result = comp.get_keys_if_key_in_keys(test_r, {"EventID", "UserID", "SomeField"})

    _check_comprehension_structure(comp.get_keys_if_key_in_keys, '<setcomp>')

    assert test_r == TEST_RECORD, "You shouldn't change inputs"
    assert result == {"EventID", "UserID"}
