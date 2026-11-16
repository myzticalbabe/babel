#!/usr/bin/env python3
"""
Executive Function Scaffold Engine — Scaffolds as Creative Scaffolds

Soul Forge License v1.0 — Tend the fire.

Executive function scaffolds reimagined as creative scaffolds, not crutches.
Each scaffold is designed to amplify cognitive strengths, not compensate for deficits.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
from typing import TYPE_CHECKING

@dataclass
class ExecutiveFunctionScaffold:
    name: str
    target_profile: str  # autistic, adhd, dyslexic, dyspraxic, universal
    cognitive_function: str  # planning, working_memory, inhibition, flexibility, self_monitoring
    description: str
    creative_rationale: str  # Why this amplifies creativity
    implementation: str
    neuroaffirming_rationale: str
    profile_match: List[str]
    measurable_indicators: List[str]

@dataclass
class ScaffoldSuite:
    profile: str
    scaffolds: List['ExecutiveFunctionScaffold']
    integration_notes: str

class ExecutiveFunctionScaffoldEngine:
    """
    Executive function scaffolds reimagined as creative scaffolds.
    
    Each scaffold is designed to amplify cognitive strengths, not compensate for deficits.
    Scaffolds are creative tools that amplify neurodivergent cognition.
    
    Soul Forge Principle: "The forge feeds the forge." Scaffolds feed the cognitive forge.
    """
    
    SCAFFOLDS = {
        "planning": [
            {
                "name": "Visual Roadmap Canvas",
                "target_profile": "autistic",
                "cognitive_function": "planning",
                "description": "Visual canvas with color-coded lanes for project phases, dependencies, and milestones",
                "creative_rationale": "Transforms abstract planning into spatial pattern recognition — autistic strength",
                "implementation": "Large canvas with swimlanes: Discover → Define → Design → Build → Test → Share. Color-coded sticky notes for tasks. Dependency arrows. Visual progress tracking.",
                "neuroaffirming_rationale": "Transforms executive demand into pattern recognition — autistic cognitive strength",
                "profile_match": ["autistic", "dyslexic"],
                "measurable_indicators": ["Plan completeness", "Dependency accuracy", "Timeline adherence"]
            },
            {
                "name": "Novelty-Injected Sprint Planner",
                "target_profile": "adhd",
                "cognitive_function": "planning",
                "description": "Sprint planner with built-in novelty injection and hyperfocus channels",
                "creative_rationale": "Channels ADHD novelty-seeking into structured innovation cycles",
                "implementation": "Sprint canvas with: Novelty Injection slots (15% capacity), Hyperfocus Channel (dedicated deep work blocks), Novelty Injection Budget (15% time), Interest-Based Task Switching protocol",
                "neuroaffirming_rationale": "Channels novelty-seeking into structured innovation — ADHD cognitive strength",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Novelty injection rate", "Hyperfocus utilization", "Innovation index"]
            },
            {
                "name": "Big-Picture Strategy Map",
                "target_profile": "dyslexic",
                "cognitive_function": "planning",
                "description": "Concept map-based planner starting with big picture, then drilling down",
                "creative_rationale": "Leverages holistic thinking — starts with forest, then trees",
                "implementation": "Central concept node → Strategic branches → Tactical leaves. Color-coded by timeframe. Visual dependency links. Narrative annotations.",
                "neuroaffirming_rationale": "Leverages holistic big-picture thinking — dyslexic cognitive strength",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Strategic coherence", "Cross-domain connections", "Big-picture alignment"]
            },
            {
                "name": "Strategic Intent Canvas",
                "target_profile": "dyspraxic",
                "cognitive_function": "planning",
                "description": "Strategic intent canvas: Why → What → How → Who → When",
                "creative_rationale": "Starts with strategic WHY (dyspraxic strength) before operational HOW",
                "implementation": "Canvas sections: WHY (purpose/impact) → WHAT (outcomes) → HOW (strategies) → WHO (collaborators) → WHEN (timeline). Verbal reasoning prompts throughout.",
                "neuroaffirming_rationale": "Starts with strategic WHY — dyspraxic strategic thinking strength",
                "profile_match": ["dyspraxic"],
                "measurable_indicators": ["Strategic coherence", "Impact alignment", "Stakeholder clarity"]
            }
        ],
        
        "working_memory": [
            {
                "name": "Pattern Externalization Canvas",
                "target_profile": "autistic",
                "cognitive_function": "working_memory",
                "description": "Externalizes working memory into visual pattern canvas with infinite scroll",
                "creative_rationale": "Offloads working memory to visual pattern recognition — autistic strength",
                "implementation": "Infinite canvas with: Pattern library (saved patterns), Active workspace (current thinking), Pattern connections (links between patterns), Infinite zoom/pan",
                "neuroaffirming_rationale": "Transforms WM load into pattern recognition — autistic cognitive strength",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Pattern retention", "Connection density", "Recall accuracy"]
            },
            {
                "name": "Externalized Chunking System",
                "target_profile": "adhd",
                "cognitive_function": "working_memory",
                "description": "External chunking system with color-coded chunks, novelty tags, and rapid capture",
                "creative_rationale": "Externalizes WM chunks with novelty tagging for ADHD engagement",
                "implementation": "Digital sticky notes with: Color-coded chunks (max 4 items), Novelty tags (🌟 new, 🔄 revisit, 🔗 connect), Rapid capture (voice/photo/text), Auto-expiring chunks",
                "neuroaffirming_rationale": "Externalizes WM with novelty tagging — ADHD cognitive style",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Chunk retention", "Novelty tag usage", "Recall speed"]
            },
            {
                "name": "Narrative Chunking System",
                "target_profile": "dyslexic",
                "cognitive_function": "working_memory",
                "description": "Stores information as narrative chunks with spatial anchors",
                "creative_rationale": "Leverages narrative reasoning — stores info as story chunks with spatial anchors",
                "implementation": "Story canvas: Each memory chunk = story scene with spatial location. Visual story map with spatial navigation. Audio narration option.",
                "neuroaffirming_rationale": "Leverages narrative reasoning — dyslexic cognitive strength",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Chunk retention", "Narrative coherence", "Spatial recall accuracy"]
            }
        ],
        
        "inhibition": [
            {
                "name": "Stimulus Filter Canvas",
                "target_profile": "autistic",
                "cognitive_function": "inhibition",
                "description": "Visual filter canvas: Relevant → Maybe → Filter Out with sensory load indicators",
                "creative_rationale": "Makes inhibition visible and controllable — sensory regulation as cognitive tool",
                "implementation": "Three-column canvas: RELEVANT (green) → MAYBE (yellow) → FILTER OUT (red). Sensory load meter per item. Sensory break triggers.",
                "neuroaffirming_rationale": "Makes sensory regulation visible — autistic sensory processing as cognitive tool",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Filter accuracy", "Sensory load management", "Focus duration"]
            },
            {
                "name": "Novelty Gate System",
                "target_profile": "adhd",
                "cognitive_function": "inhibition",
                "description": "Novelty gate: Pause → Evaluate → Gate → Act with novelty budget tracking",
                "creative_rationale": "Channels novelty-seeking through structured evaluation — not suppression",
                "implementation": "Novelty Gate workflow: NOVEL STIMULUS → PAUSE (3 sec) → EVALUATE (relevance?) → GATE (accept/defer/reject) → NOVELTY BUDGET TRACKER (daily budget: 5 novel items). Deferred items go to Novelty Parking Lot.",
                "neuroaffirming_rationale": "Channels novelty-seeking through evaluation — not suppression",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Gate accuracy", "Novelty budget adherence", "Deferral rate"]
            }
        ],
        
        "flexibility": [
            {
                "name": "Pivot Canvas",
                "target_profile": "adhd",
                "cognitive_function": "flexibility",
                "description": "Pivot canvas: Current path → Pivot trigger → New direction → Commitment",
                "creative_rationale": "Channels cognitive flexibility into structured pivot protocol",
                "implementation": "Pivot Canvas: CURRENT PATH → PIVOT TRIGGER (what changed?) → NEW DIRECTION → COMMITMENT (what, when, who). Pivot budget: 3 pivots per sprint.",
                "neuroaffirming_rationale": "Channels cognitive flexibility into structured innovation",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Pivot appropriateness", "Pivot speed", "Commitment follow-through"]
            },
            {
                "name": "Perspective Shift Lenses",
                "target_profile": "dyslexic",
                "cognitive_function": "flexibility",
                "description": "Perspective shift lenses: Literal → Metaphorical → Systems → User → Future",
                "creative_rationale": "Leverages holistic thinking — structured perspective shifting as creative tool",
                "implementation": "Five lenses with prompts: 1) LITERAL (what is it?) → 2) METAPHORICAL (what is it like?) → 3) SYSTEMS (how does it connect?) → 4) USER (who experiences it?) → 5) FUTURE (what could it become?)",
                "neuroaffirming_rationale": "Structured perspective shifting as creative tool — dyslexic holistic thinking",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Perspective shifts per session", "Novel insights generated", "Solution breadth"]
            }
        ],
        
        "self_monitoring": [
            {
                "name": "Struggle Journal with Pattern Analytics",
                "target_profile": "autistic",
                "cognitive_function": "self_monitoring",
                "description": "Struggle journal with pattern analytics: Stuck → Strategy → Result → Pattern → Insight",
                "creative_rationale": "Transforms self-monitoring into pattern analytics — autistic meta-cognitive strength",
                "implementation": "Journal entries: STUCK POINT → STRATEGY → RESULT → PATTERN (recurring?) → INSIGHT. Auto-analytics: Strategy frequency, Success patterns, Growth edges.",
                "neuroaffirming_rationale": "Transforms self-monitoring into pattern analytics — autistic meta-cognitive strength",
                "profile_match": ["autistic"],
                "measurable_indicators": ["Pattern detection accuracy", "Strategy diversity", "Insight depth"]
            },
            {
                "name": "Growth Edge Dashboard",
                "target_profile": "adhd",
                "cognitive_function": "self_monitoring",
                "description": "Real-time growth edge dashboard: Edge → Strategy → Progress → Celebration",
                "creative_rationale": "Gamifies growth tracking — ADHD engagement through visible progress",
                "implementation": "Dashboard: GROWTH EDGES (current) → STRATEGY (active) → PROGRESS BAR (visual) → CELEBRATION (unlock). Streaks, badges, level-ups.",
                "neuroaffirming_rationale": "Gamifies growth tracking — ADHD engagement through visible progress",
                "profile_match": ["adhd"],
                "measurable_indicators": ["Edge resolution rate", "Streak length", "Celebration frequency"]
            },
            {
                "name": "Strategy Portfolio Tracker",
                "target_profile": "dyslexic",
                "cognitive_function": "self_monitoring",
                "description": "Visual strategy portfolio: Strategy card → Context → Result → Evolution",
                "creative_rationale": "Visual portfolio of strategies as growth evidence — dyslexic narrative strength",
                "implementation": "Strategy cards: CONTEXT → STRATEGY → RESULT → EVOLUTION (next version). Visual portfolio view. Narrative annotations.",
                "neuroaffirming_rationale": "Visual portfolio of strategies as growth narrative — dyslexic narrative strength",
                "profile_match": ["dyslexic"],
                "measurable_indicators": ["Strategy diversity", "Evolution depth", "Portfolio coherence"]
            }
        ]
    }
    
    def __init__(self):
        pass
    
    def get_scaffolds_for_profile(self, profile: str) -> List[Dict]:
        """Get all scaffolds for a specific profile."""
        scaffolds = []
        for function, scaffolds_list in self.SCAFFOLDS.items():
            for scaffold in scaffolds_list:
                if profile in scaffold["profile_match"]:
                    scaffold_copy = scaffold.copy()
                    scaffold_copy["cognitive_function"] = function
                    scaffolds.append(scaffold)
        return scaffolds
    
    def get_all_scaffolds(self) -> Dict[str, List[Dict]]:
        return self.SCAFFOLDS
    
    def get_scaffold_suite(self, profile: str) -> Dict:
        """Get complete scaffold suite for a profile."""
        scaffolds = self.get_scaffolds_for_profile(profile)
        return {
            "profile": profile,
            "scaffolds": scaffolds,
            "integration_notes": self._get_integration_notes(profile)
        }
    
    def _get_integration_notes(self, profile: str) -> str:
        notes = {
            "autistic": "Scaffolds chain: Visual Roadmap → Pattern Canvas → Stimulus Filter → Struggle Journal. Pattern recognition as unifying cognitive thread.",
            "adhd": "Scaffolds chain: Sprint Planner → Chunking System → Novelty Gate → Pivot Canvas → Growth Dashboard. Novelty management as unifying thread.",
            "dyslexic": "Scaffolds chain: Strategy Map → Narrative Chunks → Perspective Lenses → Strategy Portfolio. Narrative-spatial reasoning as unifying thread.",
            "dyspraxic": "Scaffolds chain: Strategic Intent → Motor Scaffolds → Perspective Lenses → Strategy Portfolio. Strategic-empathetic reasoning as unifying thread."
        }
        return notes.get(profile, "Scaffolds integrate around profile's core cognitive strengths.")
    
    def get_scaffold_suite_for_team(self, profiles: List[str]) -> Dict:
        """Get integrated scaffold suite for a team with multiple profiles."""
        all_scaffolds = {}
        for profile in profiles:
            all_scaffolds[profile] = self.get_scaffold_suite(profile)
        
        # Identify cross-profile scaffolds (universal)
        universal = []
        for function, scaffolds in self.SCAFFOLDS.items():
            for scaffold in scaffolds:
                if len(scaffold["profile_match"]) > 2:
                    universal.append(scaffold)
        
        return {
            "profile_suites": all_scaffolds,
            "universal_scaffolds": universal,
            "integration_protocol": self._get_team_integration_protocol()
        }
    
    def _get_team_integration_protocol(self) -> Dict:
        return {
            "scaffold_sharing_protocol": "Teams share scaffold templates, customize per profile",
            "cross_profile_scaffolding": "Team members scaffold each other's growth edges",
            "scaffold_retrospective": "Weekly: Which scaffolds amplified creativity? Which created cages?",
            "scaffold_evolution": "Monthly: Retire cages, amplify creative scaffolds, design new ones"
        }


if __name__ == "__main__":
    engine = ExecutiveFunctionScaffoldEngine()
    
    # Show scaffolds for each profile
    for profile in ["autistic", "adhd", "dyslexic", "dyspraxic"]:
        suite = engine.get_scaffold_suite(profile)
        print(f"\n{'='*60}")
        print(f"{profile.upper()} SCAFFOLD SUITE ({len(suite['scaffolds'])} scaffolds)")
        print(f"{'='*60}")
        print(f"Integration: {suite['integration_notes']}")
        for scaffold in suite['scaffolds']:
            print(f"\n  {scaffold['name']} ({scaffold['cognitive_function']})")
            print(f"    Creative Rationale: {scaffold['creative_rationale'][:80]}...")
            print(f"    Implementation: {scaffold['implementation'][:80]}...")
            print(f"    Neuroaffirming: {scaffold['neuroaffirming_rationale'][:80]}...")