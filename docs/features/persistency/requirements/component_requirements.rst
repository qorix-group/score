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

Component Requirements
######################

.. comp_req:: Key Handling
   :id: comp_req__kvs__key_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__supported_datatypes_keys
   :status: valid

   The system shall ensure that each key consists solely of alphanumeric characters, underscores, or dashes.
   The system shall ensure that each key is encoded as valid UTF-8.
   The system shall guarantee the uniqueness of each key.
   The system shall limit the maximum length of a key to 32 bytes.

.. comp_req:: Value Handling
   :id: comp_req__kvs__value_handling
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__supported_datatypes_values,feat_req__kvs__default_values
   :status: valid

   The system shall only accept values of the following data types: Number, String, Null, Array[Value], or Dictionary{Key:Value}.
   The system shall ensure that all values can be serialized to and deserialized from JSON.
   The system shall restrict the maximum length of a value to 1024 bytes.
   The system shall support unset values and provide a default value in such cases.
   The system shall ensure that, if a value has a default, it is possible to reset the value to its default.

.. comp_req:: Default Value Handling
   :id: comp_req__kvs__default_value_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__default_values,feat_req__kvs__default_value_retrieval,feat_req__kvs__default_value_reset,feat_req__kvs__default_value_file
   :status: valid

   The system may provide default values.
   The system shall ensure that each default value is of a permitted value data type.
   The system shall provide an additional API to retrieve default values.
   The system shall allow configuration of default values either in code or in a separate configuration file.
   The system shall, if default values are stored in a file, secure this file with an associated checksum file.

.. comp_req:: Constraint Configuration
   :id: comp_req__kvs__constraints
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__config_file
   :status: valid

   The system shall allow configuration of KVS constraints at compile-time using source code constants or at runtime using a configuration file.

.. comp_req:: Language Agnostic
   :id: comp_req__kvs__language_agnostic
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__cpp_rust_interoperability
   :status: valid

   The system shall either provide an API that supports bindings to other languages or use a storage and memory exchange format that is adaptable to other languages.

.. comp_req:: Concurrency
   :id: comp_req__kvs__concurrency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__intra_process_comm
   :status: valid

   The system shall implement thread-safe mechanisms to enable concurrent access to data without data races.

.. comp_req:: Multi-Instance
   :id: comp_req__kvs__multi_instance
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__multiple_kvs
   :status: valid

   The system shall manage all runtime variables within an instance, such that multiple KVS instances can be created and used concurrently within a single software architecture element.

.. comp_req:: Persistent Data Storage
   :id: comp_req__kvs__persistent_data_storage
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__persistency,feat_req__kvs__integrity_check,feat_req__kvs__persist_data
   :status: valid

   The system shall use the file API and the JSON data format to persist data.
   The system shall generate a checksum for each data file and store it alongside the data.
   The system shall verify the checksum upon loading data.

.. comp_req:: Persistent Data Schema Handling
   :id: comp_req__kvs__persistent_data_schema
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__versioning,feat_req__kvs__update_mechanism
   :status: valid

   The system shall not provide built-in versioning.
   The chosen JSON file storage format shall enable the application to implement versioning, including upgrade and downgrade paths, as needed.

.. comp_req:: Snapshots
   :id: comp_req__kvs__snapshots
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__snapshots
   :status: valid

   The system shall create a snapshot each time data is stored.
   The system shall maintain a configurable maximum number of snapshots.
   The system shall assign the ID 1 to the newest snapshot and increment the IDs of older snapshots accordingly.
   The system shall rotate and delete the oldest snapshot when the maximum number is reached.
   The system shall allow restoration of a snapshot by its ID.
   The system shall allow deletion of individual snapshots.

.. comp_req:: Develop Mode
   :id: comp_req__kvs__dev_mode
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__dev_mode
   :status: valid

   The system shall provide a developer mode that can be enabled during build time to display debugging and internal information.

.. comp_req:: Async API
   :id: comp_req__kvs__async_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__async_api
   :status: valid

   The system shall provide, in addition to the standard API, an asynchronous API.

.. comp_req:: Permission Handling
   :id: comp_req__kvs__permission_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: feat_req__kvs__access_control
   :status: valid

   The system shall not implement its own access or permission controls but shall rely on the underlying filesystem for permission management.
   The system shall report any access or permission errors encountered at the filesystem level to the application.

.. comp_req:: Callback Support
   :id: comp_req__kvs__callback_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__kvs__events
   :status: valid

   The system shall provide an API for registering callbacks that are triggered by data change events.
