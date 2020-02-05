'''
Test utility functions
'''
# Copyright 2019-2020 Typo. All Rights Reserved.
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


def generate_config(**kwargs):
    '''
    Generates a config file for testing
    '''
    config = {
        'cluster_api_endpoint': 'https://typo.ai',
        'api_key': 'typo_key',
        'api_secret': 'typo_secret',
        'repository': 'mock_repository',
        'dataset': 'mock_dataset',
        'audit_id': '123',
        'state': {},
        'records_per_page': 100,
        'record_limit': -1
    }

    config.update(kwargs)

    return config


def generate_record(record_id, **kwargs):
    '''
    Generates a record API response
    '''
    record = {
        'tag': '',
        'quality_label': 'Not Set',
        'quality_feedback': {
            'date': 'Not Set',
            'typo': 'Good'
        },
        'record': {
            'date': 'today',
            'typo': 'tap'
        },
        'total_models': 3,
        'processed_models': 3,
        'record_hash': 'hash',
        'created_at': '2020-01-27T00:20:35.782Z',
        'tenant_id': 1,
        'repository_id': 1,
        'id': record_id,
        'audit_id': 1,
        'has_errors': False,
        'errors_fields': []
    }

    record.update(kwargs)

    return record
