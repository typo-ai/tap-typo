#!/usr/bin/env python3

# Copyright 2019-2020 Typo. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.
#
# This product includes software developed at or by Typo (https://www.typo.ai/).

import sys
import singer
from singer import utils

from tap_typo.logging import log_critical, log_error, log_info
from tap_typo.typo import TapTypo


REQUIRED_CONFIG_KEYS = [
    'api_key', 'api_secret', 'cluster_api_endpoint'
]
LOGGER = singer.get_logger()


@utils.handle_top_exception(LOGGER)
def main():
    '''
    Called when the program is executed.
    '''
    # Parse command line arguments
    try:
        args = utils.parse_args(REQUIRED_CONFIG_KEYS)
    except Exception as exception:  # pylint: disable=W0703
        log_critical(exception)
        sys.exit(1)

    config = args.config

    if args.discover:
        log_info('Starting in Discover Mode.')
    else:
        log_info('Starting in Sync Mode.')

    tap = TapTypo(
        catalog=args.catalog.to_dict() if args.catalog else None,
        config=config,
        state=args.state
    )

    if args.discover:
        tap.discover()
        log_info('Discover Mode completed.')
    else:
        catalog_mode = args.catalog is not None
        tap.sync(catalog_mode)
        log_info('Sync Mode completed.')


if __name__ == '__main__':
    log_error('__main__')
    main()
