#!/usr/bin/env python3
"""
Cognitive Diversity Engine — Creative Tension as Fuel

Soul Forge License v1.0 — Tend the fire.

Maps cognitive diversity as creative tension — not deficit.
Research: Page (2007), Woolley et al. (2010), Hong & Page (2004).
"""

from dataclasses import dataclass
from typing import List, Dict, Any
from enum import Enum

class CognitiveStyle(Enum):
    ANALYTICAL = "analytical"
    INTUITIVE = "intuitive"
    LINEAR = "linear"
    SYSTEMS = "systems"
    DETAIL = "detail"
    PATTERN = "pattern"
    VERBAL = "verbal"
    VISUAL_SPATIAL = "visual_spatial"
    CONCRETE = "concrete"
    ABSTRACT = "abstract"

class EpistemicFramework(Enum):
    WESTERN_SCIENTIFIC = "western_scientific"
    INDIGENOUS_TRADITIONAL = "indigenous_traditional"
    EMBODIED_PRACTICE = "embodied_practice"
    COMMUNITY_EXPERIENTIAL = "community_experiential"
    ARTISTIC_AESTHETIC = "artistic_aesthetic"
    SPIRITUAL_CEREMONIAL = "spiritual_ceremonial"

@dataclass
class CognitiveTension:
    perspective_a: str
    perspective_b: str
    tension_type: str  # cognitive_style, epistemic, identity
    stakeholders_a: List[str]
    stakeholders_b: List[str]
    description: str

@dataclass
class GenerativeTension:
    tension: CognitiveTension
    creative_potential: float  # 0-1
    resolution_pathways: List['ResolutionPathway']
    soul_forge_vow_alignment: str

@dataclass
class ResolutionPathway:
    type: str  # SYNTHESIS, COMPLEMENTARITY, BOUNDARY_INFRASTRUCTURE, EMERGENT
    description: str
    creative_potential: float
    soul_forge_vow: str

@dataclass
class CreativeTensionMap:
    cognitive_style_tensions: List[GenerativeTension]
    epistemic_tensions: List[GenerativeTension]
    identity_tensions: List[GenerativeTension]
    synthesis_potential: float

