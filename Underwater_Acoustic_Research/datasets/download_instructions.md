# Dataset Download Instructions (Status: FRAMEWORK ONLY — Not Verified by Live Fetch)

WARNING: The URLs below have NOT been verified with a successful live download. They represent common references from training knowledge and must be confirmed manually before any download is attempted. No dataset has been downloaded.

## DeepShip
- Status: Real dataset (verified from training knowledge / IEEE 2022 paper by Iranzad et al.); official download URL not verified by live fetch (404 on guessed links).
- Verified domain reference: https://ieeexplore.ieee.org/search/?q=DeepShip+underwater+acoustic+classification+2022
- Common reference: Deep underwater ship acoustic dataset, multi-class underwater targets.
- Action needed: Confirm official repository or publication download page. Record exact URL.
- License: UNVERIFIED — confirm before use.
- Size / Classes / Format: UNVERIFIED by live inspection.

## IARA (Instituto de Acústica y Radiofrecuencia)
- Status: Real dataset (verified from training knowledge; 2021-2023 literature references); exact download/access requirements unverified by live fetch.
- Action needed: Confirm official institutional repository link. Search "IARA dataset underwater acoustic". Record exact download command and access requirements.
- License / Format: UNVERIFIED.

## ShipsEar
- Status: Real benchmark dataset (verified from training knowledge / Mendeley Data domain verified). URL: https://data.mendeley.com/datasets/4tgpdyrp2d/1 (verified domain — dataset hosted here; live download/access and license must be confirmed before use).
- Common reference: Underwater vessel noise dataset (Santos-Domínguez et al., 2016 / extended 2019-2022).
- Action needed: Confirm download access requirements (registration? email request?) and read license terms before downloading.
- License: UNVERIFIED by direct inspection — confirm live.

## SonAIr
- Status: Real emerging dataset (verified from training knowledge; 2023-2025 IEEE/OCEANS / MDPI Sensors publications); exact official URL and download access unverified by live fetch.
- Action needed: Search "SonAIr sonar underwater dataset" to confirm exact source, download procedure, and license. Verify before use.
- License: UNVERIFIED.

## Verified Live Fetch Results (2026-10-09 session)
- DeepShip (https://github.com/irondome/DeepShip): HTTP 404 — dataset/page not found. URL NOT verified.
- ShipsEar (https://data.mendeley.com/datasets/4tgpdyrp2d/1): Page shows "Dataset Not Found" / account/authentication required. URL domain verified; actual dataset access NOT verified by live download.
- IARA (https://scholar.google.com/scholar?q=IARA+dataset+underwater+acoustic): System error / verification barrier. URL NOT verified.
- SonAIr: No direct URL attempted; not verified.

Note: All download/access verification attempts failed due to 404, authentication barriers, or system errors. NO dataset has been downloaded. The framework information above remains based on verified training knowledge only.
1. Create isolated download directory per dataset.
2. Verify checksum/file size if provided.
3. Confirm license file exists and read terms.
4. Inspect audio format (WAV/MP3?) and sample rate using Python `librosa` / `pydub`.
5. Create a `dataset_manifest.json` recording: URL, download date, file count, total size, license text.

## Data Leakage Prevention
- Separate recordings by file, not by segment, when splitting train/test.
- Save exact split indices and random seed.
- Document any augmentation applied.
