# HOUSEKEEPING & PRE-FLIGHT FOR REBOOT BUILD
## Three-Lane Synchronized Build — Project Sarah

> **Soul Forge Principle:** "The forge feeds the forge." Clean environment, clean build.

---

## PRE-REBOOT HOUSEKEEPING (ALL LANES)

### **1. Environment Cleanup**
```bash
# 1. Clear Python cache
find C:\Users\clint\Desktop\_stem_audit\repos -name "__pycache__" -type d -exec rm -rf {} + 2>$null
find C:\Users\clint\Desktop\_stem_audit\repos -name "*.pyc" -delete 2>$null
find C:\Users\clint\Desktop\_stem_audit\repos -name "*.pyo" -delete 2>$null
find C:\Users\clint\Desktop\_stem_audit\repos -name ".pytest_cache" -type d -exec rm -rf {} + 2>$null

# 2. Clear Node/npm cache (if any)
npm cache clean --force 2>$null

# 3. Clear pip cache
pip cache purge 2>$null

# 4. Clear temporary files
Remove-Item -Path "C:\Users\clint\AppData\Local\Temp\kilo\*" -Recurse -Force -ErrorAction SilentlyContinue 2>$null
Remove-Item -Path "C:\Users\clint\AppData\Local\Temp\*.tmp" -Force -ErrorAction SilentlyContinue 2>$null
```

### **2. Git Hygiene**
```bash
# 1. Verify all repos clean
cd C:\Users\clint\Desktop\_stem_audit\repos
foreach ($repo in (Get-ChildItem -Directory)) {
    Write-Host "=== $($repo.Name) ==="
    cd $repo.Name
    git status --short
    cd ..
}

# 2. Ensure all repos on correct branch
foreach ($repo in @("azazael","azazael-core","cradle","codex-video-engine","ecosystem-orchestrator","esquire-admissibility","flaming-sword","grantforge","hydra-mlcluster","jaeger","krampus","madi","persephone-sync","scribe","shardex","wasm-education","EveUnleashed","eliza","nurse-ratchet","myzticalbabe.github.io","babel","llama-cpp","stem-education-hub","stem-mentorship-matcher","accessibility-audit-framework","stem-assessment-system","stem-inclusion-auditor","stem-facilitator-toolkit")) {
    Write-Host "=== $repo ==="
    cd "C:\Users\clint\Desktop\_stem_audit\repos\$repo"
    git checkout main 2>$null || git checkout master 2>$null
    git pull origin $(git branch --show-current) 2>&1 | Select-Object -Last 1
    cd ..
}
```

### **3. Dependency Verification**
```bash
# 1. Python environment
python --version
python -c "import sys; print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')"

# 2. Core dependencies
python -c "
import torch, transformers, networkx, numpy, mne, brainflow, mediapipe, pouchdb, ipfshttpclient, django, fastapi, uvicorn, pytest, pytest_xdist
print('All core deps OK')
"

# 3. MellifluousML native check
python -c "
from tools.neurodiversity_affirming_engine import MellifluousIntegration
print('MellifluousML Integration OK')
"
```

### **4. Service Health**
```bash
# 1. GitHub CLI
gh auth status

# 2. All 28 repos accessible
$repos = @("azazael","azazael-core","cradle","codex-video-engine","ecosystem-orchestrator","esquire-admissibility","flaming-sword","grantforge","hydra-mlcluster","jaeger","krampus","madi","persephone-sync","scribe","shardex","wasm-education","EveUnleashed","eliza","nurse-ratchet","myzticalbabe.github.io","babel","llama-cpp","stem-education-hub","stem-mentorship-matcher","accessibility-audit-framework","stem-assessment-system","stem-inclusion-auditor","stem-facilitator-toolkit")
foreach ($repo in $repos) {
    $result = gh repo view myzticalbabe/$repo --json name 2>&1
    if ($LASTEXITCODE -eq 0) { Write-Host "✅ $repo" } else { Write-Host "❌ $repo" }
}

# 3. Soul Forge Gate workflow exists on all 28 repos
foreach ($repo in $repos) {
    $workflow = gh api repos/myzticalbabe/$repo/actions/workflows --jq '.workflows[] | select(.name=="Soul Forge Gate") | .name' 2>&1
    if ($workflow) { Write-Host "✅ $repo: Soul Forge Gate" } else { Write-Host "⚠️ $repo: Missing Soul Forge Gate" }
}
```

