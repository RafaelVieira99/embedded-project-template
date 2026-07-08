# Coding Style Rules

These rules define the default coding style for this embedded C/C++ project template. Project-specific rules may extend this file, but should not silently contradict it.

## General Rules

- Keep code simple, explicit, and easy to review.
- Prefer small functions with one clear responsibility.
- Avoid hidden global state. Pass dependencies through function arguments or constructors where practical.
- Treat compiler warnings as defects.
- Do not commit generated build output, temporary files, or local IDE state.
- Keep public interfaces stable and documented.

## C++ Rules

- Use C++17 unless the project states otherwise.
- Use `#pragma once` for project headers.
- Use lower_snake_case for functions and variables.
- Use PascalCase for types and classes.
- Use UPPER_SNAKE_CASE only for compile-time constants or macros.
- Prefer `constexpr`, `enum class`, and typed constants over macros.
- Prefer RAII and standard library containers over manual memory management.
- Avoid dynamic allocation in embedded runtime paths unless the architecture explicitly allows it.
- Mark functions `const`, `noexcept`, or `static` where it improves correctness and clarity.
- Include the matching project header first in `.cpp` files, followed by standard/library headers.

## Formatting

- Use 4 spaces for indentation.
- Put braces on their own line for functions and control blocks.
- Keep lines reasonably short; target 100 characters or fewer.
- Add blank lines between logical blocks.
- Do not align code manually with long runs of spaces.

## Error Handling

- Make failure states visible through return values, status types, assertions, or logs.
- Do not ignore return values from APIs that can fail.
- Avoid exceptions in embedded firmware unless the project explicitly enables them.
- Validate external input at module boundaries.

## Testing

- Add or update tests for every behavior change.
- Keep unit tests deterministic and independent.
- Prefer table-driven tests when checking many input/output cases.
- Test edge cases, invalid inputs, and failure paths.
- Keep test output useful for debugging failures.

## Documentation

- Document public interfaces, assumptions, timing constraints, and hardware dependencies.
- Keep `docs/ARCHITECTURE.md`, `docs/TEST_REPORT.md`, and `docs/DELIVERY_REPORT.md` current for delivered work.
- Use comments to explain why code exists when the reason is not obvious from the implementation.

## Git and Review

- Keep commits focused on one logical change.
- Use clear commit messages that explain the reason for the change.
- Do not mix formatting-only changes with behavior changes unless the project owner approves it.
