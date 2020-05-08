'''
Mock functions for testing
'''
# Copyright 2019-2020 Typo
#
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
#
# you may not use this file except in compliance with the
#
# License.
#
#
#
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing, software
#
# distributed under the License is distributed on an "AS IS" BASIS,
#
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#
# implied. See the License for the specific language governing
#
# permissions and limitations under the License.
#
#
#
# This product includes software developed at
#
# or by Typo (https://www.typo.ai/).

from test_utils.utils import generate_record


class MockRequestResponse:  # pylint: disable=too-few-public-methods
    '''
    Mocks requests get/post response
    '''
    def __init__(self, json_data, status_code, headers=None):
        self.json_data = json_data
        self.headers = headers if headers else {}
        self.text = ''
        self.status_code = status_code

    def json(self):
        '''
        Mocks response.json()
        '''
        return self.json_data


def generate_streaming_dataset_header_response():
    '''
    Streaming dataset sample header response
    '''
    return {
        'code': 'GET_DATASET_SUCCESS',
        'message': 'Get dataset success',
        'data': {
            'id': 1,
            'dataset': {
                'schema': {}
            },
            'metadata': None
        }
    }


def generate_dataset_listing_response():
    '''
    Simple response from dataset listing endpoint
    '''
    return [
        {
            "id": 1,
            "created_at": "2020-01-01T01:01:01.000Z",
            "updated_at": "2020-01-01T01:01:01.000Z",
            "tenant_id": 1,
            "name": "mock_dataset",
            "display_name": "mock_dataset",
            "repository_id": 1,
            "type": "Web App",
            "source": "https://mock-webapp.com",
            "tablename": "mock-tablename",
            "total_records": 500,
            "total_errors": 100,
            "total_fixes": 0,
            "total_ignores": 0,
            "total_actions": 0,
            "total_good_labels": 0,
            "total_bad_labels": 0,
            "total_labels": 0,
            "config": {
            },
            "repository": {
                "id": 1,
                "created_at": "2020-01-01T01:01:01.000Z",
                "updated_at": "2020-01-01T01:01:01.000Z",
                "name": "mock_repository",
                "is_enabled": True,
                "tenant_id": 2
            },
            "duplicate_checks": [],
            "models": [
                {
                    "id": 93059,
                    "created_at": "2020-02-04T15:59:42.297Z",
                    "updated_at": "2020-02-04T15:59:42.297Z",
                    "tenant_id": 2,
                    "repository_id": None,
                    "dataset_id": 14,
                    "features": [
                        "field_1",
                        "field_2",
                    ],
                    "subset_matcher": {},
                    "algorithm": "isolation-forest",
                    "algorithm_alias": "multivariate_check_1",
                    "object_path": "DH32VJ/isolation_forest.joblib",
                    "weight": 1,
                    "is_selected": True,
                    "build_run_id": "02e882d0-4766-11ea-8915-919a227c9964",
                    "accuracy": None,
                    "confusion_matrix": None,
                    "ro_object_path": None
                },
                {
                    "id": 93060,
                    "created_at": "2020-02-04T15:59:42.899Z",
                    "updated_at": "2020-02-04T15:59:42.899Z",
                    "tenant_id": 2,
                    "repository_id": None,
                    "dataset_id": 14,
                    "features": [
                        "dttm",
                        "tempend",
                        "densityor",
                        "tempstart",
                        "sysmoddate",
                        "syslockdate",
                        "syscreatedate",
                        "tankendvolcalc",
                        "dttmutclastticketintrun"
                    ],
                    "subset_matcher": {},
                    "algorithm": "modified-zscore",
                    "algorithm_alias": "univariate_check_1",
                    "object_path": "SE74EL/modified_zscore.joblib",
                    "weight": 1,
                    "is_selected": True,
                    "build_run_id": "02e882d0-4766-11ea-8915-919a227c9964",
                    "accuracy": None,
                    "confusion_matrix": None,
                    "ro_object_path": None
                }
            ],
            "schema": {}
        }
    ]


