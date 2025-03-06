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

Getting Started
###############

.. doc_getstrt:: Getting Started on Implementation
   :id: doc_getstrt__imp__getstrt
   :status: valid
   :tags: Implementation

This document describes the steps which need to be done to document detailed design and implement the code.

Therefore a detailed guideline :need:`gd_guidl__implementation` is available.


Relevant Documents
******************

**Concept Document:** :need:`doc_concept__imp__concept` provides a high-level overview of the integration concept.
**Implementation Guideline:** :need:`gd_guidl__implementation` Details on the implemenation.
**SW Development Plan:** <Link to SW Development Plan> Process description of SW development including
- selection of design and programming language
- design guideline
- coding guideline (e.g. MISRA, can also include style guide or naming convention)
- SW configuration guideline
- Method selection (e.g. for Architecture Verification)
- development tools


Tooling Support
***************

Compiler selection
==================
<TBD>


CI/CD Pipeline
==============

Description which Static Code Analysis Tools <TBD>, Compiler <TBD>, Unit Test Tool <TBD>, Structural Coverage
 Tool <TBD>, are implmented in the CI/CD Pipeline.

Developer Experience
====================

For all RST files also a linter is configured, it will be automatically run in the CI upon check-in.
Locally it can be run via

.. code-block:: shell

   bazel test //:format.check
   bazel build //docs
