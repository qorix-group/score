..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

- Key-Value Storage is needed because there are (legacy) applications which require a KVS
- There are multiple Key-Value Storages allowed per application
- There must be an update mechanism from different versions of a KVS to another version
- When are modifications persisted? Configurable?
- The same KVS should be read/writeable from C++ & Rust.
- Supported Datatypes: Primitive Datatypes & Non-Primitive Datatypes; To be coordinated with IPC/Communication CTF, to use the same datatypes
- Tooling to modify/access content of KVS "from the outside"
- KVS should store default values
- Integrity of the KVS should be checked
- Only allow keys that are predefined to avoid spelling errors

.. document:: [Your Feature Name]
   :id: DOC__Your_Feature_Name
   :status: draft
   :safety: ASIL_D
   :tags: contribution_request, feature_request

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``DOC_``
    - Adjust ``status`` to be ``valid``
    - Adjust ``asil`` according to your needs
    - Extend ``tags`` according to your needs, but please keep two default tags there


Feature flag
============

This feature is a standard feature that needs no special feature flag.


Abstract
========

This feature request describes the key-value storage that is needed by
applications to store either temporary or permant data in an easy way that
conforms to most programming languages that provide a hash, hashmap, dictionary
or similar. It provides support for commonly used datatypes and will be written
in Rust. Access to the KVS is possible from any support language through
language specific interfaces.


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

[Describe the requirements, architecture of any new feature.] or
[Describe the change to requirements, architecture, implementation, process, documentation, infrastructure of any change request.]

   .. note::
      A Feature Request shall specify the stakeholder requirements as part of our platform/project.
      Thereby the :need:`RL_technical_lead` will approve these requirements as part of accepting the Feature Request (e.g. merging the PR with the Feature Request).


Backwards Compatibility
=======================

The API for the specific language tries to represent the language specific
implementation like hashmaps or dictionaries to be mostly backwards compatible
to already existing key-value-storage usage cases.


Security Impact
===============

Access to the key-value-storage would allow a malicious user to control the
behaviour of the device so it needs to be secured as much as possible, like
only providing debug access when a debug firmware image is installed.


Safety Impact
=============

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

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================
