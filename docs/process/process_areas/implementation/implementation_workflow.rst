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

Workflow Implementation
#######################

.. workflow:: Create/Maintain Detailed Design
   :id: wf__impl__detailed_design
   :status: valid
   :tags: implementation
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :input: wp__sw_component_req, wp__sw_component_architecture
   :output: wp__sw_implementation

   Every Unit has a Detailed Design. After the Design the implementation will be done by write the
   Source Code. It will be verified by the Unit Test. It's recommended to use the local build environments
   to avoid unnecessary cycles.

.. workflow:: Create/Perform Unit Test
   :id: wf__impl__unit_test
   :status: valid
   :tags: implementation
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :input: wp__sw_implementation
   :output: wp__sw_unit_test

   Every Unit shall have at least one Unit Test.
