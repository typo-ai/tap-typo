'''
Test stdout output strings for comparison
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

TEST_DISCOVER_MODE_OUTPUT = '''{
  "streams": [
    {
      "stream": "tap-typo-mock_repository-mock_dataset",
      "tap_stream_id": "tap-typo-mock_repository-mock_dataset",
      "schema": {
        "type": "object",
        "additionalProperties": true,
        "properties": {
          "__typo_result": {
            "type": "string"
          },
          "__typo_record_id": {
            "type": "integer"
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "__typo_record_id"
            ],
            "inclusion": "available",
            "schema-name": "tap-typo-mock_repository-mock_dataset",
            "repository": "mock_repository",
            "dataset": "mock_dataset",
            "audit_id": null,
            "is-view": false,
            "database-name": "mock_repository",
            "row-count": 500,
            "valid-replication-keys": [
              "__typo_record_id"
            ],
            "selected-by-default": false
          }
        },
        {
          "breadcrumb": [
            "properties",
            "__typo_result"
          ],
          "metadata": {
            "inclusion": "available",
            "selected-by-default": true,
            "sql-datatype": "varchar(255)"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "__typo_record_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected-by-default": true,
            "sql-datatype": "int"
          }
        }
      ],
      "key_properties": [
        "__typo_record_id"
      ],
      "bookmark_properties": [
        "__typo_record_id"
      ]
    },
    {
      "stream": "tap-typo-mock_repository-mock_dataset-audit-123",
      "tap_stream_id": "tap-typo-mock_repository-mock_dataset-audit-123",
      "schema": {
        "type": "object",
        "additionalProperties": true,
        "properties": {
          "field_1": {
            "type": [
              "null",
              "integer"
            ]
          },
          "field_2": {
            "type": [
              "null",
              "number"
            ]
          },
          "__typo_result": {
            "type": "string"
          },
          "__typo_record_id": {
            "type": "integer"
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "__typo_record_id"
            ],
            "inclusion": "available",
            "schema-name": "tap-typo-mock_repository-mock_dataset-audit-123",
            "repository": "mock_repository",
            "dataset": "mock_dataset",
            "audit_id": 123,
            "is-view": true,
            "database-name": "mock_repository",
            "row-count": 5000,
            "valid-replication-keys": [
              "__typo_record_id"
            ],
            "selected-by-default": false
          }
        },
        {
          "breadcrumb": [
            "properties",
            "field_1"
          ],
          "metadata": {
            "inclusion": "available",
            "selected-by-default": true,
            "sql-datatype": "int"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "field_2"
          ],
          "metadata": {
            "inclusion": "available",
            "selected-by-default": true,
            "sql-datatype": "float"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "__typo_result"
          ],
          "metadata": {
            "inclusion": "available",
            "selected-by-default": true,
            "sql-datatype": "varchar(255)"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "__typo_record_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected-by-default": true,
            "sql-datatype": "int"
          }
        }
      ],
      "key_properties": [
        "__typo_record_id"
      ],
      "bookmark_properties": [
        "__typo_record_id"
      ]
    }
  ]
}
'''

TEST_RESUME_WITH_STATE_OUTPUT = (
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 6}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "SCHEMA", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "schema": {"type": "object", "additionalProperties": true, "properties": {"field_1": {"type": ["null", "integer"]}, "field_2": {"type": ["null", "number"]}, "__typo_result": {"type": "string"}, "__typo_record_id": {"type": "integer"}}}, "key_properties": ["__typo_record_id"], "bookmark_properties": ["__typo_record_id"]}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 7}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 7}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 8}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 8}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 9}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 9}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 10}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 10}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 11}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 11}}}}\n' # noqa pylint: disable=line-too-long
)

TEST_GET_SIMPLE_AUDIT_DATASET_OUTPUT = (
    '{"type": "STATE", "value": {}}\n' +
    '{"type": "SCHEMA", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "schema": {"type": "object", "additionalProperties": true, "properties": {"field_1": {"type": ["null", "integer"]}, "field_2": {"type": ["null", "number"]}, "__typo_result": {"type": "string"}, "__typo_record_id": {"type": "integer"}}}, "key_properties": ["__typo_record_id"], "bookmark_properties": ["__typo_record_id"]}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 1}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 1}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 2}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 2}}}}\n' # noqa pylint: disable=line-too-long
)

TEST_GET_SIMPLE_STREAMING_DATASET_OUTPUT = (
    '{"type": "STATE", "value": {}}\n' +
    '{"type": "SCHEMA", "stream": "tap-typo-mock_repository-mock_dataset", "schema": {"type": "object", "additionalProperties": true, "properties": {"__typo_result": {"type": "string"}, "__typo_record_id": {"type": "integer"}}}, "key_properties": ["__typo_record_id"], "bookmark_properties": ["__typo_record_id"]}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 1}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset": {"__typo_record_id": 1}}}}\n' +
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 2}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset": {"__typo_record_id": 2}}}}\n'
)

TEST_MULTI_PAGE_NO_LIMIT_OUTPUT = (
    '{"type": "STATE", "value": {}}\n' +
    '{"type": "SCHEMA", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "schema": {"type": "object", "additionalProperties": true, "properties": {"field_1": {"type": ["null", "integer"]}, "field_2": {"type": ["null", "number"]}, "__typo_result": {"type": "string"}, "__typo_record_id": {"type": "integer"}}}, "key_properties": ["__typo_record_id"], "bookmark_properties": ["__typo_record_id"]}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 1}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 1}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 2}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 2}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "Error", "__typo_record_id": 3}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 3}}}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "RECORD", "stream": "tap-typo-mock_repository-mock_dataset-audit-123", "record": {"date": "today", "typo": "tap", "__typo_result": "OK", "__typo_record_id": 4}}\n' + # noqa pylint: disable=line-too-long
    '{"type": "STATE", "value": {"bookmarks": {"tap-typo-mock_repository-mock_dataset-audit-123": {"__typo_record_id": 4}}}}\n' # noqa pylint: disable=line-too-long
)
