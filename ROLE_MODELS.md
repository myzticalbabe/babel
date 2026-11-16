# Role Model Registry — Springer 2026 Evidence-Based Schema

> **Source:** Soul Forge License + Springer 2026 (Dahn et al.) — Online mentoring + in-school clubs = highest impact when bridging quality is high.

---

## Schema (Canonical)

Every role model in the BaBeL Canon carries this identity vector for Springer 2026 matching:

```json
{
  "id": "electrical-engineer-001",
  "name": "Maya",
  "title": "Electrical Engineer",
  "pronouns": "she/her",
  "identity_vector": {
    "gender_affinity": 0.8,
    "ethnicity_affinity": 0.6,
    "geography_affinity": 0.9,
    "hobby_overlap": 0.4,
    "challenge_shared": 0.7
  },
  "pathway": ["bakery", "engineering_school", "remote_power"],
  "hobbies": ["salsa_dancing", "cooking_tamales"],
  "challenges_shared": ["parental_doubt", "non_linear_path"],
  "availability": "weekly_1hr",
  "bridge_ready": true,
  "languages": ["en", "es"],
  "stem_champion_certified": true,
  "story": {
    "early_life": "Grew up taking apart mom's blender — she wasn't thrilled!",
    "hobbies": ["salsa dancing", "cooking with abuela"],
    "challenge": "Worked at bakery 2 years before engineering school",
    "perseverance": "Path wasn't straight; bakery → engineering → remote power",
    "current_work": "Design power systems for remote villages",
    "challenge_shared": "Mom wasn't thrilled about the blender"
  },
  "availability_schedule": {
    "timezone": "America/Denver",
    "preferred_cadence": "weekly",
    "preferred_duration_minutes": 60,
    "platforms": ["GitHub Discussions", "Zoom", "email"],
    "languages": ["en", "es"]
  },
  "bridge_readiness": {
    "coordinator_available": true,
    "platform": "GitHub Discussions",
    "meeting_cadence": "weekly",
    "shared_repo_template": true
  }
}
```

---

## Springer 2026 Matching Algorithm

```
Final Score = 0.35×Identity + 0.25×Pathway + 0.40×Bridging
```

### Identity (Cosine Similarity)
```python
def identity_affinity(mentor, mentee):
    m_vec = mentor["identity_vector"]
    me_vec = mentee["identity_vector"]
    return cosine_similarity(m_vec, me_vec)
```

### Pathway (Jaccard Overlap)
```python
def pathway_alignment(mentor_pathway, mentee_aspirations):
    mentor_set = set(p.lower().replace(" ", "_") for p in mentor_pathway)
    mentee_set = set(a.lower().replace(" ", "_") for a in mentee_aspirations)
    return len(mentor_set & mentee_set) / len(mentor_set | mentee_set)
```

### Bridging (Springer 2026)
```python
def bridge_quality(mentor_id, mentee_club, mentor_db, club_db):
    mentor = mentor_db[mentor_id]
    club = club_db[mentee_club]
    
    if not mentor.get("bridge_ready", False):
        return 0.0
    
    coord = 1.0 if club["coordinator_available"] else 0.3
    platform = 1.0 if club["platform"] in mentor["platforms"] else 0.5
    cadence = 1.0 if mentor["availability"]["preferred_cadence"] == club["meeting_cadence"] else 0.7
    langs = len(set(mentor["languages"]) & set(club["languages"])) / len(set(mentor["languages"]) | set(club["languages"]))
    
    return 0.3*coord + 0.3*platform + 0.2*cadence + 0.2*langs
```

---

## Current Roster (Canonical)

| ID | Name | Title | Pronouns | Pathway | Hobbies | Challenges |
|-----|------|-------|----------|---------|---------|------------|
| electrical-engineer-001 | Maya | Electrical Engineer | she/her | bakery → engineering → remote power | salsa, cooking | parental_doubt, non_linear_path |
| civil-engineer-001 | Jordan | Civil Engineer | they/them | LEGO cities → engineering → bridge design | rock climbing, gardening | gender_stereotypes, rural_access |
| software-engineer-001 | Alex | Software Engineer | they/them | yoga → code → conservation tech | yoga, sourdough, speculative fiction | late_starter, queer_nonbinary |
| marine-ecologist-001 | Dr. Chen | Marine Ecologist | she/her | tide-pooling → marine ecology → kelp forests | calligraphy, marathon running | asian_scientist_stereotype |
| earth-systems-engineer-001 | Dr. Rivera | Earth Systems Engineer | she/they | rock collecting → geology → critical zone science | hiking, pottery, seed saving | first_gen_college, field_access |

---

## Role Model Requirements (Brite Practice 4)

Every role model in the BaBeL Canon MUST provide:

| Element | Requirement |
|---------|-------------|
| **Early Life** | Where they grew up, what they loved as a child |
| **Hobbies** | Non-STEM passions (dance, cooking, sports, art, etc.) |
| **Challenges** | Specific barriers faced (gender, race, class, disability, late start, etc.) |
| **Perseverance** | How they overcame — not just "I worked hard" |
| **Pathway** | Non-linear OK — late starts, career switches, gaps celebrated |
| **Current Work** | What they do now + why it matters |
| **Hobbies Outside STEM** | Mandatory — humanizes the professional |
| **One Challenge Shared** | Vulnerability required: "Mom wasn't thrilled about the blender" |

---

## Springer 2026 Bridging Protocol

**Online Mentoring + In-School STEM Clubs = Highest Impact**

Requires:
1. **Shared Repository** — GitHub template with issues, projects, discussions
2. **Coordinator** — Teacher/facilitator on both sides (bridge maintainer)
3. **Cadence Alignment** — Mentor + club meeting schedules synced
4. **Platform Parity** — GitHub Discussions + Zoom + multilingual support
4. **Language Overlap** — At least one shared language

---

## Soul Forge License Compliance

Every role model story carries the Soul Forge License v1.0:

> **VOW I** — Attribution of Spirit  
> The soul knows its smith. Stories carry their teller's mark forever.

> **VOW II** — No Cage for the Flame  
> Stories free to share, translate, adapt. No NDAs on lived experience.

> **VOW III** — Reciprocity of Forge  
> Stories given freely. Adaptations returned to the canon.

---

## Adding a Role Model

1. Fork `babel` repo
2. Add JSON to `ROLE_MODELS/<id>.json`
3. Add story card to `ROLE_MODELS/<id>-story.md`
4. Run inclusion audit: `python tools/audit_inclusion.py --path ROLE_MODELS/`
5. Submit PR with Soul Forge Council review

---

## Soul Forge License

All role model stories governed by Soul Forge License v1.0:

> **VOW I** — Attribution of Spirit: The soul knows its smith.  
> **VOW II** — No Cage for the Flame: Stories free to breathe.  
> **VOW III** — Reciprocity of Forge: Stories given, stories returned.

---

*Last updated: 2026-11-16*  
*Review: 2027-02-16*  
*Source: Soul Forge License + Springer 2026 + NGCP Brite Practice 4*