
# AI-316 Lab 02
## System Requirements & Software Architecture for AI Projects

**Course:** AI Project Design and Development (AI-316)  
**Lab:** 02  
**Project:** AI-Powered Smart Automated Attendance and Surveillance System  
**Student:** Shahmeer Abbasi  

---

# Task 1: Functional & Non-Functional Requirements

## 1.1 Functional Requirements

| ID | Functional Requirement | Description |
|----|------------------------|-------------|
| FR-01 | Face Detection | The system shall detect human faces from the camera/video input. |
| FR-02 | Face Recognition | The system shall identify registered students using the trained AI model. |
| FR-03 | Attendance Logging | The system shall record the student's attendance with date and time. |
| FR-04 | Database Synchronization | The system shall store and synchronize attendance records with the database. |
| FR-05 | Alert Generation | The system shall generate alerts or logs when an unknown or unrecognized person is detected. |

## 1.2 Non-Functional Requirements

| ID | Non-Functional Requirement | Description |
|----|----------------------------|-------------|
| NFR-01 | Performance | The system should process camera frames with minimum processing delay. |
| NFR-02 | Accuracy | The face recognition model should provide reliable identification of registered students. |
| NFR-03 | Privacy | Student facial data and attendance records must be protected from unauthorized access. |
| NFR-04 | Reliability | The system should continue operating reliably during normal camera and network conditions. |
| NFR-05 | Resource Efficiency | The application should use reasonable CPU, memory, storage, and network resources. |

---

# Task 2: System Boundary, User Persona & Input/Output Mapping

## 2.1 System Actors

| Actor | Responsibility |
|-------|----------------|
| Security Operator | Monitors the system and responds to alerts. |
| Administrator | Manages users, student records, attendance data, and system configuration. |
| Automated Trigger System | Automatically activates detection and generates events based on camera input. |
| Student | Appears in front of the camera and is identified by the system. |

## 2.2 System Inputs

| Input | Description |
|-------|-------------|
| Camera Stream | Live video stream captured from the camera. |
| Image Frames | Individual frames extracted from the video stream. |
| Student Database | Registered student information and facial data. |
| Model Parameters | Configuration required by the AI inference model. |
| Camera Resolution | Resolution of the incoming video stream. |

## 2.3 System Outputs

| Output | Description |
|--------|-------------|
| Detected Face | Location of detected face in the image. |
| Recognition Result | Identity or unknown status of the detected person. |
| Attendance Record | Student ID, date and time of attendance. |
| Alert Notification | Notification for an unknown or suspicious detection. |
| System Log | Record of detection, inference, attendance, and system events. |

## 2.4 Operational Constraints

| Constraint | Description |
|------------|-------------|
| Processing Resources | The system must operate within available CPU and memory resources. |
| Network Bandwidth | Network usage should remain within available bandwidth. |
| Camera Quality | Detection accuracy depends on camera resolution and image quality. |
| Storage | Attendance records and logs require sufficient storage. |
| Processing Delay | Excessive inference delay should be avoided for real-time operation. |

---

# Task 3: Data-Flow Diagram

## 3.1 Level 0 Context Diagram

```mermaid
flowchart LR

Camera[Camera / Video Stream]
Operator[Security Operator]
Admin[Administrator]

System((AI Attendance &\nSurveillance System))

Camera -->|Video Stream| System
System -->|Alerts & Detection Results| Operator
Admin -->|Student Records / Configuration| System
System -->|Attendance Reports / Logs| Admin
