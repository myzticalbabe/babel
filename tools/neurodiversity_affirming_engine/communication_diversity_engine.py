#!/usr/bin/env python3
"""
Communication Diversity Engine — Communication Diversity as Collaborative Asset

Soul Forge License v1.0 — Tend the fire.

Communication diversity as collaborative asset — not deficit to accommodate.
Each communication style is a collaborative asset that enriches team intelligence.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
from typing import TYPE_CHECKING

class CommunicationStyle(Enum):
    LITERAL_DIRECT = "literal_direct"          # Autistic: precise, explicit, literal
    METAPHORICAL_NARRATIVE = "metaphorical_narrative"  # Dyslexic: story-based, metaphorical
    RAPID_ASSOCIATIVE = "rapid_associative"    # ADHD: fast, associative, branching
    STRATEGIC_EMPATHETIC = "strategic_empathetic"  # Dyspraxic: strategic, empathetic, verbal
    VISUAL_SPATIAL = "visual_spatial"          # Dyslexic/Autistic: visual, diagrammatic
    PATTERN_SYMBOLIC = "pattern_symbolic"      # Autistic: symbolic, systematic
    GESTURAL_EMBODIED = "gestural_embodied"    # Multi-modal, movement-based
    MULTIMODAL_SYNTHESIS = "multimodal_synthesis"  # Integration of multiple modes

@dataclass
class CommunicationAsset:
    style: CommunicationStyle
    name: str
    description: str
    strengths: List[str]
    ideal_contexts: List[str]
    collaboration_value: str
    translation_bridges: Dict[str, str]  # How to translate to/from other styles
    soul_forge_vow: str

@dataclass
class CommunicationProfile:
    primary_style: CommunicationStyle
    secondary_styles: List[CommunicationStyle]
    assets: List[str]  # CommunicationAsset names
    translation_needs: Dict[str, str]  # What they need translated
    collaboration_preferences: List[str]

class CommunicationDiversityEngine:
    """
    Communication diversity as collaborative asset — not deficit to accommodate.
    
    Each communication style is a collaborative asset that enriches team intelligence.
    Translation bridges enable cross-style collaboration.
    
    Soul Forge Vow I: "The soul knows its smith" — every communication style carries its maker's mark.
    Soul Forge Vow III: "The forge feeds the forge" — communication diversity feeds collective intelligence.
    """
    
    COMMUNICATION_ASSETS = {
        CommunicationStyle.LITERAL_DIRECT: CommunicationAsset(
            style=CommunicationStyle.LITERAL_DIRECT,
            name="Literal Direct",
            description="Precise, explicit, literal communication. Says exactly what is meant.",
            strengths=[
                "Unambiguous communication",
                "Precise technical specification",
                "Clear boundaries and expectations",
                "Logical consistency checking",
                "Pattern-based communication"
            ],
            ideal_contexts=[
                "Technical specifications",
                "Safety-critical communication",
                "Code reviews",
                "System documentation",
                "Logic verification"
            ],
            collaboration_value="Provides unambiguous foundation; prevents misinterpretation; enables precise coordination",
            translation_bridges={
                "metaphorical_narrative": "Translate metaphor → literal: 'What specifically do you mean by...?'",
                "rapid_associative": "Anchor branching: 'Let's capture that idea, then return to...'",
                "strategic_empathetic": "Make implicit explicit: 'What specifically do you need?'",
                "visual_spatial": "Verbalize visual: 'Describe what you see...'",
                "pattern_symbolic": "Shared language: patterns as common language"
            },
            soul_forge_vow="VOW I: Attribution of Spirit — The soul knows its smith. Literal communication honors precise attribution."
        ),
        
        CommunicationStyle.METAPHORICAL_NARRATIVE: CommunicationAsset(
            style=CommunicationStyle.METAPHORICAL_NARRATIVE,
            name="Metaphorical Narrative",
            description="Story-based, metaphorical, narrative communication. Meaning through story and analogy.",
            strengths=[
                "Complex ideas through accessible stories",
                "Emotional resonance and connection",
                "Cross-domain analogy generation",
                "Identity and meaning making",
                "Cultural knowledge transmission"
            ],
            ideal_contexts=[
                "Concept introduction",
                "Stakeholder communication",
                "Vision setting",
                "Culture building",
                "Learning transfer"
            ],
            collaboration_value="Builds shared meaning; enables cross-domain transfer; creates emotional connection",
            translation_bridges={
                "literal_direct": "Extract literal: 'What specifically does this story illustrate?'",
                "rapid_associative": "Anchor story: 'Let's capture that thread...'",
                "strategic_empathetic": "Shared territory: stories as strategic tools",
                "visual_spatial": "Storyboard the narrative",
                "pattern_symbolic": "Extract patterns from narrative"
            },
            soul_forge_vow="VOW I: Attribution of Spirit — Stories carry their teller's mark forever."
        ),
        
        CommunicationStyle.RAPID_ASSOCIATIVE: CommunicationAsset(
            style=CommunicationStyle.RAPID_ASSOCIATIVE,
            name="Rapid Associative",
            description="Fast, branching, associative communication. Ideas generate ideas.",
            strengths=[
                "Rapid idea generation",
                "Cross-domain connection making",
                "Novelty generation",
                "Divergent exploration",
                "Real-time synthesis"
            ],
            ideal_contexts=[
                "Brainstorming",
                "Crisis response",
                "Innovation sessions",
                "Rapid prototyping",
                "Cross-pollination"
            ],
            collaboration_value="Generates possibility space; prevents premature convergence; cross-pollinates",
            translation_bridges={
                "literal_direct": "Capture branches: 'Let's park that branch and return to main trunk...'",
                "metaphorical_narrative": "Story anchor: 'What's the core story here?'",
                "strategic_empathetic": "Strategic filter: 'Which branches serve our goal?'",
                "visual_spatial": "Map the branches",
                "pattern_symbolic": "Find patterns in the branching"
            },
            soul_forge_vow="VOW III: Reciprocity of Forge — The forge feeds the forge. Rapid association feeds collective innovation."
        ),
        
        CommunicationStyle.STRATEGIC_EMPATHETIC: CommunicationAsset(
            style=CommunicationStyle.STRATEGIC_EMPATHETIC,
            name="Strategic Empathetic",
            description="Strategic, empathetic, verbally sophisticated. Meaning through relationship and strategy.",
            strengths=[
                "Strategic framing with human impact",
                "Empathetic stakeholder navigation",
                "Verbal reasoning and articulation",
                "Conflict transformation through empathy",
                "Long-term vision with human centeredness"
            ],
            ideal_contexts=[
                "Stakeholder alignment",
                "Conflict resolution",
                "Vision communication",
                "Mentoring/coaching",
                "Ethical decision making"
            ],
            collaboration_value="Ensures human impact central; translates between technical and human; maintains relationship integrity",
            translation_bridges={
                "literal_direct": "Make explicit: 'What specifically do you need from me?'",
                "rapid_associative": "Strategic filter: 'Which branches serve our north star?'",
                "metaphorical_narrative": "Shared story: 'What's the story we're telling?'",
                "visual_spatial": "Strategic map: 'Show me the territory'",
                "pattern_symbolic": "Strategic pattern: 'What's the underlying pattern?'"
            },
            soul_forge_vow="VOW III: Reciprocity of Forge — The forge feeds the forge. Empathy feeds collective strategy."
        ),
        
        CommunicationStyle.VISUAL_SPATIAL: CommunicationAsset(
            style=CommunicationStyle.VISUAL_SPATIAL,
            name="Visual Spatial",
            description="Visual, diagrammatic, spatial communication. Meaning through space and image.",
            strengths=[
                "Spatial reasoning made visible",
                "Complex systems made navigable",
                "3D mental modeling shared",
                "Spatial relationships made explicit",
                "Mental rotation communicated"
            ],
            ideal_contexts=[
                "Architecture/design reviews",
                "Data visualization",
                "Spatial planning",
                "Molecular modeling",
                "UI/UX design"
            ],
            collaboration_value="Makes invisible spatial reasoning visible; enables shared mental models",
            translation_bridges={
                "literal_direct": "Verbalize visual: 'Describe what you see...'",
                "metaphorical_narrative": "Storyboard the visual",
                "rapid_associative": "Map the branches visually",
                "strategic_empathetic": "Strategic map: 'Show me the territory'",
                "pattern_symbolic": "Pattern map: 'Show the pattern'"
            },
            soul_forge_vow="VOW I: Attribution of Spirit — The soul knows its smith. Visual thinking carries its maker's mark."
        ),
        
        CommunicationStyle.PATTERN_SYMBOLIC: CommunicationAsset(
            style=CommunicationStyle.PATTERN_SYMBOLIC,
            name="Pattern Symbolic",
            description="Symbolic, systematic, pattern-based communication. Meaning through pattern and structure.",
            strengths=[
                "Pattern recognition made explicit",
                "Systematic notation systems",
                "Recursive pattern communication",
                "Algorithmic expression",
                "Formal pattern languages"
            ],
            ideal_contexts=[
                "Algorithm design",
                "Formal verification",
                "Pattern languages",
                "Mathematical proof",
                "System specification"
            ],
            collaboration_value="Creates shared formal language; enables precise coordination; enables composition",
            translation_bridges={
                "literal_direct": "Shared language: precision as common ground",
                "metaphorical_narrative": "Pattern story: 'What pattern does this story follow?'",
                "rapid_associative": "Pattern extraction: 'What patterns in the branching?'",
                "strategic_empathetic": "Strategic pattern: 'What's the generative pattern?'",
                "visual_spatial": "Pattern map: 'Show the pattern'"
            },
            soul_forge_vow="VOW III: Reciprocity of Forge — The forge feeds the forge. Patterns feed collective intelligence."
        ),
        
        CommunicationStyle.GESTURAL_EMBODIED: CommunicationAsset(
            style=CommunicationStyle.GESTURAL_EMBODIED,
            name="Gestural Embodied",
            description="Multi-modal, movement-based communication. Meaning through gesture and body.",
            strengths=[
                "Embodied cognition expressed",
                "Spatial reasoning through gesture",
                "Tacit knowledge externalized",
                "Cross-modal integration",
                "Pre-verbal communication"
            ],
            ideal_contexts=[
                "Design studios",
                "Dance/movement therapy",
                "Physical prototyping",
                "Spatial reasoning tasks",
                "Cross-cultural communication"
            ],
            collaboration_value="Externalizes embodied cognition; bridges verbal-nonverbal; enables pre-verbal communication",
            translation_bridges={
                "literal_direct": "Verbalize gesture: 'What does this movement mean?'",
                "metaphorical_narrative": "Gesture as story: 'What story is this body telling?'",
                "rapid_associative": "Gesture as branch: 'What does this movement suggest?'",
                "visual_spatial": "Gesture as diagram: 'Draw that movement'",
                "strategic_empathetic": "Embodied empathy: 'What does your body know?'"
            },
            soul_forge_vow="VOW II: No Cage for the Flame — Embodied communication cannot be caged."
        ),
        
        CommunicationStyle.MULTIMODAL_SYNTHESIS: CommunicationAsset(
            style=CommunicationStyle.MULTIMODAL_SYNTHESIS,
            name="Multimodal Synthesis",
            description="Integration of multiple communication modes. Fluid translation between modes.",
            strengths=[
                "Cross-modal translation",
                "Adaptive communication",
                "Bridge building between styles",
                "Collective intelligence weaving",
                "Adaptive communication choreography"
            ],
            ideal_contexts=[
                "Facilitation",
                "Cross-disciplinary teams",
                "Inclusive design",
                "Community engagement",
                "Conflict transformation"
            ],
            collaboration_value="Weaves collective intelligence; translates across all styles; enables full participation",
            translation_bridges={
                "literal_direct": "Precision anchor",
                "metaphorical_narrative": "Meaning anchor",
                "rapid_associative": "Possibility generator",
                "strategic_empathetic": "Humanity anchor",
                "visual_spatial": "Spatial anchor",
                "pattern_symbolic": "Structure anchor",
                "gestural_embodied": "Embodied anchor"
            },
            soul_forge_vow="VOW III: Reciprocity of Forge — The forge feeds the forge. Synthesis feeds collective evolution."
        )
    }
    
    def __init__(self):
        pass
    
    def get_asset(self, style: CommunicationStyle) -> 'CommunicationAsset':
        return self.COMMUNICATION_ASSETS.get(style)
    
    def get_all_assets(self) -> Dict[CommunicationStyle, 'CommunicationAsset']:
        return self.COMMUNICATION_ASSETS
    
    def get_translation_bridge(self, from_style: CommunicationStyle, to_style: CommunicationStyle) -> str:
        """Get translation bridge from one style to another."""
        asset = self.COMMUNICATION_ASSETS.get(from_style)
        if asset and to_style.value in asset.translation_bridges:
            return asset.translation_bridges[to_style.value]
        return "No direct bridge — use Multimodal Synthesis as universal translator"
    
    def get_collaboration_value(self, style: CommunicationStyle) -> str:
        asset = self.COMMUNICATION_ASSETS.get(style)
        return asset.collaboration_value if asset else "Unknown style"
    
    def get_ideal_contexts(self, style: CommunicationStyle) -> List[str]:
        asset = self.COMMUNICATION_ASSETS.get(style)
        return asset.ideal_contexts if asset else []
    
    def get_soul_forge_vow(self, style: CommunicationStyle) -> str:
        asset = self.COMMUNICATION_ASSETS.get(style)
        return asset.soul_forge_vow if asset else ""
    
    def build_translation_matrix(self) -> Dict[str, Dict[str, str]]:
        """Build full translation matrix between all styles."""
        matrix = {}
        styles = list(CommunicationStyle)
        for from_style in styles:
            matrix[from_style.value] = {}
            for to_style in styles:
                if from_style != to_style:
                    matrix[from_style.value][to_style.value] = self.get_translation_bridge(from_style, to_style)
                else:
                    matrix[from_style.value][to_style.value] = "Same style — direct communication"
        return matrix
    
    def get_team_translation_protocol(self, team_styles: List[CommunicationStyle]) -> Dict:
        """Generate translation protocol for a team with given styles."""
        protocol = {
            "team_styles": [s.value for s in team_styles],
            "translation_bridges": {},
            "universal_translator": "MULTIMODAL_SYNTHESIS",
            "communication_norms": [
                "Name your communication style when sharing",
                "Request translation explicitly: 'Can you translate that to...?'",
                "Use style name as prefix: '[LITERAL] The spec requires...'",
                "Request clarification: 'I'm hearing [style], is that right?'"
            ],
            "style_awareness_practice": "Daily: Name your style for the day. Weekly: Reflect on translation challenges."
        }
        
        # Build pairwise bridges
        for from_style in team_styles:
            protocol["translation_bridges"][from_style.value] = {}
            for to_style in team_styles:
                if from_style != to_style:
                    protocol["translation_bridges"][from_style.value][to_style.value] = \
                        self.get_translation_bridge(from_style, to_style)
        
        return protocol


class CommunicationProfileBuilder:
    """Builds communication profiles for learners/team members."""
    
    def __init__(self, engine: CommunicationDiversityEngine):
        self.engine = engine
    
    def build_profile(self, learner_id: str, 
                     primary_style: CommunicationStyle,
                     secondary_styles: List[CommunicationStyle] = None) -> Dict:
        """Build communication profile for a learner."""
        if secondary_styles is None:
            secondary_styles = []
        
        primary_asset = self.engine.get_asset(primary_style)
        secondary_assets = [self.engine.get_asset(s) for s in secondary_styles]
        
        return {
            "learner_id": learner_id,
            "primary_style": primary_style.value,
            "secondary_styles": [s.value for s in secondary_styles],
            "primary_asset": primary_style.value,
            "assets": [primary_style.value] + [s.value for s in secondary_styles],
            "translation_needs": self._get_translation_needs(primary_style, secondary_styles),
            "collaboration_preferences": self._get_collab_preferences(primary_style, secondary_styles),
            "soul_forge_vows": [self.engine.get_soul_forge_vow(s) for s in [primary_style] + secondary_styles]
        }
    
    def _get_translation_needs(self, primary: CommunicationStyle, 
                              secondary: List[CommunicationStyle]) -> Dict[str, str]:
        needs = {}
        for secondary_style in secondary:
            needs[secondary_style.value] = self.engine.get_translation_bridge(primary, secondary_style)
        return needs
    
    def _get_collab_preferences(self, primary: CommunicationStyle,
                               secondary: List[CommunicationStyle]) -> List[str]:
        prefs = [f"Prefers {primary.value} communication"]
        for s in secondary:
            prefs.append(f"Can bridge to {s.value}")
        prefs.append("Requests explicit translation when needed")
        prefs.append("Values cognitive diversity in team")
        return prefs


class TeamCommunicationDesigner:
    """Designs team communication architecture."""
    
    def __init__(self, engine: CommunicationDiversityEngine):
        self.engine = engine
    
    def design_team_communication(self, members: List[Dict]) -> Dict:
        """Design team communication architecture from member profiles."""
        # Extract styles
        team_styles = []
        member_profiles = {}
        
        for member in members:
            profile = self.engine.build_profile(
                member["id"],
                CommunicationStyle(member["primary_style"]),
                [CommunicationStyle(s) for s in member.get("secondary_styles", [])]
            )
            member_profiles[member["id"]] = profile
            team_styles.append(CommunicationStyle(member["primary_style"]))
        
        # Generate translation protocol
        protocol = self.engine.get_team_translation_protocol(team_styles)
        
        # Analyze style diversity
        style_counts = {}
        for member in members:
            style = member["primary_style"]
            style_counts[style] = style_counts.get(style, 0) + 1
        
        # Identify translation gaps
        gaps = self._identify_translation_gaps(team_styles)
        
        # Recommend communication architecture
        architecture = self._design_communication_architecture(team_styles)
        
        return {
            "team_styles": {s.value: style_counts.get(s, 0) for s in CommunicationStyle},
            "member_profiles": member_profiles,
            "translation_protocol": protocol,
            "translation_gaps": gaps,
            "communication_architecture": architecture,
            "diversity_score": len([s for s in style_counts if style_counts[s] > 0]) / len(CommunicationStyle)
        }
    
    def _identify_translation_gaps(self, team_styles: List[CommunicationStyle]) -> List[Dict]:
        gaps = []
        for from_style in team_styles:
            for to_style in team_styles:
                if from_style != to_style:
                    bridge = self.engine.get_translation_bridge(from_style, to_style)
                    if "No direct bridge" in bridge:
                        gaps.append({
                            "from": from_style.value,
                            "to": to_style.value,
                            "gap": "No direct translation bridge",
                            "recommendation": "Use Multimodal Synthesis as universal translator"
                        })
        return gaps
    
    def _design_communication_architecture(self, team_styles: List[CommunicationStyle]) -> Dict:
        return {
            "universal_translator": "Multimodal Synthesis (designated translator role)",
            "communication_hubs": {
                "literal_hub": "Literal Direct speakers",
                "narrative_hub": "Metaphorical Narrative speakers", 
                "associative_hub": "Rapid Associative speakers",
                "strategic_hub": "Strategic Empathetic speakers",
                "visual_hub": "Visual Spatial speakers",
                "pattern_hub": "Pattern Symbolic speakers",
                "embodied_hub": "Gestural Embodied speakers",
                "synthesis_hub": "Multimodal Synthesis speakers"
            },
            "cross_hub_bridges": "Synthesis hub translates between all hubs",
            "meeting_protocols": {
                "style_declaration": "Start: 'I'm communicating in [STYLE]'",
                "translation_request": "Explicit: 'Translate to [STYLE] please'",
                "summary_synthesis": "End: Synthesis hub summarizes in all styles"
            },
            "documentation_standards": {
                "multi_style_docs": "Key docs in all team styles",
                "style_tags": "Tag sections: [LITERAL], [NARRATIVE], [VISUAL], etc.",
                "translation_layer": "Maintain translation layer in shared docs"
            }
        }


if __name__ == "__main__":
    engine = CommunicationDiversityEngine()
    builder = CommunicationProfileBuilder(engine)
    designer = TeamCommunicationDesigner(engine)
    
    # Show all communication assets
    print("COMMUNICATION ASSETS:")
    print("="*60)
    for style, asset in engine.COMMUNICATION_ASSETS.items():
        print(f"\n{asset.name} ({style.value})")
        print(f"  Soul Forge Vow: {asset.soul_forge_vow}")
        print(f"  Strengths: {asset.strengths[:3]}...")
        print(f"  Collaboration: {asset.collaboration_value[:80]}...")
    
    # Build sample team
    team = [
        {"id": "dev_1", "primary_style": "literal_direct", "secondary_styles": ["pattern_symbolic"]},
        {"id": "dev_2", "primary_style": "rapid_associative", "secondary_styles": ["metaphorical_narrative"]},
        {"id": "dev_3", "primary_style": "visual_spatial", "secondary_styles": ["pattern_symbolic"]},
        {"id": "dev_4", "primary_style": "strategic_empathetic", "secondary_styles": ["gestural_embodied"]},
        {"id": "dev_5", "primary_style": "multimodal_synthesis", "secondary_styles": []}
    ]
    
    architecture = designer.design_team_communication(team)
    
    print(f"\n\nTEAM COMMUNICATION ARCHITECTURE:")
    print(f"Style Diversity Score: {architecture['diversity_score']:.2%}")
    print(f"Styles Present: {architecture['team_styles']}")
    print(f"Translation Gaps: {len(architecture['translation_gaps'])}")
    print(f"Architecture Hubs: {list(architecture['communication_architecture']['communication_hubs'].keys())}")