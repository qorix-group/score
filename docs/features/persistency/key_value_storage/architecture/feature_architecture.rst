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

Feature Architecture : persistency/key_value_storage
====================================================

Overview
--------

- key_value_storage provides the capability to efficiently store, retrieve, and
  manage key-value pairs in a persistent storage system.

Description
-----------

- key_value_storage organize data as pairs, where each unique key is associated with a specific value.
  The key acts as a unique identifier for getting the value.
- The data is persisted in JSON format to the file system, providing a human-readable,
  and widely supported way to store and manage key-value pairs.
- The JSON data persisted is according to RFC-8259.

Rationale Behind Architecture Decomposition
*******************************************

- The architecture is decomposed to include a dedicated JSON parser component (TinyJSON) to facilitate the persistent storage of data in JSON format.
- The architecture is decomposed to include a FileStorage component (fs) to read and write to the file system.


Static Architecture
-------------------

.. feat_arc_sta:: Static Architecture
   :id: feat_arc_sta__key_value_storage__static
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_static_view.puml

Dynamic Architecture
--------------------

.. feat_arc_dyn:: KVS Builder
   :id: feat_arc_dyn__key_value_storage__builder_pattern
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_dyn_builder.puml

.. feat_arc_dyn:: Check if key contains default value
   :id: feat_arc_dyn__key_value_storage__check_key_default
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__default_values,feat_req__key_value_storage__default_value_retrieval
   :status: valid

   .. uml:: _assets/kvs_dyn_check_value_default.puml

.. feat_arc_dyn:: Delete key from KVS instance
   :id: feat_arc_dyn__key_value_storage__delete_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_dyn_delete_data_key.puml

.. feat_arc_dyn:: Flush to permanent storage
   :id: feat_arc_dyn__key_value_storage__flush
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__persist_data,feat_req__key_value_storage__persistency,feat_req__key_value_storage__snapshots,feat_req__key_value_storage__integrity_check,feat_req__key_value_storage__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_flush_local_repr_to_file.puml

.. feat_arc_dyn:: Read key value
   :id: feat_arc_dyn__key_value_storage__read_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__supported_datatypes_keys,feat_req__key_value_storage__supported_datatypes_values,feat_req__key_value_storage__default_values,feat_req__key_value_storage__default_value_retrieval
   :status: valid

   .. uml:: _assets/kvs_dyn_read_data_key.puml

.. feat_arc_dyn:: Read data from permanent storage
   :id: feat_arc_dyn__key_value_storage__read_data_from_perm_storage
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__persist_data,feat_req__key_value_storage__persistency,feat_req__key_value_storage__integrity_check,feat_req__key_value_storage__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_read_file_into_local_repr.puml

.. feat_arc_dyn:: Write value to key
   :id: feat_arc_dyn__key_value_storage__write_key
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__supported_datatypes_keys,feat_req__key_value_storage__supported_datatypes_values
   :status: valid

   .. uml:: _assets/kvs_dyn_write_data_key.puml

.. feat_arc_dyn:: Restore snapshop
   :id: feat_arc_dyn__key_value_storage__snapshot_restore
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__snapshots,feat_req__key_value_storage__persist_data,feat_req__key_value_storage__persistency
   :status: valid

   .. uml:: _assets/kvs_dyn_restore_snapshot.puml


Logical Interfaces
------------------

.. feat_arc_int:: Ikvs
   :id: feat_arc_int__key_value_storage__interface
   :security: YES
   :safety: ASIL_B
   :fulfils: feat_req__key_value_storage__safety_asil_b,feat_req__key_value_storage__stable_api
   :status: valid

   .. uml:: _assets/kvs_interface.puml
