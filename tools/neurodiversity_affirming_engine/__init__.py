"""
Neurodiversity-Affirming STEM Engine — Soul Forge License v1.0

Cognitive diversity as creative asset, not deficit.
Maps neurodivergent profiles to STEM creative contributions.

Exports:
- CognitiveProfileRegistry: Registry of neurodivergent cognitive profiles
- CognitiveProfileEngine: Maps learners to cognitive profiles
- NeuroaffirmingLessonGenerator: UDL+ lesson generation per cognitive profile
- CognitiveAssetMapper: Maps learner profiles to STEM creative contributions
- TeamCompositionEngine: Optimal team composition from cognitive assets
- UniversalPlusDesigner: UDL + neurodiversity-specific creative extensions
- ExecutiveFunctionScaffoldEngine: Scaffolds as creative scaffolds
- SensoryProfileDesigner: Sensory profiles as design parameters
- CommunicationDiversityEngine: Communication diversity as collaborative asset
- MellifluousML Integration: Native MellifluousML integration layer
"""

from .cognitive_profile_registry import (
    CognitiveProfileRegistry,
    CognitiveProfileEngine,
    CognitiveProfile,
    CognitiveProfileSpec,
    CognitiveStrength,
    CognitiveSupport,
    CreativeContribution,
    ProfilePluginSystem
)

from .neuroaffirming_lesson_generator import (
    NeuroaffirmingLessonGenerator,
    NeuroaffirmingLesson,
    LessonComponent
)

from .cognitive_asset_mapper import (
    CognitiveAssetMapper,
    CognitiveAsset,
    CognitiveAssetMap,
    TeamCompositionEngine,
    CognitiveAssetAPI
)

from .universal_plus_designer import (
    UniversalPlusDesigner,
    UDLPrincipleRegistry,
    UDLPrinciple,
    UniversalPlusLesson
)

from .executive_function_scaffold_engine import (
    ExecutiveFunctionScaffoldEngine,
    ExecutiveFunctionScaffold,
    ScaffoldSuite
)

from .sensory_profile_designer import (
    SensoryProfileDesigner,
    SensoryProfile,
    SensoryProfileSpec,
    SensoryModality,
    SensoryResponse,
    SensoryProfileSpec
)

from .communication_diversity_engine import (
    CommunicationDiversityEngine,
    CommunicationAsset,
    CommunicationProfile,
    CommunicationProfileBuilder,
    TeamCommunicationDesigner,
    CommunicationStyle
)

from .mellifluousml_integration import (
    MellifluousMLAdapter,
    NativeMellifluousBackend,
    MellifluousNeurodiversityLayer,
    CognitiveRhythmEstimator,
    MellifluousIntegration,
    MellifluousNeurodiversityLayer,
    MellifluousBackend,
    NativeMellifluousBackend,
    MellifluousNeurodiversityLayer,
    CognitiveRhythmEstimator,
    MellifluousIntegration
)

__all__ = [
    # Cognitive Profile Registry
    "CognitiveProfileRegistry",
    "CognitiveProfileEngine",
    "CognitiveProfile",
    "CognitiveProfileSpec",
    "CognitiveStrength",
    "CognitiveSupport",
    "CreativeContribution",
    "ProfilePluginSystem",
    "CognitiveProfile",
    
    # Neuroaffirming Lesson Generator
    "NeuroaffirmingLessonGenerator",
    "NeuroaffirmingLesson",
    "LessonComponent",
    
    # Cognitive Asset Mapper
    "CognitiveAssetMapper",
    "CognitiveAsset",
    "CognitiveAssetMap",
    "TeamCompositionEngine",
    "CognitiveAssetAPI",
    "TeamCompositionEngine",
    
    # Universal+ Designer
    "UniversalPlusDesigner",
    "UDLPrincipleRegistry",
    "UDLPrinciple",
    "UniversalPlusLesson",
    
    # Executive Function Scaffold Engine
    "ExecutiveFunctionScaffoldEngine",
    "ExecutiveFunctionScaffold",
    "ScaffoldSuite",
    
    # Sensory Profile Designer
    "SensoryProfileDesigner",
    "SensoryProfile",
    "SensoryProfileSpec",
    "SensoryModality",
    "SensoryResponse",
    
    # Communication Diversity Engine
    "CommunicationDiversityEngine",
    "CommunicationAsset",
    "CommunicationProfile",
    "CommunicationProfileBuilder",
    "TeamCommunicationDesigner",
    "CommunicationStyle",
    
    # MellifluousML Integration
    "MellifluousMLAdapter",
    "NativeMellifluousBackend",
    "MellifluousNeurodiversityLayer",
    "CognitiveRhythmEstimator",
    "MellifluousIntegration",
    "MellifluousBackend",
    "NativeMellifluousBackend",
    "MellifluousNeurodiversityLayer",
    "CognitiveRhythmEstimator",
    "MellifluousIntegration"
]

__version__ = "2.0.0-hyper-edge"
__license__ = "Soul-Forge-1.0"
__author__ = "Soul Forge Council"