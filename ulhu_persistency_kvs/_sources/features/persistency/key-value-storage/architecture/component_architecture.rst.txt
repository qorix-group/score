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

Component Architecture
######################

Technical Concept Description
*****************************

The key-value-storage feature (KVS) scope is very small so only the KVS itself
and a another component to handle the persistent storage format are defined.

The API is stable for major version releases. Any changes are discussed in the
CFT. Whenever possible, the existing API is not changed and new functionality
is provided by new function calls.

Key-Value-Storage (KVS)
=======================

The KVS is presented like a dictonary or hashmap implementation to the
application with some extra APIs for flushing data, handling snapshots and
other functionality. All API functions guarantee to not panic or throw
exceptions that can't be handled. Error handling has one of the highest
priorities.

All actions are log- and traceable. The component supports productive and
develop environments.

The KVS is multi-threading safe and allows concurrent access to the same store.
Tracking changes can be done by subscribing to specified keys or the whole
store.

Values that are stored behind the keys can be numbers, text, null, arrays or
objects. Objects and arrays can be used to nest values.

A snapshot logic ensures rollback capabilities if something goes wrong.

TinyJSON
========

TinyJSON is used to serialize and deserialize the data as the well-known format
JSON to and from the permanent storage.
