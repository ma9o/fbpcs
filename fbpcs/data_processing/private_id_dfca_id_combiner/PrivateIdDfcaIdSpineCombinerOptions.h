/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <gflags/gflags_declare.h>

DECLARE_string(spine_path);
DECLARE_string(data_path);
DECLARE_string(output_path);
DECLARE_string(tmp_directory);
DECLARE_string(run_name);
DECLARE_string(sort_strategy);
DECLARE_bool(log_cost);
DECLARE_string(log_cost_s3_bucket);
DECLARE_string(log_cost_s3_region);
DECLARE_int32(max_id_column_cnt);
DECLARE_string(protocol_type);
DECLARE_string(run_id);
