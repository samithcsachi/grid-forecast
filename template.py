import os 
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


project_name = 'GridForecast_Electricity_Demand_Predictor'


list_of_files = [

    # SRC MAIN PACKAGE 
    f"SRC/{project_name}/__init__.py",
    
    # ENTITY-BASED CONFIG 
    # Entities
    f"SRC/{project_name}/entity/__init__.py",
    f"SRC/{project_name}/entity/config_entity.py",
    
    # Configuration manager
    f"SRC/{project_name}/config/__init__.py",
    f"SRC/{project_name}/config/configuration.py",
    
    # Constants
    f"SRC/{project_name}/constants/__init__.py",
    f"SRC/{project_name}/constants/constants.py",
    
    
    # HELPER MODULES 

    f"SRC/{project_name}/data_ingestion/__init__.py",
    f"SRC/{project_name}/data_ingestion/fetch.py",          

    f"SRC/{project_name}/validation/__init__.py",
    f"SRC/{project_name}/validation/validate_schema.py",     
    f"SRC/{project_name}/validation/validate_data.py",       

    f"SRC/{project_name}/transformation/__init__.py",
    f"SRC/{project_name}/transformation/preprocess.py",      
    f"SRC/{project_name}/transformation/feature_engineering.py", 

    f"SRC/{project_name}/training/__init__.py",
    f"SRC/{project_name}/training/train_sarima.py",          
    f"SRC/{project_name}/training/train_prophet.py",         
    f"SRC/{project_name}/training/train_lstm.py",            
    f"SRC/{project_name}/training/trainer.py",               

    f"SRC/{project_name}/evaluation/__init__.py",
    f"SRC/{project_name}/evaluation/metrics.py",            
    f"SRC/{project_name}/evaluation/evaluate.py",            

    f"SRC/{project_name}/monitoring/__init__.py",
    f"SRC/{project_name}/monitoring/drift_detection.py",    
    f"SRC/{project_name}/monitoring/performance_monitor.py", 

    f"SRC/{project_name}/registry/__init__.py",
    f"SRC/{project_name}/registry/save_model.py",           
    f"SRC/{project_name}/registry/load_model.py",           
    f"SRC/{project_name}/registry/promotion.py",             

    f"SRC/{project_name}/experiments/__init__.py",
    f"SRC/{project_name}/experiments/tracker.py",            
    
    # Database
    f"SRC/{project_name}/database/__init__.py",
    f"SRC/{project_name}/database/supabase_client.py",
    f"SRC/{project_name}/database/experiment_repository.py",
    f"SRC/{project_name}/database/model_repository.py",
    
    
    # COMPONENTS 
    # Stage implementations
    f"SRC/{project_name}/components/__init__.py",
    f"SRC/{project_name}/components/stage_01_data_ingestion.py",
    f"SRC/{project_name}/components/stage_02_data_validation.py",
    f"SRC/{project_name}/components/stage_03_transformation.py",
    f"SRC/{project_name}/components/stage_04_model_training.py",
    f"SRC/{project_name}/components/stage_05_model_evaluation.py",
    f"SRC/{project_name}/components/stage_06_drift_monitoring.py",
    f"SRC/{project_name}/components/stage_07_model_registry.py",
    
    
    # PIPELINES 
    # Pipeline orchestration
    f"SRC/{project_name}/pipelines/__init__.py",
    f"SRC/{project_name}/pipelines/training_pipeline.py",
    f"SRC/{project_name}/pipelines/retraining_pipeline.py",
    f"SRC/{project_name}/pipelines/inference_pipeline.py",
    f"SRC/{project_name}/pipelines/monitoring_pipeline.py",
    
    
    # UTILITIES 
    # General utilities
    f"SRC/{project_name}/utils/__init__.py",
    f"SRC/{project_name}/utils/logger.py",
    f"SRC/{project_name}/utils/config_loader.py",
    f"SRC/{project_name}/utils/time_utils.py",
    f"SRC/{project_name}/utils/helpers.py",
    
      
    # USER-FACING APPLICATIONS
    # FastAPI application
    f"SRC/{project_name}/app/__init__.py",
    f"SRC/{project_name}/app/fastapi_app.py",
    
    # Streamlit dashboard
    f"SRC/{project_name}/app/streamlit_app.py",
    
    
    # TESTS 
    # Test suite
    "tests/__init__.py",
    "tests/test_ingestion.py",
    "tests/test_validation.py",
    "tests/test_transformation.py",
    "tests/test_training.py",
    "tests/test_evaluation.py",
    "tests/test_registry.py",
    "tests/test_monitoring.py",
    "tests/test_database.py",
    
    
    # RESEARCH & NOTEBOOKS 
    # Research notebooks
    "research/01_data_exploration.ipynb",
    "research/02_feature_engineering.ipynb",
    "research/03_sarima_experiments.ipynb",
    "research/04_prophet_experiments.ipynb",
    "research/05_lstm_experiments.ipynb",
    "research/06_drift_analysis.ipynb",
    
    
    # CONFIGURATION FILES
    # YAML configuration
    "configs/config.yaml",
    "configs/schema.yaml",
    "configs/params.yaml",
    
    
      
    # CI/CD 
    # GitHub workflows
    ".github/workflows/ci.yaml",
    ".github/workflows/daily_pipeline.yaml",
    ".github/workflows/deploy.yaml",
    
    
    # ROOT FILES 
    # Root configuration files
    "Dockerfile",
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
        