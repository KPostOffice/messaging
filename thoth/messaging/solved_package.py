#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Francesco Murdaca
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This is Thoth Messaging module for SolvedPackageMessage."""

import logging

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.solver.solved-package"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a solved package message Kafka topic."""

    package_name: str
    package_version: str
    index_url: str
    solver: str
    version: str = "v1"


solved_package_message = MessageBase(base_name=base_name, model=MessageContents)
