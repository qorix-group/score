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

Workproducts Implementation
###########################

.. workproduct:: Implementation
   :id: wp__sw_implementation
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__software_10, std_req__iso26262__software_29

   Implementation includes source code and detailed design (e.g. in form of comments or linked graphical representations) and SW configuration (e.g. #ifdef)
   The "how to" is described in the SW Development Plan guidelines

.. workproduct:: Unit test
   :id: wp__sw_unit_test
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__software_11, std_wp__iso26262__software_12, std_req__iso26262__software_29

   Unit testing verifies component requirements and detailed design (traced to). Tooling defined in SW Development Plan and integrated in CI/Build.

.. needextend:: "docs/process/implementation" in docname
   :+tags: implementation
