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

File Access
###########

.. document:: File Storage Persistency
   :id: DOC__persistency_file_storage
   :status: draft
   :safety: ASIL_B
   :tags: contribution_request, feature_request


Draft notes
===========

- "File Storage Persistency Feature":
   - Additional tooling regarding integrity checking & updating
- "File Storage OSAL":
   - Can just language native APIs be reused?
   - Safety certification of C++ stdlib / Rust lib?
   - Re-implementation of language APIs probably needed due to testability
   - Enforcement of access rights is up to the OS


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_persistency_file_storage``


Abstract
========

This feature request introduces a generic abstraction layer to the file storage
either provided by the underlying operating system or emulated by the platform
layer. It provides thread-safe access to files that can contain any data. It
also ensures that the access is secured by a configurable access model.


Motivation
==========

The simplest solution would be accessing the file system directly by the POSIX
API. As this would heavily rely on the underlying filesystem in regards of
permissions and control this is not a portable solution. This feature provides
a complete API that allows to separate processes and will also pass the safety
certification for ASIL B.


Rationale
=========

The feature must support traceability and all public APIs must be mock- and testable.


Specification
=============

  * https://eclipse-score.github.io/score/requirements/stakeholder/index.html#STKH_REQ__12
  * https://eclipse-score.github.io/score/requirements/stakeholder/index.html#STKH_REQ__8

[Describe the requirements, architecture of any new feature.] or
[Describe the change to requirements, architecture, implementation, process, documentation, infrastructure of any change request.]

   .. note::
      A Feature Request shall specify the stakeholder requirements as part of our platform/project.
      Thereby the :need:`RL_technical_lead` will approve these requirements as part of accepting the Feature Request (e.g. merging the PR with the Feature Request).


Backwards Compatibility
=======================

This feature provides a similar file access API like POSIX so it is possible to
retrofit existing solutions with minimal changes.


Security Impact
===============

[How could a malicious user take advantage of this new feature?]

   .. note::
      If there are security concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.



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
