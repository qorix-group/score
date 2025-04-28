Feature Architecture : persistency/key_val_storage
==================================================

Overview
--------

- key_val_storage provides the capability to efficiently store, retrieve, and
  manage key-value pairs in a persistent storage system.

Description
-----------

- key_val_storage organize data as pairs, where each unique key is associated with a specific value.
  The key acts as a unique identifier for getting the value.
- The data is persisted in JSON format to the file system, providing a human-readable,
  and widely supported way to store and manage key-value pairs.
- The JSON data persisted is according to RFC-8259.

Rationale Behind Architecture Decomposition
*******************************************

- The architecture is decomposed to include a dedicated JSON parser component (TinyJSON) to facilitate the persistent storage of data in JSON format.
- The architecture is decomposed to include a FileStorage component (fs) to read and write to the file system.


Static Architecture
-------------------

.. feat_arc_sta:: Static Architecture
   :id: FEAT_ARC_STA__persistency_key_val_storage__key_value_storage
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_static_view.puml

Dynamic Architecture
--------------------

.. feat_arc_dyn:: KVS Builder
   :id: FEAT_ARC_DYN__persistency_key_val_storage__builder_pattern
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_dyn_builder.puml

.. feat_arc_dyn:: Check if key contains default value
   :id: FEAT_ARC_DYN__persistency_key_val_storage__check_key_default_value
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__default_values,FEAT_REQ__KVS__default_value_retrieval
   :status: valid

   .. uml:: _assets/kvs_dyn_check_value_default.puml

.. feat_arc_dyn:: Delete key from KVS instance
   :id: FEAT_ARC_DYN__persistency_key_val_storage__delete_key
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b
   :status: valid

   .. uml:: _assets/kvs_dyn_delete_data_key.puml

.. feat_arc_dyn:: Flush to permanent storage
   :id: FEAT_ARC_DYN__persistency_key_val_storage__flush
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__persist_data,FEAT_REQ__KVS__persistency,FEAT_REQ__KVS__snapshots,FEAT_REQ__KVS__integrity_check,FEAT_REQ__KVS__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_flush_local_repr_to_file.puml

.. feat_arc_dyn:: Read key value
   :id: FEAT_ARC_DYN__persistency_key_val_storage__read_key
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__supported_datatypes_keys,FEAT_REQ__KVS__supported_datatypes_values,FEAT_REQ__KVS__default_values,FEAT_REQ__KVS__default_value_retrieval
   :status: valid

   .. uml:: _assets/kvs_dyn_read_data_key.puml

.. feat_arc_dyn:: Read data from permanent storage
   :id: FEAT_ARC_DYN__persistency_key_val_storage__read_data_from_perm_storage
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__persist_data,FEAT_REQ__KVS__persistency,FEAT_REQ__KVS__integrity_check,FEAT_REQ__KVS__snapshots
   :status: valid

   .. uml:: _assets/kvs_dyn_read_file_into_local_repr.puml

.. feat_arc_dyn:: Write value to key
   :id: FEAT_ARC_DYN__persistency_key_val_storage__write_key
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__supported_datatypes_keys,FEAT_REQ__KVS__supported_datatypes_values
   :status: valid

   .. uml:: _assets/kvs_dyn_write_data_key.puml

.. feat_arc_dyn:: Restore snapshop
   :id: FEAT_ARC_DYN__persistency_key_val_storage__snapshot_restore
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__snapshots,FEAT_REQ__KVS__persist_data,FEAT_REQ__KVS__persistency
   :status: valid

   .. uml:: _assets/kvs_dyn_restore_snapshot.puml


Logical Interfaces
------------------

.. feat_arc_int:: Ikvs
   :id: FEAT_ARC_INT__persistency_key_val_storage__keyvaluestorage
   :security: YES
   :safety: ASIL_B
   :satisfies: FEAT_REQ__KVS__safety_asil_b,FEAT_REQ__KVS__stable_api
   :status: valid

   .. uml:: _assets/kvs_interface.puml
