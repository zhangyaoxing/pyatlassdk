"""Generated model for GroupSettings. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class GroupSettings(BaseModel):
    """Collection of settings that configures the project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    is_atlas_home_page_ai_assistant_enabled: bool | None = Field(default=None, alias="isAtlasHomePageAiAssistantEnabled", description="Flag that indicates whether the MongoDB Assistant on the Atlas Home Page is enabled for the specified project.")
    is_cluster_ai_assistant_enabled: bool | None = Field(default=None, alias="isClusterAiAssistantEnabled", description="Flag that indicates whether the AI Cluster Assistant is enabled for the specified project.")
    is_collect_database_specifics_statistics_enabled: bool | None = Field(default=None, alias="isCollectDatabaseSpecificsStatisticsEnabled", description="Flag that indicates whether to collect database-specific metrics for the specified project.")
    is_data_explorer_enabled: bool | None = Field(default=None, alias="isDataExplorerEnabled", description="Flag that indicates whether to enable the Data Explorer for the specified project.")
    is_data_explorer_gen_ai_features_enabled: bool | None = Field(default=None, alias="isDataExplorerGenAIFeaturesEnabled", description="Flag that indicates whether to enable the use of generative AI features which make requests to 3rd party services in Data Explorer for the specified project.")
    is_data_explorer_gen_ai_sample_document_passing_enabled: bool | None = Field(default=None, alias="isDataExplorerGenAISampleDocumentPassingEnabled", description="Flag that indicates whether to enable the passing of sample field values with the use of generative AI features in the Data Explorer for the specified project.")
    is_data_validation_enabled: bool | None = Field(default=None, alias="isDataValidationEnabled", description="Flag that indicates whether data validation is enabled for all clusters in the specified project.")
    is_extended_storage_sizes_enabled: bool | None = Field(default=None, alias="isExtendedStorageSizesEnabled", description="Flag that indicates whether to enable extended storage sizes for the specified project.")
    is_native_reranking_enabled: bool | None = Field(default=None, alias="isNativeRerankingEnabled", description="Flag that indicates whether to enable Native Reranking with Voyage AI models in the Aggregation Pipeline for the specified project.")
    is_performance_advisor_enabled: bool | None = Field(default=None, alias="isPerformanceAdvisorEnabled", description="Flag that indicates whether to enable the Performance Advisor and Profiler for the specified project.")
    is_realtime_performance_panel_enabled: bool | None = Field(default=None, alias="isRealtimePerformancePanelEnabled", description="Flag that indicates whether to enable the Real Time Performance Panel for the specified project.")
    is_schema_advisor_enabled: bool | None = Field(default=None, alias="isSchemaAdvisorEnabled", description="Flag that indicates whether to enable the Schema Advisor for the specified project.")
