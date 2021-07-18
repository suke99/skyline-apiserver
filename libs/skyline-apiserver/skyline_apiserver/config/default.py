# Copyright 2021 99cloud
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import List

from pydantic import StrictBool, StrictInt, StrictStr
from skyline_config import Opt

debug = Opt(
    name="debug",
    description="Enable debug",
    schema=StrictBool,
    default=False,
)

log_dir = Opt(
    name="log_dir",
    description="Log directory",
    schema=StrictStr,
    default="./log",
)

secret_key = Opt(
    name="secret_key",
    description="Secret key",
    schema=StrictStr,
    default="aCtmgbcUqYUy_HNVg5BDXCaeJgJQzHJXwqbXr0Nmb2o",
)

access_token_expire = Opt(
    name="access_token_expire",
    description="Access token expire seconds",
    schema=StrictInt,
    default=60 * 60,
)

access_token_renew = Opt(
    name="access_token_renew",
    description="access token renew seconds",
    schema=StrictInt,
    default=30 * 60,
)

cors_allow_origins = Opt(
    name="cors_allow_origins",
    description="CORS allow origins",
    schema=List[StrictStr],
    default=[],
)

session_name = Opt(
    name="session_name",
    description="Session name",
    schema=StrictStr,
    default="session",
)

database_url = Opt(
    name="database_url",
    description="Database url",
    schema=StrictStr,
    default="mysql://root:root@localhost:3306/skyline",
)

GROUP_NAME = __name__.split(".")[-1]
ALL_OPTS = (
    debug,
    log_dir,
    secret_key,
    access_token_expire,
    access_token_renew,
    cors_allow_origins,
    session_name,
    database_url,
)

__all__ = ("GROUP_NAME", "ALL_OPTS")