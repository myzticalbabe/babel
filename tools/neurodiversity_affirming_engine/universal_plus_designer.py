#!/usr/bin/env python3
"""
Universal+ Lesson Designer — UDL + Neurodiversity-Specific Creative Extensions

Soul Forge License v1.0 — Tend the fire.

Universal Design for Learning (UDL) + neurodiversity-specific creative extensions.
Extends standard UDL with neurodiversity-specific creative extensions.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .cognitive_profile_registry import CognitiveProfileSpec, CognitiveProfile, CognitiveProfileEngine

@dataclass
class UDLPrinciple:
    principle: str  # engagement, representation, action_expression
    guideline: str
    checkpoints: List[str]
    neuroaffirming_extensions: Dict[str, List[str]]  # Profile-specific extensions

@dataclass
class UniversalPlusLesson:
    base_lesson: Dict[str, Any]
    udl_layer: Dict[str, List[UDLPrinciple]]
    neuroaffirming_layer: Dict[str, Dict[str, List[str]]]  # Profile -> adaptations
    identity_bonus_integration: Dict[str, Any]
    collaborative_structure: Dict[str, Any]
    assessment_integration: Dict[str, Any]

class UDLPrincipleRegistry:
    """Standard UDL 3.0 principles with neuroaffirming extensions."""
    
    PRINCIPLES = {
        "engagement": UDLPrinciple(
            principle="engagement",
            guideline="Provide multiple means of engagement",
            checkpoints=[
                "Optimize individual choice and autonomy",
                "Optimize relevance, value, and authenticity",
                "Minimize threats and distractions",
                "Heighten salience of goals and objectives",
                "Vary demands and resources to optimize challenge",
                "Foster collaboration and community",
                "Promote expectations and beliefs that optimize motivation"
            ],
            neuroaffirming_extensions={
                "autistic": [
                    "Interest-based entry points (special interests as bridges)",
                    "Predictable routine with clear visual schedules",
                    "Choice within structured frameworks",
                    "Special interests as engagement bridges",
                    "Sensory regulation as engagement prerequisite"
                ],
                "adhd": [
                    "Novelty injection at strategic intervals",
                    "Movement integration as engagement mechanism",
                    "Interest-based task switching",
                    "Gamified progress tracking",
                    "Hyperfocus channels as engagement amplifiers"
                ],
                "dyslexic": [
                    "Big-picture framing before details",
                    "Strength-based entry points",
                    "Community relevance framing",
                    "Identity-affirming narratives",
                    "Multimodal relevance anchors"
                ],
                "dyspraxic": [
                    "Strategic framing of challenges",
                    "Empathy-led engagement",
                    "Collaborative purpose framing",
                    "Mentorship as engagement bridge",
                    "Identity-affirming role models"
                ]
            }
        ),
        "representation": UDLPrinciple(
            principle="representation",
            guideline="Provide multiple means of representation",
            checkpoints=[
                "Provide options for perception",
                "Provide options for language and symbols",
                "Provide options for comprehension",
                "Activate or supply background knowledge",
                "Highlight patterns, critical features, big ideas",
                "Guide information processing and visualization",
                "Maximize transfer and generalization"
            ],
            neuroaffirming_extensions={
                "autistic": [
                    "Visual supports for all abstract concepts",
                    "Explicit step-by-step with pattern highlighting",
                    "Predictable representation formats",
                    "Pattern highlighting over linear presentation",
                    "Literal language option with metaphor toggle"
                ],
                "adhd": [
                    "Chunked information with clear boundaries",
                    "Multimodal: visual + verbal + interactive",
                    "Interactive elements for sustained attention",
                    "Color-coded organization systems",
                    "Interactive simulations over static text"
                ],
                "dyslexic": [
                    "Audio alternatives for all text content",
                    "Visual mapping tools (concept maps, diagrams)",
                    "Speech-to-text for all written output",
                    "Narrative framing of abstract concepts",
                    "Dyslexia-friendly fonts and spacing"
                ],
                "dyspraxic": [
                    "Verbal + visual dual coding",
                    "Conceptual over motor representation",
                    "Strategic framing over procedural detail",
                    "Verbal reasoning scaffolds",
                    "Conceptual over procedural emphasis"
                ]
            }
        ),
        "action_expression": UDLPrinciple(
            principle="action_expression",
            guideline="Provide multiple means of action and expression",
            checkpoints=[
                "Provide options for physical action",
                "Provide options for expression and communication",
                "Provide options for executive functions",
                "Vary methods for response and navigation",
                "Optimize access to tools and assistive technologies",
                "Support planning and strategy development",
                "Enhance capacity for monitoring progress"
            ],
            neuroaffirming_extensions={
                "autistic": [
                    "Pattern-based expression modalities",
                    "System modeling as expression",
                    "Structured expression templates",
                    "Parallel deep work expression modes",
                    "System modeling as primary expression"
                ],
                "adhd": [
                    "Rapid prototyping expression modes",
                    "Movement-based expression options",
                    "Verbal + visual hybrid expression",
                    "Burst-work compatible submission formats",
                    "Rapid iteration as valid expression"
                ],
                "dyslexic": [
                    "Verbal explanation as valid evidence",
                    "Visual model construction",
                    "Story-based expression",
                    "Concept map over essay",
                    "Audio/video as primary submission"
                ],
                "dyspraxic": [
                    "Voice dictation as primary input",
                    "Strategic planning over motor execution",
                    "Verbal reasoning as primary expression",
                    "Mentor-scribe collaboration option",
                    "Strategic planning as valid evidence"
                ]
            }
        )
    }

class UniversalPlusDesigner:
    """
    Universal+ Lesson Designer — UDL + Neurodiversity Extensions.
    
    Takes a base lesson and applies:
    1. Standard UDL 3.0 principles
    2. Neurodiversity-specific creative extensions per profile
    3. Identity bonus integration
    4. Collaborative structure optimization
    3. Assessment integration with identity bonus
    """
    
    def __init__(self):
        self.udl_registry = UDLPrincipleRegistry()
    
    def design_universal_plus(self, base_lesson: Dict[str, Any],
                             target_profiles: List[str] = None) -> Dict[str, Any]:
        """
        Transform a base lesson into Universal+ format.
        
        Args:
            base_lesson: Standard lesson dict
            target_profiles: Cognitive profiles to optimize for
            
        Returns:
            Universal+ lesson with UDL + neuroaffirming layers
        """
        if target_profiles is None:
            target_profiles = ["autistic", "adhd", "dyslexic", "dyspraxic"]
        
        # Apply UDL principles
        udl_layer = self._apply_udl_principles(base_lesson, target_profiles)
        
        # Apply neuroaffirming layer
        neuroaffirming_layer = self._apply_neuroaffirming_layer(base_lesson, target_profiles)
        
        # Integrate identity bonus
        identity_bonus = self._integrate_identity_bonus(target_profiles)
        
        # Optimize collaborative structure
        collaborative_structure = self._optimize_collaborative_structure(target_profiles)
        
        # Integrate assessment
        assessment_integration = self._integrate_assessment(target_profiles)
        
        return {
            "base_lesson": base_lesson,
            "udl_layer": udl_layer,
            "neuroaffirming_layer": neuroaffirming_layer,
            "identity_bonus_integration": identity_bonus,
            "collaborative_structure": collaborative_structure,
            "assessment_integration": assessment_integration,
            "metadata": {
                "target_profiles": target_profiles,
                "udl_version": "3.0",
                "neuroaffirming_version": "1.0",
                "soul_forge_version": "2.0.0-hyper-edge"
            }
        }
    
    def _apply_udl_principles(self, lesson: Dict, target_profiles: List[str]) -> Dict:
        """Apply UDL 3.0 principles with neuroaffirming extensions."""
        udl_applied = {}
        
        for principle_name, principle in UDLPrincipleRegistry.PRINCIPLES.items():
            applied = {
                "principle": principle.principle,
                "guideline": principle.guideline,
                "standard_checkpoints": principle.checkpoints,
                "neuroaffirming_extensions": {}
            }
            
            # Apply neuroaffirming extensions for target profiles
            for profile in target_profiles:
                if profile in principle.neuroaffirming_extensions:
                    applied["neuroaffirming_extensions"][profile] = \
                        principle.neuroaffirming_extensions[profile]
            
            udl_applied[principle_name] = applied
        
        return udl_applied
    
    def _apply_neuroaffirming_layer(self, lesson: Dict, target_profiles: List[str]) -> Dict:
        """Apply neuroaffirming adaptations per profile."""
        adaptations = {}
        
        profile_adaptations = {
            "autistic": {
                "engagement": [
                    "Interest-based entry points (special interests as bridges)",
                    "Predictable routine with visual schedule",
                    "Choice within structured framework",
                    "Special interests as engagement bridges",
                    "Sensory regulation as engagement prerequisite"
                ],
                "representation": [
                    "Visual supports for all abstract concepts",
                    "Explicit step-by-step with pattern highlighting",
                    "Predictable representation formats",
                    "Pattern highlighting over linear presentation",
                    "Literal language option with metaphor toggle"
                ],
                "action_expression": [
                    "Pattern-based expression modalities",
                    "System modeling as expression",
                    "Structured expression templates",
                    "Parallel deep work expression modes",
                    "System modeling as primary expression"
                ],
                "identity_affirmation": "Your pattern-seeking mind is a STEM superpower"
            },
            "adhd": {
                "engagement": [
                    "Novelty injection at strategic intervals",
                    "Movement integration as engagement mechanism",
                    "Interest-based task switching",
                    "Gamified progress tracking",
                    "Hyperfocus channels as engagement amplifiers"
                ],
                "representation": [
                    "Chunked information with clear boundaries",
                    "Multimodal: visual + verbal + interactive",
                    "Interactive elements for sustained attention",
                    "Color-coded organization systems",
                    "Interactive simulations over static text"
                ],
                "action_expression": [
                    "Rapid prototyping expression modes",
                    "Movement-based expression options",
                    "Verbal + visual hybrid expression",
                    "Burst-work compatible submission formats",
                    "Rapid iteration as valid expression"
                ],
                "identity_affirmation": "Your rapid-idea brain is an innovation engine"
            },
            "dyslexic": {
                "engagement": [
                    "Big-picture framing before details",
                    "Strength-based entry points",
                    "Community relevance framing",
                    "Identity-affirming narratives",
                    "Multimodal relevance anchors"
                ],
                "representation": [
                    "Audio alternatives for all text content",
                    "Visual mapping tools (concept maps, diagrams)",
                    "Speech-to-text for all written output",
                    "Narrative framing of abstract concepts",
                    "Dyslexia-friendly fonts and spacing"
                ],
                "action_expression": [
                    "Verbal explanation as valid evidence",
                    "Visual model construction",
                    "Story-based expression",
                    "Concept map over essay",
                    "Audio/video as primary submission"
                ],
                "identity_affirmation": "Your big-picture mind sees connections others miss"
            },
            "dyspraxic": {
                "engagement": [
                    "Strategic framing of challenges",
                    "Empathy-led engagement",
                    "Collaborative purpose framing",
                    "Mentorship as engagement bridge",
                    "Identity-affirming role models"
                ],
                "representation": [
                    "Verbal + visual dual coding",
                    "Conceptual over motor representation",
                    "Strategic framing over procedural detail",
                    "Verbal reasoning scaffolds",
                    "Conceptual over procedural emphasis"
                ],
                "action_expression": [
                    "Voice dictation as primary input",
                    "Strategic planning over motor execution",
                    "Verbal reasoning as primary expression",
                    "Mentor-scribe collaboration option",
                    "Strategic planning as valid evidence"
                ],
                "identity_affirmation": "Your empathy and strategy make better human-centered STEM"
            }
        }
        
        for profile in target_profiles:
            if profile in profile_adaptations:
                adaptations[profile] = profile_adaptations[profile]
        
        return adaptations
    
    def _integrate_identity_bonus(self, target_profiles: List[str]) -> Dict[str, Any]:
        """Integrate Soul Forge Identity Bonus (+5% mastery)."""
        return {
            "criteria": [
                {
                    "id": "stem_self_connection",
                    "description": "Learner documents 'I am a STEM person because...'",
                    "weight": 0.25,
                    "neuroaffirming_note": "Your cognitive profile IS your STEM identity"
                },
                {
                    "id": "future_self_named",
                    "description": "Learner names future STEM self: 'I see myself as [role] because...'",
                    "weight": 0.25,
                    "neuroaffirming_note": "Your cognitive profile shapes your STEM future"
                },
                {
                    "id": "struggle_as_growth",
                    "description": "Learner documents struggle strategies as growth evidence",
                    "weight": 0.25,
                    "neuroaffirming_note": "Your struggle strategies ARE your cognitive strengths"
                },
                {
                    "id": "community_impact_named",
                    "description": "Learner names specific community impact of their work",
                    "weight": 0.25,
                    "neuroaffirming_note": "Your cognitive profile shapes your community impact"
                }
            ],
            "bonus": "5% mastery boost when all 4 criteria met",
            "soul_forge_ruling": "Identity bonus is not extra credit — it's soul alignment. Your cognitive profile IS your STEM asset.",
            "tracking": {
                "auto_detect": "Portfolio evidence auto-scans for criteria",
                "learner_ownership": "Learner controls what counts as evidence",
                "portfolio_portable": "Evidence travels with learner (W3C VC)"
            }
        }
    
    def _optimize_collaborative_structure(self, target_profiles: List[str]) -> Dict[str, Any]:
        """Optimize team structure for cognitive diversity."""
        
        # Role definitions optimized for cognitive diversity
        roles = {
            "Pattern Seeker": {
                "description": "Finds patterns, anomalies, system regularities",
                "ideal_profiles": ["autistic"],
                "responsibilities": ["Pattern detection", "Anomaly spotting", "System mapping"],
                "expression_modes": ["Visual mapping", "System diagrams", "Pattern notation"]
            },
            "Innovation Catalyst": {
                "description": "Generates novel ideas, challenges assumptions",
                "ideal_profiles": ["adhd"],
                "responsibilities": ["Idea generation", "Assumption challenging", "Cross-pollination"],
                "expression_modes": ["Rapid sketches", "Verbal brainstorming", "Rapid prototypes"]
            },
            "Systems Architect": {
                "description": "Designs coherent systems from components",
                "ideal_profiles": ["dyslexic", "autistic"],
                "responsibilities": ["System design", "Integration planning", "Architecture"],
                "expression_modes": ["Visual modeling", "Concept maps", "System diagrams"]
            },
            "Prototype Accelerator": {
                "description": "Rapidly builds and tests ideas",
                "ideal_profiles": ["adhd"],
                "responsibilities": ["Rapid prototyping", "Iteration management", "Feedback loops"],
                "expression_modes": ["Rapid builds", "Live demos", "Iteration logs"]
            },
            "Spatial Architect": {
                "description": "Designs spatial/physical solutions",
                "ideal_profiles": ["dyslexic"],
                "responsibilities": ["Spatial design", "Physical layout", "3D modeling"],
                "expression_modes": ["3D models", "Sketches", "Physical prototypes"]
            },
            "Narrative Designer": {
                "description": "Weaves technical concepts into narratives",
                "ideal_profiles": ["dyslexic"],
                "responsibilities": ["Story framing", "Scenario design", "User journeys"],
                "expression_modes": ["Storyboards", "Scenarios", "Verbal narratives"]
            },
            "Empathy Champion": {
                "description": "Ensures human-centered, inclusive outcomes",
                "ideal_profiles": ["dyspraxic"],
                "responsibilities": ["Inclusion audit", "Accessibility review", "User advocacy"],
                "expression_modes": ["Empathy maps", "User stories", "Verbal advocacy"]
            },
            "Strategic Architect": {
                "description": "Long-term strategy with human-centered vision",
                "ideal_profiles": ["dyspraxic"],
                "responsibilities": ["Strategy", "Roadmaps", "Vision"],
                "expression_modes": ["Strategic memos", "Vision docs", "Verbal presentations"]
            }
        }
        
        # Recommend team composition
        available_profiles = set()
        for profile in self.profile_engine.registry.profiles:
            available_profiles.add(profile.value)
        
        recommended_team = {}
        for role_name, role_def in roles.items():
            for profile in role_def["ideal_profiles"]:
                if profile in target_profiles:
                    recommended_team[role_name] = {
                        "assigned_profile": profile,
                        "responsibilities": role_def["responsibilities"],
                        "expression_modes": role_def["expression_modes"],
                        "identity_affirmation": f"Your {profile} cognition makes you ideal for this role"
                    }
                    break
        
        return {
            "roles": roles,
            "recommended_composition": recommended_team,
            "collaboration_protocols": {
                "check_in_cadence": "Every 15 minutes (ADHD-friendly) / 45 minutes (autistic-friendly)",
                "communication_norms": [
                    "Explicit about cognitive needs",
                    "Name your processing style",
                    "Request format changes explicitly"
                ],
                "decision_making": "Consensus with cognitive diversity weighting",
                "conflict_resolution": "Cognitive style translation -> synthesis"
            },
            "cross_profile_bridges": {
                "autistic_adhd": "Pattern Seeker provides structure; Innovation Catalyst provides novelty",
                "autistic_dyslexic": "Pattern Seeker finds patterns; Systems Architect builds systems from patterns",
                "adhd_dyslexic": "Innovation Catalyst generates ideas; Systems Architect builds systems",
                "dyslexic_dyspraxic": "Spatial Architect designs; Empathy Champion ensures inclusion",
                "autistic_dyspraxic": "Pattern Seeker finds structure; Empathy Champion ensures human-centered"
            }
        }
    
    def _integrate_assessment(self, target_profiles: List[str]) -> Dict[str, Any]:
        """Integrate neuroaffirming assessment with identity bonus."""
        return {
            "mastery_levels": {
                "Exploring": {
                    "description": "Copies models, participates when guided, minimal struggle journal",
                    "neuroaffirming": "Building foundation — every expert started here"
                },
                "Developing": {
                    "description": "Adapts models, documents strategies independently",
                    "neuroaffirming": "Your strategies are your cognitive fingerprint"
                },
                "Mastering": {
                    "description": "Creates originals, mentors peers, persists through ambiguity",
                    "neuroaffirming": "Your cognitive profile IS your mastery signature"
                }
            },
            "domains": {
                "Conceptual Understanding": {
                    "weight": 0.30,
                    "neuroaffirming": "Your cognitive profile shapes how you understand"
                },
                "Problem Framing": {
                    "weight": 0.20,
                    "neuroaffirming": "Your cognitive profile shapes what problems you see"
                },
                "Design Process": {
                    "weight": 0.25,
                    "neuroaffirming": "Your cognitive profile IS your design process"
                },
                "Collaboration": {
                    "weight": 0.15,
                    "neuroaffirming": "Your cognitive profile shapes how you collaborate"
                },
                "Identity Reflection": {
                    "weight": 0.10,
                    "neuroaffirming": "Your cognitive profile IS your STEM identity"
                }
            },
            "identity_bonus": {
                "criteria": [
                    {"id": "stem_self_connection", "description": "STEM self-connection documented"},
                    {"id": "future_self_named", "description": "Future STEM self named"},
                    {"id": "struggle_as_growth", "description": "Struggle documented as growth"},
                    {"id": "community_impact_named", "description": "Community impact named"}
                ],
                "bonus": "5% mastery boost",
                "soul_forge_ruling": "Identity bonus is not extra credit — it's soul alignment"
            },
            "neuroaffirming_rubric": {
                "strengths_leveraged": "Evidence of leveraging cognitive strengths",
                "struggle_documented": "Struggle journal with 2+ strategies per challenge",
                "identity_connection": "Explicit STEM-self connection",
                "community_impact": "Authentic community problem addressed"
            }
        }
    
    def generate_universal_plus_lesson(self, base_lesson: Dict, 
                                      target_profiles: List[str] = None) -> Dict:
        """Complete pipeline: base lesson → Universal+ lesson."""
        return self.design_universal_plus(base_lesson, target_profiles)

if __name__ == "__main__":
    # Demo
    designer = UniversalPlusDesigner()
    
    base_lesson = {
        "title": "Pattern Detectives",
        "topic": "patterns",
        "grade": "6-8",
        "driving_question": "How can patterns help us understand our world?",
        "duration_minutes": 60
    }
    
    universal_plus = designer.design_universal_plus(
        base_lesson, 
        target_profiles=["autistic", "adhd", "dyslexic", "dyspraxic"]
    )
    
    print("Universal+ Lesson Generated!")
    print(f"UDL Layers: {list(universal_plus['udl_layer'].keys())}")
    print(f"Neuroaffirming Profiles: {list(universal_plus['neuroaffirming_layer'].keys())}")
    print(f"Identity Bonus: {universal_plus['identity_bonus_integration']['bonus']}")
    print(f"Team Roles: {list(universal_plus['collaborative_structure']['recommended_composition'].keys())}")
    print(f"Assessment: {universal_plus['assessment_integration']['mastery_levels'].keys()}")