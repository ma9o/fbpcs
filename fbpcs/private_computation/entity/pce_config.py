#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict


from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json
from fbpcs.private_computation.entity.cloud_provider import CloudProvider


@dataclass_json
@dataclass
class PCEConfig:
    subnets: List[str]
    cluster: str
    region: str
    onedocker_task_definition: str
    partner_name: Optional[str] = None
    cloud_provider: CloudProvider = CloudProvider.AWS
    # TODO T118605748 The cloud_account_id should not be optional in PCEConfig. Make it required after a full release cycle
    cloud_account_id: Optional[str] = None
    partner_id: Optional[str] = None
    pce_id: Optional[str] = None

    def __str__(self) -> str:
        # pyre-ignore
        return self.to_json()