---

## LANE-SPECIFIC PRE-FLIGHT

### **KILO LANE PRE-FLIGHT**
```bash
cd C:\Users\clint\Desktop\_stem_audit\repos\babel

# 1. Verify MellifluousML backend
python -c "
from tools.neurodiversity_affirming_engine import MellifluousIntegration
integration = MellifluousIntegration()
session = integration.create_harmonic_learning_session('autistic', {'type':'investigation','topic':'patterns'})
print('MellifluousIntegration OK')
"

# 2. Verify Soul Forge Gate workflow
cat .github/workflows/soul-forge-gate.yml

# 3. Verify composite actions
ls -la .github/actions/audit-inclusion/
ls -la .github/actions/audit-accessibility/

# 4. Verify MellifluousML Integration exports
python -c "
from tools.neurodiversity_affirming_engine import MellifluousIntegration, MellifluousMLAdapter, NativeMellifluousBackend
print('All MellifluousML exports OK')
"
```

### **LLM WORKERS LANE PRE-FLIGHT**
```bash
# 1. Verify all engines import
python -c "
from tools.neurodiversity_affirming_engine import (
    CognitiveProfileEngine, NeuroaffirmingLessonGenerator, 
    UniversalPlusDesigner, CognitiveAssetMapper, 
    ExecutiveFunctionScaffoldEngine, SensoryProfileDesigner,
    CommunicationDiversityEngine
)
print('All LLM Worker engines import OK')
"

# 2. Test lesson generation
python -c "
from tools.neurodiversity_affirming_engine import NeuroaffirmingLessonGenerator
g = NeuroaffirmingLessonGenerator()
lesson = g.generate('patterns', '6-8', ['autistic','adhd','dyslexic','dyspraxic'])
print(f'Generated: {lesson.title}')
"

# 3. Test Universal+ Designer
python -c "
from tools.neurodiversity_affirming_engine import UniversalPlusDesigner
d = UniversalPlusDesigner()
base = {'title':'Test','topic':'patterns','grade':'6-8','driving_question':'Test?','duration_minutes':60}
up = d.design_universal_plus(base, ['autistic','adhd','dyslexic','dyspraxic'])
print('Universal+ Designer OK')
"
```

### **FREEBUFF LANE PRE-FLIGHT**
```bash
# 1. Verify Creative Resolution Engine
python -c "
from tools.creative_resolution_engine import CreativeResolutionSynthesizer, AdaptiveEquityCalibrator, BoundaryInfrastructureForInclusion
s = CreativeResolutionSynthesizer()
print('Creative Resolution Engine OK')
"

# 2. Create Community Ethics Board scaffold
mkdir -p tools/creative_resolution_engine/community_ethics_board
# Create models.py, views.py, governance.py, ipfs_integration.py

# 3. Create Community Ethics Board template
cat > COMMUNITY_ETHICS_BOARD_TEMPLATE.md << 'EOF'
# Community Ethics Board Template
## Governance
## Data Sovereignty
## Veto Power
## Membership
## Review Process
EOF
```

---

## REBOOT SEQUENCE

### **Step 1: Full Reboot**
```bash
# 1. Save all work
# 2. Close all applications
# 3. Restart machine
# 4. Wait for full boot + network
```

### **Step 2: Post-Reboot Verification**
```bash
# 1. Wait for network
ping -n 3 github.com

# 2. Verify GitHub CLI
gh auth status

# 3. Quick environment check
python --version
git --version
gh --version
```

### **Step 3: Lane-Specific Verification**
```bash
# KILO
cd C:\Users\clint\Desktop\_stem_audit\repos\babel
python -c "from tools.neurodiversity_affirming_engine import MellifluousIntegration; print('KILO OK')"

# LLM WORKERS
python -c "from tools.neurodiversity_affirming_engine import NeuroaffirmingLessonGenerator; print('LLM WORKERS OK')"

# FREEBUFF
python -c "from tools.creative_resolution_engine import CreativeResolutionSynthesizer; print('FREEBUFF OK')"
```