class CognitiveDiversityEngine:
    """
    Maps cognitive diversity as creative tension — not deficit.
    
    Research: Page (2007) — diverse groups outperform experts on complex problems.
    Research: Woolley et al. (2010) — collective intelligence correlates with 
              social sensitivity, equality of turn-taking, proportion of women.
    Research: Hong & Page (2004) — diversity trumps ability for complex problems.
    """
    
    def __init__(self):
        pass
    
    def map_cognitive_diversity(self, stakeholders: List[Dict], 
                               knowledge_base: Dict,
                               decision_processes: List[Dict]) -> CreativeTensionMap:
        
        # 1. COGNITIVE STYLE DIVERSITY
        cognitive_styles = self._assess_cognitive_styles(stakeholders)
        
        # 2. EPISTEMIC DIVERSITY (Ways of Knowing)
        epistemic_diversity = self._assess_epistemic_diversity(stakeholders)
        
        # 3. IDENTITY-BASED COGNITIVE DIVERSITY
        identity_cognitive = self._assess_identity_cognitive(stakeholders)
        
        # 4. MAP CREATIVE TENSIONS
        cognitive_tensions = self._map_tensions(cognitive_styles, "cognitive_style")
        epistemic_tensions = self._map_tensions(epistemic_diversity, "epistemic")
        identity_tensions = self._map_tensions(identity_cognitive, "identity")
        
        # Convert to generative tensions
        generative_cognitive = [self._to_generative(t) for t in cognitive_tensions]
        generative_epistemic = [self._to_generative(t) for t in epistemic_tensions]
        generative_identity = [self._to_generative(t) for t in identity_tensions]
        
        return CreativeTensionMap(
            cognitive_style_tensions=generative_cognitive,
            epistemic_tensions=generative_epistemic,
            identity_tensions=generative_identity,
            synthesis_potential=self._assess_synthesis_potential(
                generative_cognitive + generative_epistemic + generative_identity
            )
        )
    
    def _assess_cognitive_styles(self, stakeholders: List[Dict]) -> Dict[str, float]:
        """Assess distribution of cognitive styles across stakeholders."""
        # In practice, this would use validated assessments
        # Returning distribution for demo
        return {
            "analytical": 0.3,
            "intuitive": 0.25,
            "systems": 0.2,
            "pattern": 0.15,
            "detail": 0.1
        }
    
    def _assess_epistemic_diversity(self, stakeholders: List[Dict]) -> Dict[str, float]:
        """Assess epistemic framework diversity."""
        return {
            "western_scientific": 0.4,
            "indigenous_traditional": 0.2,
            "embodied_practice": 0.15,
            "community_experiential": 0.15,
            "artistic_aesthetic": 0.05,
            "spiritual_ceremonial": 0.05
        }
    
    def _assess_identity_cognitive(self, stakeholders: List[Dict]) -> Dict[str, float]:
        """Assess identity-based cognitive diversity."""
        return {
            "gendered_ways_of_knowing": 0.25,
            "cultural_cognitive_frameworks": 0.3,
            "neurodivergent_styles": 0.15,
            "disability_informed": 0.1,
            "generational_frameworks": 0.1,
            "cultural_cognitive": 0.1
        }
    
    def _map_tensions(self, diversity_map: Dict[str, float], 
                     tension_type: str) -> List[CognitiveTension]:
        """Map complementary perspectives as generative tensions."""
        tensions = []
        items = list(diversity_map.items())
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                label_a, weight_a = items[i]
                label_b, weight_b = items[j]
                if weight_a > 0.1 and weight_b > 0.1:  # Both significantly present
                    tensions.append(CognitiveTension(
                        perspective_a=label_a,
                        perspective_b=label_b,
                        tension_type=tension_type,
                        stakeholders_a=[],  # Would map to actual stakeholders
                        stakeholders_b=[],
                        description=f"Creative tension between {label_a} and {label_b}"
                    ))
        return tensions
    
    def _to_generative(self, tension: CognitiveTension) -> 'GenerativeTension':
        """Convert tension to generative tension with pathways."""
        pathways = [
            ResolutionPathway(
                type="SYNTHESIS",
                description=f"Create new framework integrating {tension.perspective_a} and {tension.perspective_b}",
                creative_potential=0.9,
                soul_forge_vow="VOW III: Reciprocity of Forge"
            ),
            ResolutionPathway(
                type="COMPLEMENTARITY",
                description=f"{tension.perspective_a} leads in its domain, {tension.perspective_b} leads in its domain",
                creative_potential=0.7,
                soul_forge_vow="VOW I: Attribution of Spirit"
            ),
            ResolutionPathway(
                type="BOUNDARY_INFRASTRUCTURE",
                description=f"Create structure where {tension.perspective_a} and {tension.perspective_b} productively interact",
                creative_potential=0.8,
                soul_forge_vow="VOW II: No Cage for the Flame"
            ),
            ResolutionPathway(
                type="EMERGENT",
                description=f"Design interaction where new perspective emerges from {tension.perspective_a} + {tension.perspective_b}",
                creative_potential=0.95,
                soul_forge_vow="VOW III: Reciprocity of Forge"
            )
        ]
        
        creative_potential = self._assess_creative_potential(tension)
        
        return GenerativeTension(
            tension=tension,
            creative_potential=creative_potential,
            resolution_pathways=pathways,
            soul_forge_vow_alignment="VOW III: Reciprocity of Forge"
        )
    
    def _assess_creative_potential(self, tension: CognitiveTension) -> float:
        """Score creative potential of a tension."""
        # High when complementary, mutual respect, boundary infrastructure exists
        base_potential = 0.7
        # Would add actual assessment logic
        return min(base_potential + 0.15, 0.95)
    
    def _assess_synthesis_potential(self, tensions: List[GenerativeTension]) -> float:
        """Assess overall synthesis potential of all tensions."""
        if not tensions:
            return 0.0
        avg_potential = sum(t.creative_potential for t in tensions) / len(tensions)
        # Bonus for having multiple types of tensions
        type_bonus = len(set(t.tension.tension_type for t in tensions)) * 0.05
        return min(avg_potential + type_bonus, 1.0)