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

Key-value Storage
#################

.. document:: Persistency Key-Value-Store
   :id: DOC__Persistency_Kvs
   :status: draft
   :safety: ASIL_B
   :tags: contribution_request, feature_request


Feature flag
============

To activate this feature, use the following feature flag:

``persistency_kvs``


Abstract
========

This feature request describes the key-value storage that is needed by
applications to store either temporary or permanent data in an easy way that
conforms to most programming languages that provide a hash, hashmap, dictionary
or similar data structure. Access to the KVS is possible from any support
language through language specific interfaces.


Motivation
==========

The current solutions availabkle mostly don't meet the specific needs of the
S-CORE project like storing specific datatypes without a BASE64 conversation or
having no rollback/replay feature. Also the integration into analysis tools is
simpler when the solution grows with the needs instead having to adapt existing
data structures through wrapppers. Especially in the focus of security it will
be possible to build a system that integrates the layers from scratch and
provide them as API to any language whilst still using Rust as the backend.

A main USP of the solution will be the integration of a tracing framework that
allows to understand how events also in the context of other events interact.

A key-value storage is used within many applications to store e.g.
configuration data and is therefore seen crucial for the Eclipse S-CORE
platform.


Rationale
=========

1. There are multiple key-value storages allowed per application.

To allow for data separation and different levels of security, each application
is allowed to have multiple KVS.

2. There must be an update mechanism from different versions of a KVS to another version.

Staying compatible through updates and rollbacks is a main requirement for the
project.

3. The same KVS should be read/writeable from C++ & Rust and any other language.

Having a flexible interface allows to focus on solutions where the language
fits the needs.

4. KVS should store default values.

If possible, all keys should return a configurable default value or the access
should return an error if the key needs to be written first.

5. KVS should use a simple data representation.

The KVS should use a data representation that supports versioned up- and
downgrading like JSON or Cap'n Proto and is easily debugable by the developer.

6. Integrity of the KVS should be checked.

The KVS is always be in a consistent state that either provides the currently
stored data or if not possible the previous snapshot.


Specification
=============

.. feat_req:: C++ & Rust Interoperability
   :id: FEAT_REQ__KVS__cpp_rust_interoperability
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dev_experience__prog_languages, stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow concurrent access via C++ and Rust interfaces.

.. feat_req:: Maximum Size
   :id: FEAT_REQ__KVS__maximum_size
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall have a maximum size defined at compile time.

.. feat_req:: Thread Safety
   :id: FEAT_REQ__KVS__thread_safety
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow thread safe access per key.

.. feat_req:: Multiple KVS per Software Architecture Element
   :id: FEAT_REQ__KVS__multiple_kvs
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow to instantiate multiple key-value storages per software architecture element.

.. feat_req:: Supported Datatypes (Keys)
   :id: FEAT_REQ__KVS__supported_datatypes_keys
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow only UTF-8 encoded strings as keys.

.. feat_req:: Supported Datatypes (Values)
   :id: FEAT_REQ__KVS__supported_datatypes_values
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the storage of primitive and non-primitive datatypes as values.
   The allowed datatypes shall be identical to the ones in the IPC feature.

.. feat_req:: Default Values
   :id: FEAT_REQ__KVS__default_values
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support default values for each key.
   The default values shall be pre-defined in a configuration file.

   Note: Not each key does require a default value.

.. feat_req:: Default Value Retrieval
   :id: FEAT_REQ__KVS__default_value_retrieval
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the retrieval of a key's default value.

.. feat_req:: Default Value Reset
   :id: FEAT_REQ__KVS__default_value_reset
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall allow the reset of a specific key or all keys to its/their default value(s).

.. feat_req:: Persistency
   :id: FEAT_REQ__KVS__persistency
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall store the data persistent. It shall provide an API to trigger the persistency.

.. feat_req:: Integrity Check
   :id: FEAT_REQ__KVS__integrity_check
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall detect data corruption. TODO: Dependent on AoUs.

.. feat_req:: Versioning
   :id: FEAT_REQ__KVS__versioning
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support the versioning of different layouts.

.. feat_req:: Update Mechanism
   :id: FEAT_REQ__KVS__update_mechanism
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall implement a mechanism to support the update from one version to another version.
   In addition, multiple version jumps at once shall be supported.

.. feat_req:: Snapshots
   :id: FEAT_REQ__KVS__snapshots
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store, stkh_req__dev_experience__reprocessing
   :status: valid

   The key-value storage shall allow the explicit creation of snapshots of a specific version and
   shall support the roll-back to previous snapshots, e.g. in case the integrity check fails or an rolled-back update.
   The snapshots shall be associated with an unique ID to be referenced.

   The key-value storage shall allow the deletion of snapshots.

.. feat_req:: Tooling
   :id: FEAT_REQ__KVS__tooling
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functiona_req__support_of_store
   :status: valid

   The key-value storage shall support tooling to view and modify key-value pairs for development and debugging purposes.

