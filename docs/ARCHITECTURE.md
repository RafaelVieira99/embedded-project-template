# Architecture Document Template

## 1. Project Overview

**Project name:** `<project-name>`

**Version:** `<version-or-release>`

**Owner:** `<team-or-person>`

**Date:** `<yyyy-mm-dd>`

### Purpose

Describe what the system does, why it exists, and the problem it solves.

### Scope

Define what is included in this design and what is intentionally out of scope.

## 2. System Context

### External Actors

| Actor | Role | Interface |
| --- | --- | --- |
| `<user/system>` | `<responsibility>` | `<CLI/API/UART/SPI/I2C/etc.>` |

### External Dependencies

| Dependency | Purpose | Version/Constraint |
| --- | --- | --- |
| `<library/tool/hardware>` | `<why it is needed>` | `<version>` |

## 3. Requirements Summary

### Functional Requirements

- `<requirement-id>`: `<expected behavior>`

### Non-Functional Requirements

- Performance: `<latency/throughput/timing target>`
- Reliability: `<fault tolerance/reset behavior>`
- Safety/security: `<constraints>`
- Portability: `<supported platforms/toolchains>`

## 4. High-Level Architecture

Describe the main components and how data/control flows through the system.

```text
<external input>
      |
      v
<module A> --> <module B> --> <output>
```

## 5. Component Design

| Component | Responsibility | Inputs | Outputs | Notes |
| --- | --- | --- | --- | --- |
| `<component>` | `<what it owns>` | `<data/control>` | `<data/control>` | `<constraints>` |

## 6. Interfaces

### Public APIs

| API | Description | Error Handling |
| --- | --- | --- |
| `<function/class/message>` | `<purpose>` | `<return code/exception/status>` |

### Hardware Interfaces

| Interface | Pins/Bus | Protocol | Timing/Rate |
| --- | --- | --- | --- |
| `<UART/SPI/I2C/GPIO/etc.>` | `<mapping>` | `<details>` | `<constraints>` |

## 7. Data Model

Describe important data structures, message formats, configuration values, and persistence rules.

## 8. Error Handling

| Error Condition | Detection | Response | Recovery |
| --- | --- | --- | --- |
| `<condition>` | `<how detected>` | `<system response>` | `<manual/automatic>` |

## 9. Build and Deployment

Describe build targets, compiler/toolchain assumptions, firmware flashing steps, runtime configuration, and deployment artifacts.

## 10. Testing Strategy

Summarize unit, integration, hardware-in-loop, regression, and manual test coverage. Link to `docs/TEST_REPORT.md`.

## 11. Tradeoffs and Decisions

| Decision | Reason | Alternatives Considered |
| --- | --- | --- |
| `<decision>` | `<why>` | `<other options>` |

## 12. Known Limitations

- `<limitation and impact>`

## 13. Future Work

- `<planned improvement>`
