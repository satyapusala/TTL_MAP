#!/usr/bin/env python

""" TTL Tests class
@b @Description:
Test class covers methods for  test scenarios

@b Usage
Test class and methods can be executed using pytest framework
"""

import time
import pytest

from TTL_MAP.ttl_operations import TtlOperations
from TTL_MAP.logger import log
from TTL_MAP.logger import log_capture
from TTL_MAP.logger import end_capture


@pytest.fixture(scope="module")
def pytest_configure(request):
    """
    Sets the config in project_properties.py as source config file
    """
    log_capture('ttl_tests')
    yield
    end_capture()


def test_get_record_before_expiry(pytest_configure):
    """
    Test steps:
        a. Add rec1 to ttl_map
        b. get the value of rec1 from ttl_map
    """
    ttl = TtlOperations()
    key = 'rec1'
    ttl.add_record(key, 'rec_val1', 2)
    record = ttl.get_record(key)
    log.debug("Record accessed successfully")
    assert record == ttl.ttl_map[key], "Record accessed successfully"


def test_get_record_after_expiry(pytest_configure):
    """
    Test steps:
        a. Add rec1 to ttl_map with ttl value 2secs
        b. Wait for 3secs
        b. Get the value of rec1 from ttl_map
    """
    ttl = TtlOperations()
    key = 'rec1'
    ttl.add_record(key, 'rec_val1', 2)
    time.sleep(3)
    record = ttl.get_record(key)
    assert record == None, "Record was deleted after expiry"


def test_get_multilple_records(pytest_configure):
    """
    Test steps:
    a. Add multiple records to ttl_map with different ttl values
    b. Wait for 3secs
    c. Get the value of rec2 and rec2 from ttl_map
    """
    ttl = TtlOperations()
    ttl.add_record('rec1', 'rec_val1', 2)
    ttl.add_record('rec2', 'rec_val2', 1)
    ttl.add_record('rec3', 'rec_val3', 5)
    ttl.add_record('rec4', 'rec_val4', 10)
    time.sleep(3)
    record2 = ttl.get_record('rec2')
    record3 = ttl.get_record('rec3')
    assert record2 == None, "Record was deleted after expiry"
    assert record3 == ttl.ttl_map['rec3'], "Record accessed successfully"
