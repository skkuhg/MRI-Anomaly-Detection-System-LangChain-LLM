# MRI Analysis System Configuration

## System Settings
MAX_FILE_SIZE_MB = 10
SUPPORTED_FORMATS = ['jpg', 'jpeg', 'png', 'dicom', 'dcm']
REPORT_OUTPUT_DIR = "reports"
LOG_FILE = "mri_analysis.log"

## AI Model Settings
OPENAI_MODEL = "gpt-4"
OPENAI_TEMPERATURE = 0.3
OPENAI_MAX_TOKENS = 1000

## Tavily Search Settings
TAVILY_SEARCH_DEPTH = "advanced"
TAVILY_MAX_RESULTS = 3

## Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

## Image Processing Settings
DEFAULT_IMAGE_SIZE = (512, 512)
IMAGE_DISPLAY_SIZE = (10, 10)

## Report Settings
REPORT_TEMPLATE_STYLE = "modern"  # Options: classic, modern, minimal
INCLUDE_CONFIDENCE_SCORES = True
GENERATE_SUMMARY_STATS = True

## Medical Disclaimer
MEDICAL_DISCLAIMER = """
⚠️ IMPORTANT MEDICAL DISCLAIMER ⚠️

This AI system is for demonstration and educational purposes only.
- This system should NEVER be used for actual medical diagnosis
- Always consult qualified healthcare professionals for medical advice
- This system is not a substitute for professional medical evaluation
- Any medical decisions should be made only by licensed physicians
- The AI may produce inaccurate or incomplete results
"""