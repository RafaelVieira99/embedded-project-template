# Client Delivery Report Template

## 1. Delivery Summary

**Project:** `<project-name>`

**Client:** `<client-name>`

**Delivery date:** `<yyyy-mm-dd>`

**Delivered by:** `<name/team>`

**Delivery status:** `<complete/partial/blocked>`

### Executive Summary

Briefly describe what was delivered, the current state of the project, and any important client-facing notes.

## 2. Delivered Items

| Item | Description | Location |
| --- | --- | --- |
| Source code | `<modules/features included>` | `<repo/path>` |
| Build scripts | `<build automation>` | `<path>` |
| Tests | `<test suite summary>` | `<path>` |
| Documentation | `<architecture/test/user docs>` | `<path>` |
| Binaries/artifacts | `<firmware/executable/package>` | `<path or release link>` |

## 3. Requirements Coverage

| Requirement | Status | Evidence |
| --- | --- | --- |
| `<requirement-id>` | `<done/partial/not done>` | `<test/doc/demo reference>` |

## 4. Build and Run Instructions

```sh
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

Add target-specific flashing, configuration, or runtime instructions here.

## 5. Validation Evidence

Reference test reports, CI runs, screenshots, logs, measurements, or demo recordings.

| Evidence | Result | Link/Location |
| --- | --- | --- |
| `<test run>` | `<pass/fail>` | `<path/url>` |

## 6. Known Issues and Limitations

| Issue | Impact | Recommended Action |
| --- | --- | --- |
| `<issue>` | `<impact>` | `<fix/workaround/defer>` |

## 7. Assumptions

- `<assumption made during implementation>`

## 8. Maintenance Notes

Describe how to extend, test, debug, and maintain the delivered work.

## 9. Acceptance

| Role | Name | Date | Signature/Approval |
| --- | --- | --- | --- |
| Supplier | `<name>` | `<yyyy-mm-dd>` | `<approval>` |
| Client | `<name>` | `<yyyy-mm-dd>` | `<approval>` |
