..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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


Quality Report
==============

.. document:: Quality Report
   :id: doc__score_qlm_report
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__qlm_report[version==2]
   :tags:


This document implements :need:`wp__qms_report` and based on the :need:`wp__qms_plan`. It summarizes
the results of the quality related activities. It shall be referred in the :need:`wp__platform_sw_release_note`
of a platform release.

The Quality Report contains:

**1. Quality Overview**

**1.1. Quality Objectives and Goals**
   - Quality objectives and goals as defined in the :need:`wp__qms_plan`
   - Status of achievement of the quality objectives and goals


Quality Objectives

.. list-table:: Standards to comply with
    :header-rows: 1
    :widths: 15,45,15,40

    * - #
      - **Standard Name**
      - **Version**
      - **Status**
    * - 1
      - Automotive SPICE PAM
      - 4.0
      - Requirements fully linked to process descriptions
    * - 2
      - ISO 262626:2018
      - 2018
      - Requirements and workproducts fully linked to process descriptions
    * - 3
      - ISO/SAE 21434:2021
      - 2021
      - Requirements linked to 75%, workproducts linked to 100% to process descriptions
    * - 4
      - ISO PAS 8926:2024 (will be integrated into ISO 26262 3rd edition as updated part 8 clause 12)
      - 2024
      - Requirements and workproducts fully linked to process descriptions


Quality Performance Objectives

.. list-table:: Quality assurance activities and frequency of performing them
    :header-rows: 1

    * - #
      - **Activities**
      - **Cadence**
      - **Status**
    * - 1
      - Platform process audit
      - Once for every platform release or on demand
      - Open
    * - 2
      - Feature process conformance checks
      - Once for every feature release
      - Open
    * - 3
      - Work product review
      - Once for every feature release
      - Open
    * - 4
      - Platform release verification and approval
      - Once for every release
      - Open
    * - 5
      - Process consulting / Quality trainings
      - Continuously
      - On the job, not explicitly documented yet
    * - 6
      - Process monitoring / Process improvement
      - Continuously
      - Open


Quantitative Quality Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Quantitative Quality Goals
    :header-rows: 1

    * - #
      - **Quality Criteria**
      - **Source**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - One Platform process audit per release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the Platform process audit has be done for every release
      - Delta audit allowed to achieve 100%
      - Ensured by the process quality management, :need:`wf__exe_pltprocess_audit` - Platform process audit is available
    * - 2
      - One process conformance check for every feature release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - One process conformance check has been done for every stable feature release
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__qms_report` - Process conformance is available
    * - 3
      - Only quality-assured project/platform work products are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform work products are quality-assured
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__verification_platform_ver_report` - Work products contain the verification of the quality assurance
    * - 4
      - Only quality-assured project/platform releases are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform releases delivered to the community are quality-assured
      - Feature is released as experimental
      - Ensured by the process release management, :need:`wp__platform_sw_release_note` contain the verification and approval of the quality-assurance
    * - 5
      - Only quality-trained personnel are part of the :need:`rl__committer`
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of personnel are trained as per committer role description in :need:`rl__committer`
      - None
      - Ensured by the process platform management, :need:`wp__training_path` contain the training material and evidences for conducted trainings
    * - 6
      - No overdue quality assurance closure activities
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the quality improvement, non-conformance issues are closed
      - None
      - Ensured by the process quality management, :need:`wp__issue_track_system` contain improvements and non-conformance


Work Product Quality Goals

For all generated work products, the following quality goals are defined:

**Quality Criteria**

All work products have to be available and valid. Templates, checklists, and guidelines shall be used.
Plans have to be up to date.

The training material shall be available in the training path.
The issues in the issue tracking system following the planning strategy.

**Target value**

The target value for all work products is 100%.

**Allowed variation**

There is no allowed variation for the work products.

**Metric**

The metric for the work products is ensured by the process that contains the work product. Only valid work products can be merged. Reviews are required and therefore checklists are prepared. If applicable, script based checks are implemented.


**1.2. Lists of all work products**
    - List of all work products, compared to the :need:`wp__qms_plan`
    - Status (valid / invalid)