def generate_audit_dataset_header_response():
    '''
    Audit dataset sample header response
    '''
    return {
        'code': 'GET_AUDIT_SUCCESS',
        'message': 'Get audit success',
        'data': {
            'id': 1,
            'dataset': {
                'schema': {}
            },
            'metadata': None
        }
    }


def generate_audit_dataset_header_response_detailed_schema():
    '''
    Audit dataset sample header response with a detailed schema
    '''
    return {
        'code': 'GET_AUDIT_SUCCESS',
        'message': 'Get audit success',
        'data': {
            'id': 1,
            'dataset': {
                'schema': {
                    'val1': {
                        'primary': True,
                        'type': 'string'
                    },
                    'val2': {
                        'primary': False,
                        'type': 'varchar'
                    },
                    'val3': {
                        'type': 'int'
                    },
                    'val4': {
                        'type': 'integer'
                    },
                    'val5': {
                        'type': 'smallint'
                    },
                    'val6': {
                        'type': 'float'
                    },
                    'val7': {
                        'type': 'unknown'
                    },
                    'val8': {},
                    'val9': {
                        'primary': True
                    },
                }
            },
            'metadata': None
        }
    }


def generate_audit_listing_response():
    '''
    Simple response from audits listing endpoint
    '''
    return {
        'total': 1,
        'data': [{
            'id': 123,
            'guid': None,
            'created_at': '2020-01-01T01:01:01.000Z',
            'updated_at': '2020-01-01T01:01:01.000Z',
            'tenant_id': 1,
            'repository_id': 1,
            'dataset_id': 1,
            'name': None,
            'tag': None,
            'settings': None,
            'model': None,
            'total_records': 5000,
            'total_audited': None,
            'total_errors': 1000,
            'started_at': '2020-01-01T01:01:01.000Z',
            'ended_at': '2020-02-01T01:01:01.000Z',
            'state': 'COMPLETED',
            'data_profile': None,
            'repository': {
                'id': 1,
                'created_at': '2020-01-01T01:01:01.000Z',
                'updated_at': '2020-01-01T01:01:01.000Z',
                'name': 'mock_repository',
                'is_enabled': True,
                'tenant_id': 2
            },
            'dataset': {
                'id': 1,
                'created_at': '2020-01-01T01:01:01.000Z',
                'updated_at': '2020-01-01T01:01:01.000Z',
                'tenant_id': 1,
                'repository_id': 1,
                'tablename': 'mock_dataset_table',
                'name': 'mock_dataset',
                'display_name': 'mock_dataset',
                'type': 'Typo DI',
                'source': 'REST Import',
                'schema': None,
                'metadata': {
                    'schema': {
                        'field_1': {
                            'type': 'integer'
                        },
                        'field_2': {
                            'type': 'float'
                        }
                    }
                },
                'features': {
                    'field_1': {
                        'type': 'string'
                    },
                    'field_2': {
                        'type': 'integer'
                    }
                },
                'data_profile': {
                }
            },
            'schema': {
                'field_1': {
                    'type': 'integer'
                },
                'field_2': {
                    'type': 'float'
                }
            }
        }]
    }


def generate_streaming_dataset_response(records):
    '''
    Simple streaming dataset response
    '''
    return {
        'code': 'GET_DATASET_RESULTS_SUCCESS',
        'message': 'Get Dataset results success',
        'data': {
            'page': 1, 'per_page': 1, 'total_pages': 2,
            'total_records': 5, 'filters': [], 'sort': {},
            'records': records
        }
    }


def generate_audit_dataset_response(records, data_overrides=None):
    '''
    Simple audit dataset response
    '''
    data = {
        'page': 1, 'records_per_page': 1, 'total_pages': 2,
        'total_records': 5, 'filters': [], 'sort': {},
        'records': records
    }

    if (data_overrides):
        data.update(data_overrides)

    return {
        'code': 'GET_AUDIT_RESULTS_SUCCESS',
        'message': 'Get Dataset results success',
        'data': data
    }


