# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2024-06-24

### Changed

- `IfdRoughnessBase` no longer takes `roughness_type` parameter.
- Arithmetic roughness is removed.

## [0.2.0] - 2024-06-17

### Added

- `RectIfdRoughness` now computes the average thickness of the coating layer.

## [0.1.2] - 2024-06-15

### Fixed

- Optimal warping path sampling.

## [0.1.1] - 2024-06-14

### Fixed

- `IndexError` from `RectIfdRoughness.draw()`.

## [0.1.0] - 2024-06-12

### Added

- `IfdRoughnessBase`
- `RectIfdRoughness`
