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

from typing import List, Union

from ...runtime import Application, CallbackBase, CallbackGroup, Executor, Node
from callback_info_interface import TimeSeriesPlot
from callback_info import CallbackFrequencyPlot, CallbackJitterPlot, CallbackLatencyPlot


CallbacksType = Union[Application, Executor,
                      Node, CallbackGroup, List[CallbackBase]]


class Plot:

    @staticmethod
    def create_callback_frequency_plot(callbacks: CallbacksType) -> TimeSeriesPlot:
        return CallbackFrequencyPlot(callbacks)

    @staticmethod
    def create_callback_jitter_plot(callbacks: CallbacksType) -> TimeSeriesPlot:
        return CallbackJitterPlot(callbacks)

    @staticmethod
    def create_callback_latency_plot(callbacks: CallbacksType) -> TimeSeriesPlot:
        return CallbackLatencyPlot(callbacks)