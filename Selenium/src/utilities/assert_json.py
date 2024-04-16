
import json
import re
import numbers
import pytest
import os
import requests
import logging
from src.utilities.customLogger import CustomLogger

def read_json_file(filename):
    file_path = os.path.join(os.getcwd(), "resources/api_resources/" + filename)
    json_response = json.loads(open(file_path).read())
    return json_response


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def assert_json(my_json, your_json, trace=False):

    logger.info('Comparing Json array')

    # Should not be None
    assert your_json is not None

    # A valid Json can be either dict or list. Ex. {'a': 1} vs [{'a': 1}]
    if type(my_json) is dict:

        keys1 = my_json.keys()
        for key in keys1:
            __trace('Comparing key: ' + key, trace)
            if your_json.get(key) is None:
                logger.info(msg='Key not found: {}'.format(key), CustomLogger_name="info")
                pytest.fail(msg='Key not found: {}'.format(key))

            # if the key's value is a JSONObject then recursively check it
            data1 = my_json[key]
            data2 = your_json[key]

            __trace('Type of data1: ' + str(type(data1)), trace)
            __trace('Type of data2: ' + str(type(data2)), trace)

            if (data1 is not None) and (type(data1) is dict):
                assert_json(data1, data2, trace)
            else:
                if (data1 is not None) and (type(data1) is list) and (type(data2) is list):
                    __compare_array(data1, data2, trace)
                else:
                    __compare_value(data1, data2, trace)

    elif type(my_json) is list:
        __compare_array(my_json, your_json, trace)

    else:
        pytest.fail(logger.info('Invalid Json'))


##############################################################
###                    Helper functions                    ###
##############################################################
def __trace(data, enable_trace=False):
    if enable_trace:
        print(str(data))


def __is_string(data):
    return (type(data) is str)


def __is_match_search_regex(data):
    return __is_match_regex(data) or __is_search_regex(data)


def __is_match_regex(data):
    return (__is_string(data)) and (data.startswith('!matchRegEx:'))


def __is_search_regex(data):
    return (__is_string(data)) and (data.startswith('!searchRegEx:'))


def __match_search_json_data_regex(data1, data2):
    # the regular expression pattern is data1 excluding the _regex: prefix
    if (__is_match_regex(data1)) and (None == re.match(data1[12:], data2)):
        pytest.fail(logger.info('dummy', 'Expected pattern: ' + data1[12:] + ' NOT in: ' + data2))

    if (__is_search_regex(data1)) and (None == re.search(data1[13:], data2)):
        pytest.fail(logger.info('dummy', 'Expected pattern: ' + data1[13:] + ' NOT in: ' + data2))


def __compare_value(data1, data2, trace=False):
    __trace('Compare data', trace)
    __trace(data1, trace)
    __trace(data2, trace)

    # Only care to check if the field value is of number type
    if ('!anyNumber' == data1):
        assert isinstance(data2, numbers.Number)
    else:
        if ('!anything' != data1):
            if (__is_match_search_regex(data1)) and (__is_string(data2)):
                __match_search_json_data_regex(data1, data2)

            if (type(data1) is type(data2)):
                if (data1 != data2) and (False == __is_match_search_regex(data1)):
                    pytest.fail(logger.info('dummy', 'Expected: ' + str(data1) + ' Actual: ' + str(data2)))
            else:
                pytest.fail(logger.info('dummy', 'Expected: ' + str(type(data1)) + ' Actual: ' + str(type(data2))))


def __compare_array(jarray1, jarray2, trace=False):
    if (type(jarray1) is list) and (type(jarray2) is list):
        # Expect empty array
        if (len(jarray1) == 0) and (0 < len(jarray2)):
            pytest.fail(logger.info('dummy', 'Expected length: ' + str(len(jarray1)) + \
                                    ' Actual length: ' + str(len(jarray2))))

        elif (len(jarray1) > len(jarray2)) and (jarray1[0] != '!anythingOrNothing'):
            pytest.fail(logger.info('dummy', 'Expected length: ' + str(len(jarray1)) + \
                                    ' Actual length: ' + str(len(jarray2))))
        else:
            for i in range(len(jarray1)):

                # if the array item is a JSONObject then recursively check it
                if (type(jarray1[i]) is dict):
                    assert_json(jarray1[i], jarray2[i], trace)
                else:
                    __compare_value(jarray1[i], jarray2[i], trace)

