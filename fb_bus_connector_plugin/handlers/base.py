#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
FastyBird BUS connector plugin client handlers module base handler
"""

# Python base dependencies
import uuid
from abc import ABC, abstractmethod
from typing import Optional

# Library libs
from fb_bus_connector_plugin.logger import Logger


class BaseHandler(ABC):  # pylint: disable=too-few-public-methods
    """
    BUS messages base handler

    @package        FastyBird:FbBusConnectorPlugin!
    @module         handlers

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    _logger: Logger

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        logger: Logger,
    ) -> None:
        self._logger = logger

    # -----------------------------------------------------------------------------

    @abstractmethod
    def on_message(self, payload: bytearray, length: int, address: Optional[int], client_id: uuid.UUID) -> None:
        """On receive message event"""
