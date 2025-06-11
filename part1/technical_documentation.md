# Technical Documentation – HBnB Project

## Introduction

This document explains the organization of the HBnB project using three diagrams. It shows how the different parts of the application work together from start to finish.

---

## 1. High-Level Package Diagram

📄 [0. High-Level Package Diagram.mmd](0.%20High-Level%20Package%20Diagram%20.mmd)

👉 This diagram shows the main parts of HBnB:  
- Presentation (API, CLI)  
- Business Logic (User, Place, etc.)  
- Storage (files or database)

---

## 2. Detailed Class Diagram for Business Logic Layer

📄 [1. Detailed Class Diagram for Business Logic Layer.mmd](1.%20Detailed%20Class%20Diagram%20for%20Business%20Logic%20Layer%20.mmd)

👉 This diagram shows more details about the classes in the business logic layer.  
It includes objects like `User`, `Place`, `Review`, and a facade (`HBnBFacade`) that manages their interactions.

---

## 3. Sequence Diagrams for API Calls

📄 [2. Sequence Diagrams for API Calls.mmd](2.%20Sequence%20Diagrams%20for%20API%20Calls%20.mmd)

👉 This diagram shows how the application works when using an API:  
The interface (API or CLI) uses a facade to access functions, which then read or save data in files or a database.