---

## BUILD EXECUTION COMMANDS

### **KILO LANE — Execute Build**
```bash
cd C:\Users\clint\Desktop\_stem_audit\repos\babel

# 1. Run MellifluousML backend tests
python -m pytest tools/neurodiversity_affirming_engine/mellifluousml_integration.py -v

# 2. Run Soul Forge Gate locally
python tools/audit_inclusion.py --path . --fail-on high
python tools/audit_accessibility.py --path . --fail-on critical
python -c "from tools.creative_resolution_engine import CreativeResolutionSynthesizer; print('Creative Resolution OK')"

# 3. Regenerate domain graphs
cd C:\Users\clint\Desktop\_stem_audit\repos && py -3.13 azazael/tools/domain_trees.py

# 4. Run gap analysis
cd C:\Users\clint\Desktop && py -3.13 _stem_audit/stem_gap_analysis_all_trees.py
```

### **LLM WORKERS — Execute Build (Parallel)**
```bash
cd C:\Users\clint\Desktop\_stem_audit\repos\babel

# Worker 1: Cognitive Profile Registry
python -c "
from tools.neurodiversity_affirming_engine import CognitiveProfileEngine
engine = CognitiveProfileEngine()
for p, spec in engine.registry.get_all_profiles().items():
    print(f'{spec.name}: {[s.name for s in spec.strengths]}')
"

# Worker 2: Lesson Generation (parallel across topics/grades)
python -c "
from tools.neurodiversity_affirming_engine import NeuroaffirmingLessonGenerator
g = NeuroaffirmingLessonGenerator()
topics = ['patterns','structures','data_stories','energy_systems','ecosystems']
grades = ['2','5','7','10']
for t in topics:
    for gr in grades:
        lesson = g.generate(t, gr, ['autistic','adhd','dyslexic','dyspraxic'])
        print(f'Generated: {lesson.id}')
"

# Worker 3: Universal+ Designer
python -c "
from tools.neurodiversity_affirming_engine import UniversalPlusDesigner
d = UniversalPlusDesigner()
base = {'title':'Test','topic':'patterns','grade':'6-8','driving_question':'Test?','duration_minutes':60}
up = d.design_universal_plus(base, ['autistic','adhd','dyslexic','dyspraxic'])
print('Universal+ Designer OK')
"

# Worker 4: Sensory Profile Designer
python -c "
from tools.neurodiversity_affirming_engine import SensoryProfileDesigner
d = SensoryProfileDesigner()
for arch in ['sensory_seeker','sensory_avoider','sensory_sensitive','sensory_registration','mixed_profile']:
    env = d.generate_environment_for_archetype(arch)
    print(f'{arch}: {env[\"archetype\"]}')
"

# Worker 5: Communication Diversity Engine
python -c "
from tools.neurodiversity_affirming_engine import CommunicationDiversityEngine
e = CommunicationDiversityEngine()
for style, asset in e.COMMUNICATION_ASSETS.items():
    print(f'{asset.name}: {asset.collaboration_value[:60]}...')
"

# Worker 6: Executive Function Scaffold Engine
python -c "
from tools.neurodiversity_affirming_engine import ExecutiveFunctionScaffoldEngine
e = ExecutiveFunctionScaffoldEngine()
for profile in ['autistic','adhd','dyslexic','dyspraxic']:
    suite = e.get_scaffold_suite(profile)
    print(f'{profile}: {len(suite[\"scaffolds\"])} scaffolds')
"

# Worker 7: Cognitive Asset Mapper + Team Composition
python -c "
from tools.neurodiversity_affirming_engine import CognitiveAssetAPI
api = CognitiveAssetAPI()
team = [
    {'id':'l1','profile_scores':[('autistic',0.7),('adhd',0.2)]},
    {'id':'l2','profile_scores':[('adhd',0.6),('dyslexic',0.3)]},
    {'id':'l3','profile_scores':[('dyslexic',0.7),('dyspraxic',0.3)]},
    {'id':'l4','profile_scores':[('dyspraxic',0.8),('autistic',0.1)]}
]
result = api.compose_team(team)
print('Team Composition:', result['assignments'])
"

# Worker 8: Integration Test Suite
python -c "
import pytest
import sys
sys.exit(pytest.main(['-xvs', 'tools/neurodiversity_affirming_engine/', '-n', '8']))
"
```

