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

Persistency DFA
###############

.. document:: DFA
   :id: doc__persistency_dfa
   :status: draft
   :safety: ASIL_B
   :tags: feature_persistency

   For the DFA the failure initiator list was used to identify potential violations. If a violation doesn't apply, it is not listed here.
   Most of the violations that doesn't apply shall be analysed with the platform feature DFA. It can be shown with the DFA that at
   persistency the freedom from interference is not violated. Persistency is using the component fs and JSON but there are not used in a way that
   it's used in an combination of a feature and it's related safety mechanism.

   All failures will lead to a failure of the persistency feature. The persistency feature is not able to provide the required functionality.
   This must be handled by the application. Due to the deterministic approach, persistency will return the specified results or error codes.

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__config
    :violation_id: SR_01_07
    :violation_cause: Configuration data. Return values might be falsified.
    :mitigates: feat_req__persistency__integrity_check
    :sufficient: yes
    :status: valid

    Integrity check will fail, so the failure will be detected.

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__message_corr
    :violation_id: CO_01_02
    :violation_cause: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information.
    :mitigates: feat_req__persistency__integrity_check
    :sufficient: yes
    :status: valid

    Maybe mitigates is needed. Persistency will be not available or be falsified executed.

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__instert
    :violation_id: CO_01_03
    :violation_cause: Insertion / sequence of information
    :mitigates: feat_req__persistency__integrity_check
    :sufficient: yes
    :status: valid

    Subset of feat_saf_dfa__persistency__static CO_01_02

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__corrup_info
    :violation_id: CO_01_04
    :violation_cause: Corruption of information, inconsistent data
    :mitigates: feat_req__persistency__integrity_check
    :sufficient: yes
    :status: valid

    Subset of feat_saf_dfa__persistency__static CO_01_02

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__deadlock
    :violation_id: UI_01_04
    :violation_cause: Deadlocks.
    :mitigates: aou_req__persistency__appl_design
    :sufficient: yes
    :status: valid

    Deadlocks are not caused by the KVS, but by the application.

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__livelock
    :violation_id: UI_01_05
    :violation_cause: Livelocks
    :mitigates: aou_req__persistency__appl_design
    :sufficient: yes
    :status: valid

    Same consideration as done in feat_saf_dfa__persistency__static UI_01_04

.. feat_saf_dfa:: Persistency
    :verifies: feat_arc_sta__persistency__static
    :id: feat_saf_dfa__persistency__exec_block
    :violation_id: UI_01_06
    :violation_cause: Blocking of execution.
    :mitigates: aou_req__persistency__appl_exec
    :sufficient: yes
    :status: valid

    Execution blocking will make persistency not available.
