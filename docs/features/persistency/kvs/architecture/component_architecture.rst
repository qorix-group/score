..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Component Architecture
######################

Technical Concept Description
*****************************

The key-value-storage feature (KVS) scope is very small so only the KVS itself
and a another component to handle the persistent storage format are defined.

The API is stable for major version releases. Any changes are discussed in the
CFT. Whenever possible, the existing API is not changed and new functionality
is provided by new function calls.

Key-Value-Storage (KVS)
=======================

The KVS is presented like a dictonary or hashmap implementation to the
application with some extra APIs for flushing data, handling snapshots and
other functionality. All API functions guarantee to not panic or throw
exceptions that can't be handled. Error handling has one of the highest
priorities.

All actions are log- and traceable. The component supports productive and
develop environments.

The KVS is multi-threading safe and allows concurrent access to the same store.
Tracking changes can be done by subscribing to specified keys or the whole
store.

Values that are stored behind the keys can be numbers, text, null, arrays or
objects. Objects and arrays can be used to nest values.

A snapshot logic ensures rollback capabilities if something goes wrong.

TinyJSON
========

TinyJSON is used to serialize and deserialize the data as the well-known format
JSON to and from the permanent storage.

Component Architecure File(s)
=============================

.. comp_arc_sta:: Key-Value-Storage
   :id: comp_arc_sta__kvs__kvs
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int__archdes_component_interface_3
   :implements: comp_arc_int__archdes_component_interface_1, comp_arc_int__archdes_component_interface_2
   :fulfils: comp_req__archdes_example_req
   :includes: comp_arc_sta__archdes_sub_component_1, comp_arc_sta__archdes_sub_component_2, comp_arc_sta__archdes_sub_component_3

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. comp_arc_sta:: JSON Parser/Export
   :id: comp_arc_sta__kvs__json
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: comp_arc_int__archdes_component_interface_3
   :fulfils: comp_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


.. comp_arc_sta:: File Storage
   :id: comp_arc_sta__kvs__file_storage
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: comp_arc_int__archdes_component_interface_3
   :fulfils: comp_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. Component Interfaces

.. comp_arc_int:: Key-Value-Storage Interface
   :id: comp_arc_int__kvs__kvs_component_interface
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: rust

.. comp_arc_int:: JSON Parser/Export Component Interface
   :id: comp_arc_int__kvs__json_component_interface
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: rust

.. comp_arc_int:: File Storage Component Interface
   :id: comp_arc_int__kvs__file_storage_component_interface
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: rust

.. Subcomponents

.. comp_arc_sta:: Lower Level Component 1
   :id: comp_arc_sta__archdes_sub_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int_op__archdes_real_operation_7
   :implements: comp_arc_int_op__archdes_real_operation_3
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 2
   :id: comp_arc_sta__archdes_sub_component_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: comp_arc_int_op__archdes_real_operation_8
   :implements: comp_arc_int_op__archdes_real_operation_4
   :fulfils: comp_req__archdes_example_req

.. comp_arc_sta:: Lower Level Component 3
   :id: comp_arc_sta__archdes_sub_component_3
   :status: valid
   :safety: QM
   :security: NO
   :implements: comp_arc_int_op__archdes_real_operation_7, comp_arc_int_op__archdes_real_operation_8
   :fulfils: comp_req__archdes_example_req

.. Component Interface Operations

.. comp_arc_int_op:: KvsBuilder::new
   :id: comp_arc_int_op__kvs__builder_new
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: KvsBuilder::need_defaults
   :id: comp_arc_int_op__kvs__builder_need_defaults
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: KvsBuilder::need_kvs
   :id: comp_arc_int_op__kvs__builder_need_kvs
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: KvsBuilder::build
   :id: comp_arc_int_op__kvs__builder_build
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::open
   :id: comp_arc_int_op__kvs__open
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::flush_on_exit
   :id: comp_arc_int_op__kvs__flush_on_exit
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::open_json
   :id: comp_arc_int_op__kvs__open_json
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::reset
   :id: comp_arc_int_op__kvs__reset
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::get_all_keys
   :id: comp_arc_int_op__kvs__get_all_keys
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::key_exists
   :id: comp_arc_int_op__kvs__key_exists
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::get_value
   :id: comp_arc_int_op__kvs__get_value
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::get_default_value
   :id: comp_arc_int_op__kvs__get_default_value
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::is_value_default
   :id: comp_arc_int_op__kvs__is_value_default
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::set_value
   :id: comp_arc_int_op__kvs__set_value
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::remove_key
   :id: comp_arc_int_op__kvs__remove_key
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::flush
   :id: comp_arc_int_op__kvs__flush
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::snapshot_count
   :id: comp_arc_int_op__kvs__snapshot_count
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::snapshot_max_count
   :id: comp_arc_int_op__kvs__snapshot_max_count
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::snapshot_restore
   :id: comp_arc_int_op__kvs__snapshot_restore
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::snapshot_rotate
   :id: comp_arc_int_op__kvs__snapshot_rotate
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::get_kvs_filename
   :id: comp_arc_int_op__kvs__get_kvs_filename
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::get_hash_filename
   :id: comp_arc_int_op__kvs__get_hash_filename
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: Kvs::drop
   :id: comp_arc_int_op__kvs__drop
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__kvs_component_interface

.. comp_arc_int_op:: TinyJSON::JsonGenerator
   :id: comp_arc_int_op__tj__json_generator
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__json_component_interface

.. comp_arc_int_op:: TinyJSON::JsonValue
   :id: comp_arc_int_op__tj__json_value
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__json_component_interface

.. comp_arc_int_op:: TinyJSON::JsonParseError
   :id: comp_arc_int_op__tj__json_parse_error
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__json_component_interface

.. comp_arc_int_op:: TinyJSON::JsonGenerateError
   :id: comp_arc_int_op__tj__json_generate_error
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__json_component_interface

.. comp_arc_int_op:: TinyJSON::UnexpectedValue
   :id: comp_arc_int_op__tj__json_unexpected_value
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__json_component_interface

.. comp_arc_int_op:: Filesystem::read_to_string
   :id: comp_arc_int_op__fs__read_to_string
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__file_storage_component_interface

.. comp_arc_int_op:: Filesystem::read
   :id: comp_arc_int_op__fs__read
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__file_storage_component_interface

.. comp_arc_int_op:: Filesystem::write
   :id: comp_arc_int_op__fs__write
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__file_storage_component_interface

.. comp_arc_int_op:: Filesystem::rename
   :id: comp_arc_int_op__fs__rename
   :status: valid
   :safety: ASIL_B
   :security: NO
   :implements: feat_arc_int_op__archdes_logical_operation_1
   :included_by: comp_arc_int__kvs__file_storage_component_interface
