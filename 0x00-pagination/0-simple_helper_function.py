#!/usr/bin/env python3
"""
    pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        retrieves the index range from a given page and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