def mock_requests_post_get_token(url, headers, data, timeout):  # pylint: disable=unused-argument
    '''
    Mock get_token
    '''
    return MockRequestResponse({'token': 'test'}, 200)


def mock_requests_get_test_discover_mode(url, headers, params, timeout):  # pylint: disable=unused-argument
    '''
    Mock get requests for test_discover_mode
    '''
    # Return audit header
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123':
        return MockRequestResponse(generate_audit_dataset_header_response_detailed_schema(), 200)

    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')


def mock_requests_get_test_resume_with_state(url, headers, params, timeout):  # pylint: disable=unused-argument
    '''
    Mock get requests for test_resume_with_state
    '''
    # Return audit header
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123':
        return MockRequestResponse(generate_audit_dataset_header_response(), 200)

    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123/results?records_per_page=5&page=1&__typo_id=gt:6':
        # tap-typo will resume from record with id 7
        return MockRequestResponse(generate_audit_dataset_response(
            [generate_record(7, has_errors=True), generate_record(8), generate_record(9),
             generate_record(10), generate_record(11, has_errors=True)]
        ), 200, headers={'Link': ''})

    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')


# pylint: disable=unused-argument
def mock_requests_get_test_get_simple_streaming_dataset(url, headers, params, timeout):
    '''
    Mock get requests for test_get_simple_streaming_dataset
    '''
    # Return audit header
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset':
        return MockRequestResponse(generate_streaming_dataset_header_response(), 200)

    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/results?records_per_page=100&page=1':
        # Return 1st and only results page
        return MockRequestResponse(
            generate_streaming_dataset_response(
                [generate_record(1, has_errors=True), generate_record(2)]
            ),
            200, headers={'Link': ''})

    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')


def mock_requests_get_test_get_simple_audit_dataset(url, headers, params, timeout):
    '''
    Mock get requests for test_get_simple_audit_dataset
    '''
    # Return audit header
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123':
        return MockRequestResponse(generate_audit_dataset_header_response(), 200)

    if (url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123/results' +
            '?records_per_page=100&page=1'):
        # Return 1st and only results page
        return MockRequestResponse(
            generate_audit_dataset_response(
                [generate_record(1, has_errors=True), generate_record(2)]
            ),
            200, headers={'Link': ''})

    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')


def mock_requests_get_test_multi_page_no_limit(url, headers, params, timeout):
    '''
    Mock get requests for test_multi_page_no_limit
    '''
    # Return audit header
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123':
        return MockRequestResponse(generate_audit_dataset_header_response(), 200)

    # Return 1st page of results
    if (url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123/results?'
            + 'records_per_page=2&page=1'):
        return MockRequestResponse(
            generate_audit_dataset_response(
                [generate_record(1, has_errors=True), generate_record(2)],
                {'records_per_page': 2, 'total_records': 4}
            ),
            200, headers={'Link': '; rel="next"'})

    # Return 2nd page of results
    if url == 'https://typo.ai/repositories/mock_repository/datasets/mock_dataset/audits/123/results?records_per_page=2&page=2':
        return MockRequestResponse(
            generate_audit_dataset_response(
                [generate_record(3, has_errors=True), generate_record(4)]
            ),
            200, headers={'Link': ''})

    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')


def mock_requests_get_test_request_token(url, headers, params, timeout):  # pylint: disable=unused-argument
    '''
    Mock get requests for test_request_token
    '''
    if url == 'https://typo.ai/datasets':
        return MockRequestResponse(generate_dataset_listing_response(), 200)

    if url == 'https://typo.ai/audits':
        return MockRequestResponse(generate_audit_listing_response(), 200)

    raise Exception('This code should not be reached')
