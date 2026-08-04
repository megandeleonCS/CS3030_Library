#!/usr/bin/env bash
# ==============================================================================
# 3-Hour Sprint: Bash Entrypoint Script
# ==============================================================================
set -euo pipefail  # Strict mode: exit on error, unset vars, or pipe failure

LOG_FILE="execution.log"
INPUT_DIR="./data"

# Simple argument parsing
while [[ $# -gt 0 ]]; do
  case $1 in
    -i|--input)
      INPUT_DIR="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: ./run.sh [--input <directory>]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

log() {
  echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $1" | tee -a "$LOG_FILE"
}

log "🚀 Starting automation tool pipeline..."
log "Target input directory: $INPUT_DIR"

# Execute quality gate check before running
if command -v pylint &> /dev/null; then
    log "🔍 Running quality check (pylint)..."
    pylint tool.py --fail-under=6.0 || log "⚠️ Linting warnings detected."
fi

# Execute main Python utility
python3 tool.py "$INPUT_DIR"

log "✨ Execution complete!"
