# Copyright 2021 Research Institute of Systems Planning, Inc.
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

from typing import Optional, Tuple

from ....value_objects import (
    ClientCallbackValue,
    ServiceCallbackValue,
    SubscriptionCallbackValue,
    TimerCallbackValue,
)


class TimerCallbackValueLttng(TimerCallbackValue):
    def __init__(
        self,
        pid: int,
        callback_id: str,
        node_id: str,
        node_name: str,
        symbol: str,
        period_ns: int,
        timer_handle: int,
        publish_topic_names: Optional[Tuple[str, ...]],
        callback_object: int,
    ) -> None:
        super().__init__(
            callback_id=callback_id,
            node_id=node_id,
            node_name=node_name,
            symbol=symbol,
            period_ns=period_ns,
            publish_topic_names=publish_topic_names,
        )
        self._pid = pid
        self._callback_object = callback_object
        self._timer_handle = timer_handle

    @property
    def pid(self) -> int:
        return self._pid

    @property
    def callback_object(self) -> int:
        return self._callback_object

    @property
    def timer_handle(self) -> int:
        return self._timer_handle


class SubscriptionCallbackValueLttng(SubscriptionCallbackValue):
    def __init__(
        self,
        pid: int,
        callback_id: str,
        node_id: str,
        node_name: str,
        symbol: str,
        subscribe_topic_name: str,
        subscription_handle: int,
        publish_topic_names: Optional[Tuple[str, ...]],
        callback_object: int,
        callback_object_intra: Optional[int],
        tilde_subscription: Optional[int]
    ) -> None:
        super().__init__(
            callback_id=callback_id,
            node_id=node_id,
            node_name=node_name,
            symbol=symbol,
            subscribe_topic_name=subscribe_topic_name,
            publish_topic_names=publish_topic_names,
        )

        self._pid = pid
        self._callback_object = callback_object
        self._callback_object_intra = callback_object_intra
        self._tilde_sub = tilde_subscription
        self._subscription_handle = subscription_handle

    @property
    def pid(self) -> int:
        return self._pid

    @property
    def callback_object(self) -> int:
        return self._callback_object

    @property
    def callback_object_intra(self) -> Optional[int]:
        return self._callback_object_intra

    @property
    def tilde_subscription(self) -> Optional[int]:
        return self._tilde_sub

    @property
    def subscription_handle(self) -> int:
        return self._subscription_handle


class ServiceCallbackValueLttng(ServiceCallbackValue):
    def __init__(
        self,
        pid: int,
        callback_id: str,
        node_id: str,
        node_name: str,
        symbol: str,
        callback_object: int,
        service_name: str,
        service_handle: int
    ) -> None:
        super().__init__(
            callback_id=callback_id,
            node_id=node_id,
            node_name=node_name,
            symbol=symbol,
            service_name=service_name,
        )
        self._pid = pid
        self._callback_object = callback_object
        self._service_handle = service_handle

    @property
    def pid(self) -> int:
        return self._pid

    @property
    def callback_object(self) -> int:
        return self._callback_object

    @property
    def service_handle(self) -> int:
        return self._service_handle


class ClientCallbackValueLttng(ClientCallbackValue):
    def __init__(
        self,
        pid: int,
        callback_id: str,
        node_id: str,
        node_name: str,
        symbol: str,
        callback_object: Optional[int],
        service_name: str,
        client_handle: int,
    ) -> None:
        super().__init__(
            callback_id=callback_id,
            node_id=node_id,
            node_name=node_name,
            symbol=symbol,
            service_name=service_name,
        )
        self._pid = pid
        self._callback_object = callback_object
        self._client_handle = client_handle

    @property
    def pid(self) -> int:
        return self._pid

    @property
    def callback_object(self) -> Optional[int]:
        return self._callback_object

    @property
    def client_handle(self) -> int:
        return self._client_handle