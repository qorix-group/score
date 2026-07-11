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


Feature & Enhancement Proposal (FEP) Process
##############################################

.. document:: Feature Request Guideline
  :id: doc__feature_request_guideline
  :status: valid
  :version: 2
  :safety: QM
  :security: NO
  :realizes: wp__training_path[version==1]

.. _feature_request_guideline:

This guide describes how to propose a **Feature & Enhancement Proposal (FEP)** in S-CORE. It applies to *Feature* change requests and to *Feature Modification* change requests with major impact, for example changes affecting the platform or other Feature Teams (see the routing note in the :ref:`Change Management Plan <change_mgmt_plan>` for how that classification is made).

It supersedes the previous ad hoc Feature Request review (GitHub label plus weekly Technical Lead review). Component-level and single-Feature-Team changes are not affected by this guide; they continue through the existing Change Request process described in the :ref:`Change Management Plan <change_mgmt_plan>`.

This guide is based on or references the following documents:

* :need:`FEP Decision Record (DR-002-Proc) <dec_rec__proc__fep_process>`, which records the original decision and its rationale
* :ref:`Change Management Plan <change_mgmt_plan>`, which defines the underlying ISSUE/PR change request infrastructure used by every FEP

.. note::
  This guide describes the FEP process as currently practiced and may evolve as the Architecture Community refines it. :need:`DR-002-Proc <dec_rec__proc__fep_process>` remains the frozen record of what was originally decided; it is not updated when this guide evolves.

Roles
================================

**Author** - the person proposing the change. Responsible for writing and maintaining the FEP, integrating feedback, and driving consensus.

**Shepherd** - an Architecture Community member, not the author, who guides the FEP to maturity and judges when it is ready for the Final Comment Period. Finding a Shepherd is the author's responsibility. If no one is willing to shepherd a proposal, it does not proceed.

**Architecture Community** - all architects and Feature Team leads with standing to review FEPs. During the Final Comment Period, every member is expected to either raise a substantive objection or approve, explicitly or by silence.

The Process: Five Phases
================================

**Phase 0 - Idea Exploration** (informal, no status)

Post the idea informally in the S-CORE architecture channel before writing anything formal. This surfaces obvious problems early, finds prior related proposals, and identifies whether a Shepherd might be willing to pick it up. Move to Phase 1 once you have a willing Shepherd.

**Phase 1 - Draft + Shepherd Shaping** (status: ``Draft``)

Open a PR with your FEP draft, using the FEP template below. A FEP in draft, before a Shepherd is confirmed, does not need a GitHub Issue.

Once a Shepherd is confirmed, open a tracking Issue for the FEP, following the standard Change Request infrastructure described in the :ref:`Change Management Plan <change_mgmt_plan>`, and reference it in the FEP via the ``:tracking:`` field. The Issue links back to the FEP PR, giving bidirectional traceability.

Author and Shepherd iterate until the proposal is complete and well-argued. When the Shepherd judges it ready, they signal readiness for the Final Comment Period. The Architecture Community chair (or proxy) then announces it to the full community.

**Phase 2 - Final Comment Period (FCP)** (status: ``Under Review``)

The Architecture Community has 10 calendar days to engage. Objections must be substantive and technical; the Shepherd distinguishes blocking from non-blocking feedback and can reset the FCP once if a significant new issue requires a revised proposal.

Silence is approval. FCP closes with no unresolved blocking objections, the FEP is accepted. FCP closes with unresolved blocking objections, the FEP is rejected. Escalation may intervene in exceptional cases but is not the default path.

**Phase 3 - Decision** (status: ``Accepted`` | ``Rejected`` | ``Withdrawn``)

If the FCP closed cleanly, the FEP PR is merged and recorded as a Decision Record. If the FCP closed with unresolved blocking objections, the FEP is rejected. The author may withdraw at any point before acceptance.

Breaking Change FEPs additionally require explicit approval from a minimum quorum of Architecture Community members; they cannot pass by silence alone.

**Phase 4 - Implementation Tracking** (status: ``Implementing`` -> ``Implemented``)

The tracking Issue opened in Phase 1 stays open and becomes the implementation tracking artifact. It is closed only when the implementation, not the FEP, is merged. If implementation reveals the accepted design is materially wrong, file a follow-up FEP rather than diverging silently.

FEP Template
================================

.. code-block:: markdown

  # DR-NNN-<Category>: <Short imperative title>

  - **Date:** YYYY-MM-DD

  ```{dec_rec} <Short imperative title>
  :id: dec_rec__<arch|proc|strat|infra|int>__<slug>
  :status: draft
  :tracking: <GitHub issue URL, required once a Shepherd is confirmed>
  :context: <One sentence: what situation or gap makes this proposal necessary?>
  :decision: <One sentence: what is being proposed?>
  ```

  ---

  ## Context / Problem
  <!-- What problem does this solve? Why is the current state insufficient? -->

  ## Decision
  <!-- What is being proposed, precisely? -->

  ## Backwards Compatibility
  <!-- Who is affected? What is the migration path? Remove if not a breaking change. -->

  ## Alternatives Considered
  <!-- What other approaches did you evaluate and why were they rejected? -->

  ## Rationale
  <!-- Why this approach over the alternatives? -->

  ## Consequences
  <!-- What changes after acceptance? What must be implemented, updated, or tracked? -->

  ## Rejected Ideas
  <!-- Ideas raised during FCP that were explicitly not adopted, with rationale. Remove if empty. -->

Breaking Change FEPs - Additional Requirements
================================================

A proposal classified as **Breaking Change** must additionally include:

* **Impact Inventory**: explicit list of known integrators, configurations, or customer deliverables that will break
* **Migration Path**: concrete steps integrators must take, with estimated effort
* **Deprecation Timeline**: if a grace period is offered, how long and how the old behavior is signaled as deprecated
* **Sign-off from Affected Teams**: acknowledgment, not necessarily approval, from leads of teams known to be directly affected before FCP entry
