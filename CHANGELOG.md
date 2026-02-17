# Changelog

All notable changes to this project are documented in this file.

This project follows **Semantic Versioning**  
(https://semver.org)

---

## [Unreleased] — v2.0.0

### Added
- Short CLI alias `ink` as a fully supported alternative to `initstack`
- Plugin-based template system
- External template discovery via `~/.initstack/plugins`
- `doctor` command with plugin validation
- FastAPI template plugin support
- Schema validation for `template.json`

### Changed
- CLI command structure stabilized and hardened
- Template loading now fails safely on invalid plugins
- Improved error reporting for template and plugin issues

### Fixed
- Plugin loading failures causing CLI crashes
- Silent JSON parsing errors in templates
- Template detection inconsistencies

### Planned
- Plugin manager (`ink plugin install | list | remove`)
- Interactive template variables
- Remote plugin repositories
- CI / non-interactive execution mode
- `doctor --fix` automatic repairs

---

## [1.5.0] — 2026-02-17

### Added
- `doctor` command for environment diagnostics
- Local plugin directory detection
- FastAPI template prototype
- Improved CLI feedback and status messages

### Changed
- Internal CLI command routing
- Template resolution logic

### Fixed
- Template discovery edge cases
- CLI crashes on malformed templates

---

## [1.4.0]

### Added
- `initstack new` project scaffolding
- Built-in templates: `cli`, `python`, `web`

---

## [1.0.0]

### Added
- Initial Initstack CLI release
- Project scaffolding engine
- Template-based generation system
