# Test Report Template

## 1. Test Summary

**Project:** `<project-name>`

**Version/commit:** `<version-or-commit-hash>`

**Date:** `<yyyy-mm-dd>`

**Tester:** `<name>`

**Result:** `<pass/fail/conditional pass>`

### Scope

Describe what was tested and what was excluded from this test cycle.

## 2. Test Environment

| Item | Value |
| --- | --- |
| Host OS | `<os/version>` |
| Compiler/toolchain | `<compiler/version>` |
| Build system | `<cmake/make/etc.>` |
| Target hardware | `<board/device/revision>` |
| Test framework | `<ctest/pytest/custom>` |

## 3. Test Strategy

- Unit tests: `<coverage focus>`
- Integration tests: `<coverage focus>`
- Hardware tests: `<coverage focus>`
- Regression tests: `<coverage focus>`
- Manual tests: `<coverage focus>`

## 4. Test Cases

| ID | Test Case | Steps | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- | --- |
| TC-001 | `<name>` | `<steps>` | `<expected>` | `<actual>` | `<pass/fail>` |

## 5. Automated Test Output

```text
<paste relevant ctest/pytest/build output here>
```

## 6. Defects and Observations

| ID | Description | Severity | Status | Notes |
| --- | --- | --- | --- | --- |
| BUG-001 | `<issue>` | `<low/medium/high>` | `<open/fixed/deferred>` | `<notes>` |

## 7. Coverage and Gaps

Describe what is not covered, why it is not covered, and the risk of leaving it uncovered.

## 8. Final Assessment

State whether the project is ready for delivery, blocked, or conditionally accepted.

## 9. Sign-Off

| Role | Name | Date |
| --- | --- | --- |
| Developer | `<name>` | `<yyyy-mm-dd>` |
| Reviewer/client | `<name>` | `<yyyy-mm-dd>` |
