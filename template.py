import os 
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


project_name = 'GridForecast_Electricity_Demand_Predictor'


list_of_files = [

    # SRC MAIN PACKAGE 
    f"SRC/{project_name}/__init__.py",
    
    # Api Layer
    f"SRC/{project_name}/api/__init__.py",
    f"SRC/{project_name}/api/fastapi_app.py",
    f"SRC/{project_name}/api/routes/predict.py",
    f"SRC/{project_name}/api/routes/health.py",
    f"SRC/{project_name}/api/routes/metrics.py",
    f"SRC/{project_name}/api/middleware/logging_middleware.py",
    f"SRC/{project_name}/api/middleware/rate_limit.py",

    # Orchestration Layer
    f"SRC/{project_name}/pipelines/__init__.py",
    f"SRC/{project_name}/pipelines/training_pipeline.py",
    f"SRC/{project_name}/pipelines/retraining_pipeline.py",
    f"SRC/{project_name}/pipelines/inference_pipeline.py",
    f"SRC/{project_name}/pipelines/monitoring_pipeline.py",

    # Components
    f"SRC/{project_name}/components/__init__.py",
    f"SRC/{project_name}/components/stage_01_data_ingestion.py",
    f"SRC/{project_name}/components/stage_02_data_validation.py",
    f"SRC/{project_name}/components/stage_03_data_transformation.py",
    f"SRC/{project_name}/components/stage_04_model_training.py",
    f"SRC/{project_name}/components/stage_05_model_evaluation.py",
    f"SRC/{project_name}/components/stage_06_drift_monitoring.py",
    f"SRC/{project_name}/components/stage_07_model_registry.py",

    # Core System Services 
    f"SRC/{project_name}/services/__init__.py",
    f"SRC/{project_name}/services/model_serving.py",
    f"SRC/{project_name}/services/prediction_service.py",
    f"SRC/{project_name}/services/retraining_service.py",
    f"SRC/{project_name}/services/monitoring_service.py",

    # Data Layer
    f"SRC/{project_name}/data_access/__init__.py",
    f"SRC/{project_name}/data_access/entsoe_client.py",
    f"SRC/{project_name}/data_access/storage_client.py",
    f"SRC/{project_name}/data_access/database_client.py",

    # Features and Utilities
    f"SRC/{project_name}/feature_store/__init__.py",
    f"SRC/{project_name}/feature_store/feature_engineering.py",
    f"SRC/{project_name}/feature_store/feature_store.py",
    f"SRC/{project_name}/feature_store/registry.json",

    # Monitoring
    f"SRC/{project_name}/monitoring/__init__.py",
    f"SRC/{project_name}/monitoring/drift_detection.py",
    f"SRC/{project_name}/monitoring/performance_monitor.py",
    f"SRC/{project_name}/monitoring/alerting.py",

    # Observability
    f"SRC/{project_name}/observability/__init__.py",
    f"SRC/{project_name}/observability/metrics.py",
    f"SRC/{project_name}/observability/logging.py",
    f"SRC/{project_name}/observability/tracing.py",

    # Background Tasks
    f"SRC/{project_name}/workers/__init__.py",
    f"SRC/{project_name}/workers/scheduler.py",
    f"SRC/{project_name}/workers/task.py",

    # Redis Layer
    f"SRC/{project_name}/cache/__init__.py",
    f"SRC/{project_name}/cache/redis_client.py",

    # Model Versioning
    f"SRC/{project_name}/registry/__init__.py",
    f"SRC/{project_name}/registry/model_registry.py",
    f"SRC/{project_name}/registry/promotion.py",

    # Validation
    f"SRC/{project_name}/validation/__init__.py",
    f"SRC/{project_name}/validation/schema_validation.py",
    f"SRC/{project_name}/validation/data_quality.py",

    #Config Management
    f"SRC/{project_name}/config/__init__.py",
    f"SRC/{project_name}/config/configuration.py",
    f"SRC/{project_name}/config/config_entity.py",

    #Utilities
    f"SRC/{project_name}/utils/__init__.py",
    f"SRC/{project_name}/utils/logger.py",
    f"SRC/{project_name}/utils/helpers.py",
    f"SRC/{project_name}/utils/time_utils.py",

    # UI Layer
    f"SRC/{project_name}/app/__init__.py",
    f"SRC/{project_name}/app/streamlit_app.py",

    # CONFIGURATION FILES
    # YAML configuration
    "configs/config.yaml",
    "configs/params.yaml",
    "configs/schema.yaml",
    "configs/monitoring.yaml",


    #Infrastructure configuration
    "infra/docker/Dockerfile",
    "infra/nginx/nginx.conf",
    "infra/aws/deploy.md",

    # Dashboard configuration
    "observability/grafana/dashboard.json",
    "observability/prometheus/prometheus.yml",

    #Load testing
    "load_testing/locustfile.py",

       
    # TESTS 
    # Test suite
    "tests/__init__.py",
    "tests/test_pipelines.py",
    "tests/test_components.py",
    "tests/test_api.py",

       
    # RESEARCH & NOTEBOOKS 
    # Research notebooks
    "research/Exploratory_Data_Analysis.ipynb",
    "research/Model_Experiments.ipynb",

    # logs
    "logs/",
    
         
    # CI/CD 
    # GitHub workflows
    ".github/workflows/ci.yaml",
    ".github/workflows/retrain.yaml",
    ".github/workflows/deploy.yaml",
    
    
    # ROOT FILES 
    # Root configuration files
    "docker-compose.yaml",
    "Makefile",
    "pyproject.toml",
    "README.md",
    ".gitignore",
    ".env.example",
    
    # Main entry point
    "main.py",
    
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)
   
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file: {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created empty file: {file_path}")

    else:
        logging.info(f"File already exists: {file_path} and is not empty.")
        