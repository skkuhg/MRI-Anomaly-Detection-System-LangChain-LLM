# MRI Anomaly Detection and Data Interpretation System

An AI-powered system for MRI anomaly detection using LangChain, OpenAI GPT-4o-mini, and Tavily AI API with interactive image upload capabilities.

## 🧠 Features

- **Interactive MRI Upload**: Drag-and-drop interface for MRI image analysis
- **AI-Powered Detection**: Simulated anomaly detection with realistic results
- **Medical Context Search**: Tavily AI integration for medical research
- **GPT-4 Explanations**: Detailed medical interpretations using OpenAI GPT-4o-mini
- **Professional Reports**: Comprehensive HTML reports with medical formatting
- **Batch Processing**: Process multiple MRI images simultaneously
- **Error Handling**: Robust error handling and logging system
- **System Testing**: Built-in testing and validation functions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- OpenAI API key
- Tavily AI API key

### Installation

1. Clone this repository:
```bash
git clone https://github.com/skkuhg/MRI-Anomaly-Detection-System-LangChain-LLM.git
cd MRI-Anomaly-Detection-System-LangChain-LLM
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Open the Jupyter notebook:
```bash
jupyter notebook mri_anomaly_detection_system.ipynb
```

4. Update API keys in the notebook:
   - Replace `OPENAI_API_KEY` with your OpenAI API key
   - Replace `TAVILY_API_KEY` with your Tavily API key

### Usage

1. **Interactive Mode**: 
   - Run all cells in the notebook
   - Use the interactive upload interface to select MRI images
   - Click "Analyze MRI" to process images

2. **Programmatic Usage**:
```python
# Initialize the system
mri_system = MRIAnalysisSystem(tavily_api_key="your_tavily_key")

# Analyze an image
results = mri_system.analyze_mri_image("path/to/mri.jpg", "PATIENT_001")

# Display results
mri_system.display_results_summary(results)
```

3. **Testing the System**:
```python
# Run comprehensive system test
run_full_system_test()

# Check system health
system_health_check(mri_system)
```

## 📊 System Components

### Core Classes

- **`MRIImageHandler`**: Image validation, preprocessing, and display
- **`TavilyMRIAnalyzer`**: Medical context search and simulated analysis
- **`MedicalExplanationGenerator`**: GPT-4o-mini powered medical explanations
- **`MRIReportGenerator`**: Professional HTML report generation
- **`MRIAnalysisSystem`**: Main orchestration system
- **`MRIUploadInterface`**: Interactive Jupyter widget interface

### Key Features

- **Image Support**: JPG, JPEG, PNG, DICOM, DCM (up to 10MB)
- **Batch Processing**: Process multiple images with progress tracking
- **Error Handling**: Comprehensive error handling and logging
- **Report Generation**: Professional HTML reports with medical formatting
- **Testing Suite**: Built-in testing and validation functions

## 📁 File Structure

```
mri-anomaly-detection/
├── mri_anomaly_detection_system.ipynb  # Main notebook
├── requirements.txt                     # Python dependencies
├── README.md                           # This file
├── LICENSE                             # MIT License
├── .env.example                        # Environment variables template
├── .gitignore                          # Git ignore rules
└── sample_images/                      # Sample MRI images (if available)
```

## 🔧 Configuration

### API Keys

Create a `.env` file or set environment variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### System Settings

- **Max file size**: 10MB
- **Supported formats**: JPG, JPEG, PNG, DICOM, DCM
- **Report output**: HTML format
- **Logging**: Automatic logging to `mri_analysis.log`

## 📸 Example Usage

### Upload and Analyze MRI

1. Run the notebook cells to initialize the system
2. Use the interactive upload widget
3. Select an MRI image (JPG, PNG, DICOM)
4. Enter patient ID
5. Click "Analyze MRI"
6. View results and generated report

### Batch Processing

```python
# Process multiple images
image_paths = ["mri1.jpg", "mri2.jpg", "mri3.jpg"]
batch_results = batch_process_mri_images(image_paths, mri_system)
```

## 🏥 Medical Disclaimer

**⚠️ IMPORTANT: This system is for demonstration and educational purposes only.**

- This AI system should **NEVER** be used for actual medical diagnosis
- Always consult qualified healthcare professionals for medical advice
- This system is not a substitute for professional medical evaluation
- Any medical decisions should be made only by licensed physicians
- The AI may produce inaccurate or incomplete results

## 🧪 Testing

The system includes comprehensive testing capabilities:

```python
# Run full system test
run_full_system_test()

# Test individual components
test_system_components()

# Check system health
system_health_check(mri_system)

# Create sample test images
sample_images = create_sample_mri_images(3)
```

## 📋 System Requirements

- **Python**: 3.8+
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 1GB free space for reports and logs
- **Internet**: Required for API access (OpenAI, Tavily)

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Verify API keys are correctly set
   - Check API quotas and billing

2. **Image Upload Issues**:
   - Ensure image format is supported
   - Check file size (max 10MB)
   - Verify file is not corrupted

3. **Memory Issues**:
   - Process smaller batches
   - Restart Jupyter kernel

### Getting Help

- Check the notebook output for detailed error messages
- Run `system_health_check(mri_system)` to diagnose issues
- View logs with `view_system_logs()`

## 🚧 Development Roadmap

### Future Enhancements

1. **Real Medical API Integration**: Replace simulation with actual medical imaging APIs
2. **DICOM Support**: Full DICOM file parsing and metadata extraction
3. **Web Application**: Standalone web interface using Streamlit or Gradio
4. **Database Integration**: Store results in medical databases
5. **HIPAA Compliance**: Healthcare data protection measures
6. **Advanced Visualization**: 3D rendering and annotation tools
7. **Multi-sequence Support**: T1, T2, FLAIR, DWI sequence analysis

### Technical Improvements

- Async processing for better performance
- Cloud deployment options (AWS, Azure, GCP)
- Docker containerization
- API endpoint creation
- User authentication system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI**: GPT-4o-mini API for medical explanations
- **Tavily AI**: Medical context search capabilities
- **LangChain**: AI application framework
- **Jupyter**: Interactive notebook environment

## 📞 Contact

For questions or support, please open an issue on GitHub or contact the development team.

---

**Remember**: This system is for educational and demonstration purposes only. Always consult qualified medical professionals for actual medical diagnosis and treatment.