Quality Management Generic workproducts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: Quality related work products
    :header-rows: 1

    * - Workproduct Id
      - Link to WP
      - Status

    * - :need:`wp__chm_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__chm_plan')`

    * - :need:`wp__document_mgt_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__document_mgt_plan')`

    * - :need:`wp__feat_request`
      - :ref:`documents_docs_features`
      - :ndf:`copy('status', need_id='wp__feat_request')`

    * - :need:`wp__feature_arch`
      - :ref:`documents_docs_features`
      - :ndf:`copy('status', need_id='wp__feature_arch')`

    * - :need:`wp__feature_dfa`
      - :ref:`documents_docs_features`
      - :ndf:`copy('status', need_id='wp__feature_dfa')`

    * - :need:`wp__module_safety_manual`
      - :ref:`documents_docs_modules`
      - :ndf:`copy('status', need_id='wp__module_safety_manual')`

    * - :need:`wp__module_safety_package`
      - :ref:`documents_docs_modules`
      - :ndf:`copy('status', need_id='wp__module_safety_package')`

    * - :need:`wp__module_safety_plan`
      - :ref:`documents_docs_modules`
      - :ndf:`copy('status', need_id='wp__module_safety_plan')`

    * - :need:`wp__module_sw_release_note`
      - :ref:`documents_docs_modules`
      - :ndf:`copy('status', need_id='wp__module_sw_release_note')`

    * - :need:`wp__module_sw_release_plan`
      - :ref:`documents_docs_modules`
      - :ndf:`copy('status', need_id='wp__module_sw_release_plan')`

    * - :need:`wp__platform_dfa`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_dfa')`

    * - :need:`wp__platform_safety_manual`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_safety_manual')`

    * - :need:`wp__platform_safety_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_safety_plan')`

    * - :need:`wp__platform_safety_package`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_safety_package')`

    * - :need:`wp__platform_sw_release_note`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_sw_release_note')`

    * - :need:`wp__platform_sw_release_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__platform_sw_release_plan')`

    * - :need:`wp__prm_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__prm_plan')`

    * - :need:`wp__process_description`
      - :need:`wp__process_description`
      - :ndf:`copy('status', need_id='wp__process_description')`

    * - :need:`wp__process_strategy`
      - :need:`wp__process_strategy`
      - :ndf:`copy('status', need_id='wp__process_strategy')`

    * - :need:`wp__project_mgt`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__project_mgt')`

    * - :need:`wp__qms_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__qms_plan')`

    * - :need:`wp__requirements_feat`
      - :ref:`documents_docs_features`
      - :ndf:`copy('status', need_id='wp__requirements_feat')`

    * - :need:`wp__requirements_inspect`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__requirements_inspect')`

    * - :need:`wp__requirements_stkh`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__requirements_stkh')`

    * - :need:`wp__sw_arch_verification`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__sw_arch_verification')`

    * - :need:`wp__sw_development_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__sw_development_plan')`

    * - :need:`wp__tailoring_work_products`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__tailoring_work_products')`

    * - :need:`wp__tlm_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__tlm_plan')`

    * - :need:`wp__verification_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__verification_plan')`

    * - :need:`wp__verification_platform_int_test`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='wp__verification_platform_int_test')`


**1.3. Lists of all reports**
    - List of all reports, compared to the :need:`wp__qms_plan`
    - Results of the reports

.. list-table:: Quality related work products
    :header-rows: 1

    * - Workproduct Id
       - Link to WP
       - Status

    * - :need:`wp__fdr_reports`
       - :ref:`documents_docs_modules`
       - :ndf:`copy('status', need_id='wp__fdr_reports')`

    * - :need:`wp__process_impr_report`
       - :ref:`project_documents_list`
       - :ndf:`copy('status', need_id='wp__process_impr_report')`

    * - :need:`wp__qms_report`
       - :ref:`project_documents_list`
       - :ndf:`copy('status', need_id='wp__qms_report')`

    * - :need:`wp__tool_verification_report`
       - :ref:`project_documents_list`
       - :ndf:`copy('status', need_id='wp__tool_verification_report')`

    * - :need:`wp__verification_platform_ver_report`
       - :ref:`project_documents_list`
       - :ndf:`copy('status', need_id='wp__verification_platform_ver_report')`

**1.4. Test coverage**
    - Overview of test coverage (overall, requirements, architecture)
    - Ratio of test coverage to the :need:`wp__verification_plan`

**1.5. Issues**
    - List of all issues, compared to the :need:`wp__qms_plan`
    - Status of the issues (open / closed)

**1.6. Process Improvement**
    - List of all process improvements, compared to the :need:`wp__process_impr_report`
    - Status of the process improvements (open / closed)
