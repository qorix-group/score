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

Writing Rust Code
#################

.. document:: Coding Guidelines Rust
   :id: doc__rust_coding_guidelines
   :status: valid

Coding Guidelines
=================

The Safety-Critical Rust Consortium plans to develop guidelines, linters,
libraries, static analysis tools, formal methods and language subsets to meet
industrial and legal requirements.

`Safety-Critical Rust Consortium <https://rustfoundation.org/safety-critical-rust-consortium>`_

`Safety-Critical Rust Consortium Guidelines <https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines/>`_

`Learn unsafe Rust <https://google.github.io/learn_unsafe_rust/>`_

`Rust language <https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html>`_

State of Rust Safety-Critical Tooling
#####################################

An actual state of Rust safety critical tooling can be found in the following document:

`Mission statement Rust safety critical tooling <https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/mission-statement.md>`_


Explanation of ARA Applications in Rust
#######################################

Autosar also shares a public availabe document that explains how to use Rust in ARA applications.

`Autosar Rust ARA applications <https://www.autosar.org/fileadmin/standards/R24-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf>`_


MISRA vs Cert
#############

`MISRA vs Cert <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75/>`_

Link to Clippy
##############

`Link to Clippy <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/78/>`_


Conclusions for S-CORE
######################

During the S-CORE project only formatting and clippy checks are enforced. Also
the code should compile with zero warnings. Additional guidelines by the Rust
Community, the Rust Foundation and the Safety-Critical Rust Consortium are
applied where applicable but not enforced. If possible the usage of `unsafe` is
avoided. To keep the code `panic`-free only APIs with a proper return value
should be used.

The adaption of these guidelines will be documented in the S-CORE project
documentation.
