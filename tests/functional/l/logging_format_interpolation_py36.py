"""Test logging-fstring-interpolation for Python 3.6"""
import logging as renamed_logging

# [logging-fstring-interpolation]
renamed_logging.info(f'Read {renamed_logging} from globals')
