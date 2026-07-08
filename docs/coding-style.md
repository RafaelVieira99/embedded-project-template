# Coding Style

This document defines the coding style used in this embedded project template.

The goal is not to invent a perfect style guide. The goal is to keep code consistent,
readable, testable, and suitable for embedded systems work.

## General Principles

- Prefer simple, explicit code over clever code.
- Keep hardware-dependent code separated from application logic.
- Avoid hidden side effects.
- Check return values.
- Handle errors explicitly.
- Keep functions small and focused.
- Prefer clear names over short names.
- Make timing assumptions visible.
- Document hardware assumptions.

## Language

Firmware code is written in C or C++ depending on the target project.

For C:

- Use C99 or newer.
- Avoid compiler-specific extensions unless documented.
- Prefer fixed-width integer types from `<stdint.h>`.

For C++:

- Use C++17 unless the project states otherwise.
- Avoid unnecessary dynamic allocation in embedded code.
- Avoid exceptions unless explicitly allowed by the project.
- Avoid RTTI unless explicitly allowed by the project.
- Prefer RAII where suitable.
- Keep hardware-facing code predictable and simple.

## Formatting

Formatting is controlled by `.clang-format`.

General rules:

- Indentation: 4 spaces.
- No tabs.
- Maximum line length: 100 characters where practical.
- Always use braces for `if`, `else`, `for`, and `while`.
- Opening braces use the project clang-format style.
- Use one statement per line.

Example:

```c
if (sensor_is_ready()) {
    status = sensor_read(&sample);
} else {
    status = SENSOR_STATUS_NOT_READY;
}
```

## Naming Conventions

### Files

Use lowercase with underscores.

Examples:

```text
sensor_driver.c
sensor_driver.h
uart_cli.c
uart_cli.h
system_status.c
```

### Functions

Use lowercase with underscores.

Examples:

```c
sensor_init();
sensor_read();
uart_cli_process();
system_get_status();
```

### Types

Use a `_t` suffix for C structs and enums.

Examples:

```c
sensor_sample_t
system_status_t
uart_cli_context_t
```

For C++ classes and structs, use PascalCase unless a project-specific convention says otherwise.

### Constants and Macros

Use uppercase with underscores.

Examples:

```c
#define SENSOR_MAX_RETRY_COUNT 3
#define UART_RX_BUFFER_SIZE 128
```

### Variables

Use descriptive lowercase names.

Examples:

```c
uint32_t sample_count;
sensor_status_t sensor_status;
```

## File Organization

- Put public headers in `include/`.
- Put implementation files in `src/`.
- Put automated tests in `tests/`.
- Put build and helper scripts in `scripts/`.
- Put architecture, reports, and delivery documentation in `docs/`.
- Keep hardware-specific code behind driver or abstraction interfaces.

Preferred structure:

```text
application logic
    |
driver interface
    |
hardware abstraction layer
    |
MCU registers / vendor HAL
```

## Error Handling

Functions that can fail should return a status code or another explicit result type.

Example:

```c
typedef enum {
    SENSOR_STATUS_OK = 0,
    SENSOR_STATUS_ERROR,
    SENSOR_STATUS_TIMEOUT,
    SENSOR_STATUS_INVALID_ARGUMENT
} sensor_status_t;
```

Avoid silently ignoring errors.

Bad:

```c
sensor_read(&sample);
```

Good:

```c
sensor_status_t status = sensor_read(&sample);

if (status != SENSOR_STATUS_OK) {
    log_error("sensor_read failed: %d", status);
}
```

## Logging

Use structured log levels:

- `LOG_DEBUG`
- `LOG_INFO`
- `LOG_WARNING`
- `LOG_ERROR`

Logs should include enough context to debug the issue.

Example:

```c
LOG_ERROR("I2C read failed: address=0x%02X status=%d", device_address, status);
```

## Comments

Comments should explain why, not repeat what the code already says.

Bad:

```c
// Increment counter
counter++;
```

Good:

```c
// Count consecutive failures so the watchdog recovery logic can decide
// whether the sensor should be reinitialized.
failure_count++;
```

## Tests

Testable logic should be separated from hardware-specific code.

Where possible:

- Pure logic should have unit tests.
- Hardware drivers should have integration tests.
- Hardware-in-the-loop tests should validate real board behavior.
- Test cases should include valid inputs, invalid inputs, and boundary values.

## Documentation Expectations

Every module should document:

- Purpose.
- Public API.
- Assumptions.
- Error behavior.
- Timing constraints.
- Hardware dependencies.
- Test coverage notes where relevant.

## Deviations

Any intentional deviation from this style should be documented in the relevant file, issue,
or pull request.
