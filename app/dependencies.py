from typing import Optional

from fastapi import Header


def headers(x_rhi_username: Optional[str] = Header(None)):
    return {
        "x_rhi_username": x_rhi_username,
    }