.. feat_req:: Stable APIs
   :id: FEAT_REQ__KVS__stable_api
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__reuse_of_app_soft, stkh_req__communication__stable_app_inter
   :status: valid

   The KVS API will be designed to provide a stable interface over the
   lifecylcle without preventing new functionality from beeing implemented.

.. feat_req:: Base on existing standards
   :id: FEAT_REQ__KVS__existing_standards
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__enable_cooperation
   :status: valid

   The KVS will be based on existing standards like a dictionary compatible API
   and a well-known storage format.

.. feat_req:: Variant management support
   :id: FEAT_REQ__KVS__variant_management
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__variant_management
   :status: valid

   The KVS ensures compatibilty between architectures and versions.

.. feat_req:: IP Protection
   :id: FEAT_REQ__KVS__ip_protection
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__ip_protection
   :status: valid

   The KVS will use a licensing model that allows to use it without having to
   disclose IP. Also the used libraries will be carefully selected to ensure
   this.

.. feat_req:: Set default key values via file
   :id: FEAT_REQ__KVS__default_value_file
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS allows to configure default key values by using a file.

.. feat_req:: Configure limits via file
   :id: FEAT_REQ__KVS__config_file
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   The KVS allows to configure memory and other limits by using a config file.

.. feat_req:: Store persistent data
   :id: FEAT_REQ__KVS__persist_data
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__data_persistency
   :status: valid

   The KVS must be able to store and load its data to/from a persistent
   storage.

.. feat_req:: Support ASIL-B
   :id: FEAT_REQ__KVS__safety_asil_b
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__automotive_safety
   :status: valid

   The KVS must support at least ASIL-B.

.. feat_req:: Support engineering and field mode
   :id: FEAT_REQ__KVS__dev_mode
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__safety_features
   :status: valid

   The KVS must support an engineering (developer) and a field mode. The
   engineering must provide a way to to access all data without restrictions.

.. feat_req:: Provide an async API
   :id: FEAT_REQ__KVS__async_api
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__availability, stkh_req__app_architectures__support_request
   :status: valid

   The KVS must provide an async API.

.. feat_req:: Separate data stores
   :id: FEAT_REQ__KVS__access_control
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The KVS must make sure that data stores can only be accessed by allowed components.

.. feat_req:: Data-change events
   :id: FEAT_REQ__KVS__events
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The KVS must provide an API to register callbacks which will be called for
   several events like keys are changed or removed.

.. feat_req:: Fast access
   :id: FEAT_REQ__KVS__fast_access
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__short_app_cycles
   :status: valid

   The KVS must ensure that operations are usually done in under 5 ms.

.. feat_req:: Fast startup
   :id: FEAT_REQ__KVS__fast_startup
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__startup_perf
   :status: valid

   The KVS must ensure that the startup time, besides the time that is needed
   to read the files from the filesystem, must be very short in terms of
   initial parsing and hash checking.

.. feat_req:: Intra-process communication
   :id: FEAT_REQ__KVS__intra_process_comm
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__communication__intra_process
   :status: valid

   The KVS must support concurrent access to the data.

.. feat_req:: Multi-architecture support
   :id: FEAT_REQ__KVS__multi_arch
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__hardware_support__chipset_support
   :status: valid

   The KVS must run on all S-CORE platforms.

.. feat_req:: Logging and tracing
   :id: FEAT_REQ__KVS__log_trace
   :reqtype: Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The KVS must use the provided S-CORE logging and tracing framework.

.. feat_req:: Development steering
   :id: FEAT_REQ__KVS__dev_steering
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__re_requirements__traceability
   :status: valid

   Requirements must be linked to top-level (Stakeholder) requirements.

.. feat_req:: Document requirements as code
   :id: FEAT_REQ__KVS__req_as_code
   :reqtype: Non-Functional
   :security: no
   :safety: ASIL_B
   :satisfies: stkh_req__requirements__as_code
   :status: valid

   Requirements must be documented as code.


Backwards Compatibility
=======================

The API for the specific language tries to represent the language specific
implementation like hashmaps or dictionaries to be mostly backwards compatible
to already existing key-value-storage usage cases. Access without a safe error
handling path, like the array-operator in Rust which can panic, must be
avoided.


Security Impact
===============

Access to the key-value-storage would allow a malicious user to control the
behaviour of the device so it needs to be secured as much as possible, like
only providing debug access when a debug firmware image is installed.


Safety Impact
=============

   .. note::
      One key-value storage should not be used within different processes (freedom from interference) -> To be added to AoUs?

[How could the safety be impacted by the new feature?]

   .. note::
      If there are safety concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.
      ToDo - Link to the Safety Impact Method

[What is the expected ASIL level?]
[What is the expected classification of the contribution?]

   .. note::
      Use the component classification method here to classfiy your component, if it shall to be used in a safety context: (TODO: add link to component classification).


License Impact
==============

   .. note::
      The key-value storage itself uses the Apache-2.0 license. Licenses of
      used libraries are need to be checked.


How to Teach This
=================
