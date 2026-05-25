#!/bin/bash

cd ~/paper-briefing

echo "=== Daily Paper Briefing Pipeline ==="

python3 generate_report.py

git add .

git commit -m "auto: daily research briefing update"

git push origin main

echo "=== DONE ==="
