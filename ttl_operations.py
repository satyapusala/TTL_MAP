#!/usr/bin/env python

""" TTL operations class
@b @Description:
Base class to be imported to implement ttl Test Cases.

@b Usage
import this class and implement specific Test Case classes
"""

import sys
import time
from TTL_MAP.logger import log


class TtlOperations:
    """
    This class contains methods to perform operations like adding records and accessing records from ttl map
    """
    def __init__(self):
        self.ttl_map = dict()
        self.time_stamp = dict()

    def add_record(self, key, value, ttl=None):
        """
        Add given key and value pair to ttl map. And also add ttl info to time_stamp dict to maintain ttl data
        :param key: Key of the record
        :param value: Value of the record
        :param ttl: Time to expiry value
        """
        self.ttl_map[key] = value
        self.time_stamp[key] = [time.time(), ttl]
        log.debug("Record is successfully added to map. key: %s, Value: %s" % (key, value))

    def get_record(self, key):
        """
        This method will return record of matching key
        :param key: Key of the record to be accessed
        :return: Record of matching key
        """
        expiary_time = time.time() - self.time_stamp[key][0]
        if expiary_time > self.time_stamp[key][1]:
            del self.ttl_map[key]
            log.debug("Record is expired: %s", key)
        else:
            return self.ttl_map[key]


if __name__ == "__main__":
    ttl = TtlOperations()
    ttl.add_record('key1', 10, 2)
    time.sleep(1)
    record = ttl.get_record('key1')
    log.debug("Record is: %s", record)
    sys.exit()