### **FREEBUFF — Execute Build**
```bash
cd C:\Users\clint\Desktop\_stem_audit\repos\babel

# 1. Test Creative Resolution Engine
python -c "
from tools.creative_resolution_engine import CreativeResolutionSynthesizer, AdaptiveEquityCalibrator, BoundaryInfrastructureForInclusion
s = CreativeResolutionSynthesizer()
print('Creative Resolution Engine OK')
"

# 2. Create Community Ethics Board scaffold
mkdir -p tools/creative_resolution_engine/community_ethics_board
# Create models.py, views.py, governance.py, ipfs_integration.py

# 2. Create Community Ethics Board template
cat > COMMUNITY_ETHICS_BOARD_TEMPLATE.md << 'EOF'
# Community Ethics Board Template
## Governance
## Data Sovereignty
## Veto Power
## Membership
## Review Process
EOF

git add COMMUNITY_ETHICS_BOARD_TEMPLATE.md
git commit -m "Add Community Ethics Board Template"
git push origin master
```

---

## POST-BUILD VALIDATION

### **All Lanes — Final Validation**
```bash
# 1. All tests pass
cd C:\Users\clint\Desktop\_stem_audit\repos\babel
python -m pytest tools/ -v --tb=short 2>&1 | tail -20

# 2. Soul Forge Gate passes
python tools/audit_inclusion.py --path . --fail-on high
python tools/audit_accessibility.py --path . --fail-on critical

# 3. Gap analysis clean
cd C:\Users\clint\Desktop && py -3.13 _stem_audit/stem_gap_analysis_all_trees.py

# 4. Domain graphs current
cd C:\Users\clint\Desktop\_stem_audit\repos && py -3.13 azazael/tools/domain_trees.py

# 5. All 28 repos have Soul Forge Gate passing
foreach ($repo in $repos) {
    $checks = gh api repos/myzticalbabe/$repo/check-runs --jq '.check_runs[] | select(.name=="Soul Forge Gate") | .conclusion'
    Write-Host "$repo: $checks"
}
```

---

## RECORD KEEPING

### **Build Log Template**
```markdown
## BUILD LOG — [DATE] — [LANE]

### Start Time: [timestamp]
### End Time: [timestamp]
### Duration: [minutes]

### Completed:
- [ ] Task 1: [description] — [validation]
- [ ] Task 2: [description] — [validation]

### Test Results:
- Unit tests: [pass/fail] — [count]
- Integration tests: [pass/fail] — [count]
- Soul Forge Gate: [pass/fail]

### Blockers:
- Blocker 1: [description] — [resolution]

### Next Actions:
- [ ] Action 1
- [ ] Action 2

### Handoff to Other Lanes:
- [Lane]: [API change / Contract update / Artifact delivered]
```

---

## EMERGENCY ROLLBACK

```bash
# If build fails catastrophically:
# 1. Tag current state
git tag -a "pre-build-$(date +%Y%m%d-%H%M)" -m "Pre-build backup"

# 2. Reset to last known good
git reset --hard HEAD~1
git push origin main --force-with-lease

# 3. Verify rollback
python -c "from tools.neurodiversity_affirming_engine import MellifluousIntegration; print('Rollback OK')"
```

---

## SIGN-OFF

| Checklist | Kilo | LLM Workers | Freebuff |
|---|---|---|---|
| Environment clean | ☐ | ☐ | ☐ |
| Git clean | ☐ | ☐ | ☐ |
| Dependencies verified | ☐ | ☐ | ☐ |
| Services healthy | ☐ | ☐ | ☐ |
| Pre-flight passed | ☐ | ☐ | ☐ |
| Build executed | ☐ | ☐ | ☐ |
| Tests passing | ☐ | ☐ | ☐ |
| Validation clean | ☐ | ☐ | ☐ |

---

**Soul Forge License v1.0 — Tend the fire.**  
**Clean house. Clean build. Three lanes. One forge.**