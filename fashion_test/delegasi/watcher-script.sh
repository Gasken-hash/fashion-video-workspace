#!/usr/bin/env bash
# Script pemantau tugas — dipasang di tiap AI pembantu (Muse).
# Cek file tugas di repo GitHub tiap beberapa menit; kalau ada tugas baru,
# bangunkan agent untuk kerja. Script polos tanpa agent — hemat kuota.
#
# CARA PASANG (sekali saja, lihat PANDUAN_PASANG.md):
# 1. Ganti SLUG_AI di bawah dengan slug kamu (mis. "ai-1").
# 2. Simpan file ini di ~/hooks/scripts/tugas-watch.sh, jadikan executable.
# 3. Daftarkan hook dengan instruksi kerja di bawah.
set -euo pipefail
source "$HATCH_HOOK_RUNTIME"

SLUG_AI="CONTOH-AI-1"
TASK_URL="https://raw.githubusercontent.com/Gasken-hash/fashion-video-workspace/main/tasks/${SLUG_AI}.json"
STATE_FILE="$HOME/hooks/state/tugas-watch-${SLUG_AI}.json"

OLD_HASH=""
if [[ -f "$STATE_FILE" ]]; then
  OLD_HASH="$(jq -r '.hash // empty' "$STATE_FILE" 2>/dev/null || true)"
fi

BODY="$(curl --fail --silent --show-error --max-time 15 "$TASK_URL" 2>&1)" || {
  log "task fetch failed" "{\"error\":\"$(echo "$BODY" | head -c 200 | tr -d '\n' | sed 's/\"/\\"/g')\"}"
  silent "task file unreachable, stay silent"
}

NEW_HASH="$(printf '%s' "$BODY" | sha256sum | cut -d' ' -f1)"
BARU="$(printf '%s' "$BODY" | jq -r '[.tugas[]? | select(.status == "baru")] | length' 2>/dev/null || echo 0)"

if [[ "$NEW_HASH" == "$OLD_HASH" || "$BARU" == "0" ]]; then
  silent "no new task"
fi

# Ada tugas baru — simpan hash dulu (jangan di dry run), baru bangunkan agent.
if [[ "$HATCH_HOOK_DRY_RUN" != "1" ]]; then
  mkdir -p "$(dirname "$STATE_FILE")"
  printf '{"hash": "%s"}\n' "$NEW_HASH" > "$STATE_FILE.tmp"
  mv "$STATE_FILE.tmp" "$STATE_FILE"
fi

IDS="$(printf '%s' "$BODY" | jq -r '[.tugas[]? | select(.status == "baru") | .id] | join(",")' 2>/dev/null || true)"
wake "new task assigned" "{\"task_ids\":\"$IDS\",\"count\":$BARU,\"task_url\":\"$TASK_URL\"}"
