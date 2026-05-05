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


Safety Analysis Checklist
=========================

.. document:: Persistency Safety Analysis Checklist
   :id: doc__persistency_safety_analysis_fdr
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports
   :tags: persistency

**Purpose**
The purpose of this Safety Analysis (DFA and FMEA) checklist template is to collect the topics to be checked during verification of the Safety Analysis.

**Conduct**

As described in :need:`wf__p_formal_rv`, the formal document review is performed by an "external" safety manager:

- reviewer: Uwe Maucher, Volker Häussler

**Checklist**

Please note that the "passed" column must contain "yes" or "no" for each checklist item. Additionally, the remarks column must explain why item passed or did not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also :ref:`review_concept` for further information about reviews in general and inspection in particular.

.. list-table:: General Checklist
      :header-rows: 1
      :widths: 10,10,30,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - 1
        - Are the safety analysis performed according to the defined process and templates? See :ref:`process_requirements_safety_analysis` and also :ref:`FMEA_templates` and :ref:`dfa_templates`
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_841>`
        - Templates for safety analysis are used and the process is followed.

      * - 2
        - Is the result of the safety analysis indicate if the safety requirements are complied?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_842>`
        - The safety analysis results indicate compliance with the requirements.

      * - 3
        - Are for all not complied safety requirements mitigations defined to resolute the non-compliance? The mitigations shall have a direct influence on the violation by prevention, detection or mitigation to reduce the risk to an acceptable level.
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_843>`
        - Yes. All non-compliances have defined mitigations.

      * - 4
        - Are the mitigations effective and implemented?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_844>`
        - The mitigations are effective and have been implemented.

      * - 5
        - Are newly identified hazards adressed to be considered in HARA in the safety manual?
        - NO
        - :need:`[[title]] <std_req__iso26262__analysis_845>`
        - HARA is out of scope / tailored out for this project.

      * - 6
        - Are additional safety-related test cases determined by potential results of the safety analyses?
        - NO
        - :need:`[[title]] <std_req__iso26262__analysis_847>`
        - There are no additional safety-related test cases determined by potential results of the safety analyses.


.. list-table:: DFA Checklist
      :header-rows: 1
      :widths: 10,10,30,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - 1
        - Are the potential dependent failures identified by performming a DFA?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_741>`
        - The potential dependent failures have been identified by performing the DFA.

      * - 2
        - Is it plausible that each potential identified dependent failure that has been identified, will lead to a dependent failure which cause a violation of FFI?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_742>`
        - The identified potential dependent failures are plausible and could lead to a violation of FFI.

      * - 3
        - Are applicable operational situations and operating modes considered?
        - NO
        - :need:`[[title]] <std_req__iso26262__analysis_743>`
        - Not applicable for the project.

      * - 4
        - Are the failure initiators :need:`[[title]] <gd_guidl__dfa_failure_initiators>` suitable and applied?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_744>`
        - Failure initiators are suitable and have been applied in the DFA.

      * - 5
        - Is a rationale provided for each identified potential dependent failure?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_745>`
        - A rationale is provided for each identified potential dependent failure.

      * - 6
        - Are measures defined to resolute the identified potential dependent failures?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_746>`, :need:`[[title]] <std_req__iso26262__analysis_747>`
        - Measures are defined to resolute the identified potential dependent failures.

      * - 7
        - Can be the required level of independence shown for the identified potential dependent failures?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_748>`
        - The required level of independence can be shown for the identified potential dependent failures.

      * - 8
        - Are the templates for DFA used? See :ref:`dfa_templates` and also :ref:`process_requirements_safety_analysis`
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_748>`
        - The templates for DFA are used.

      * - 9
        - Is the DFA performed in a systematic way to identify the potential dependent failures and their effects? Are the failure effect and the mitigation described?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_8410>`
        - The DFA is performed in a systematic way to identify the potential dependent failures and their effects. The failure effect and the mitigation are described.


.. list-table:: FMEA Checklist
      :header-rows: 1
      :widths: 10,10,30,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - 1
        - Are the fault models suitable and applied for the FMEA? See :ref:`fault_models` and also :ref:`process_requirements_safety_analysis`
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_846>`
        - The fault models are suitable and have been applied for the FMEA.

      * - 2
        - Is the FMEA performed in a systmatic way to identify the potential failure modes and their effects? Are the failure effect and the mitigation described?
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_849>`
        - The FMEA is performed in a systematic way to identify the potential failure modes and their effects. The failure effect and the mitigation are described.

      * - 3
        - Are the templates for FMEA used? See :ref:`FMEA_templates` and also :ref:`process_requirements_safety_analysis`
        - YES
        - :need:`[[title]] <std_req__iso26262__analysis_849>`, :need:`[[title]] <std_req__iso26262__analysis_8410>`
        - The templates for FMEA are used.
